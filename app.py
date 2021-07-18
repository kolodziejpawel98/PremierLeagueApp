from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog
import csv

cls, wnd = uic.loadUiType('app.ui')

table = {
    "Arsenal" : 0,
    "Aston Villa" : 0,
    "Brighton" : 0,
    "Burnley" : 0,
    "Chelsea" : 0,
    "Crystal Palace" : 0,
    "Everton" : 0,
    "Fulham" : 0,
    "Leeds" : 0,
    "Leicester" : 0,
    "Liverpool" : 0,
    "Man City" : 0,
    "Man Utd" : 0,
    "Newcastle" : 0,
    "Sheffield Utd" : 0,
    "Southampton" : 0,
    "Spurs" : 0,
    "West Brom" : 0,
    "West Ham" : 0,
    "Wolves" : 0
}

class Match:
    def __init__(self, match_num, round_num, date, location, h_team, a_team, h_goals, a_goals):
        self.match_num = match_num
        self.round_num = round_num
        self.date = date
        self.location = location
        self.h_team = h_team
        self.a_team = a_team
        self.h_goals = h_goals
        self.a_goals = a_goals

    def print_values(self):
        print("Match number: " + self.match_num)
        print("Round number: " + self.round_num)
        print("Date: " + self.date)
        print("Location: " + self.location)
        print("Home team: " + self.h_team)
        print("Away team: " + self.a_team)
        print("Result: " + self.h_goals + " - " + self.a_goals)


def calc_points(list_of_matches, table):
    for team in table:
        table[team] = 0
    for game in list_of_matches[1:]:
        if game.h_goals > game.a_goals:
            table[game.h_team] += 3
        elif game.h_goals == game.a_goals:
            table[game.h_team] += 1
            table[game.a_team] += 1
        elif game.h_goals < game.a_goals:
            table[game.a_team] += 3

def calc_goals_scored(list_of_matches, table):
    for team in table:
        table[team] = 0
    for game in list_of_matches[1:]:
        table[game.h_team] += int(game.h_goals)
        table[game.a_team] += int(game.a_goals)

def calc_goals_conceded(list_of_matches, table):
    for team in table:
        table[team] = 0
    for game in list_of_matches[1:]:
        table[game.h_team] += int(game.a_goals)
        table[game.a_team] += int(game.h_goals)

def find_game(list_of_matches, team, round):
    for match in list_of_matches:
        if match.h_team == team:
            if match.round_num == str(round):
                return match.h_team + " " + match.h_goals + " - " + match.a_goals + " " + match.a_team
        elif match.a_team == team:
            if match.round_num == str(round):
                return match.h_team + " " + match.h_goals + " - " + match.a_goals + " " + match.a_team

def sort_and_print(table):
    final_table = ""

    table_end_of_season = dict( sorted(table.items(),
                       key=lambda item: item[1],
                       reverse=True))

    for key in table_end_of_season:
            final_table += key
            final_table += " : "
            final_table += str(table_end_of_season[key])
            final_table += '\n'

    return str(final_table)


class Nasza(wnd, cls):

    list_of_matches = []
    final_table = ""

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def on_pushButton_openFile_pressed(self):
        f_name = QFileDialog.getOpenFileName(self, 'Open file')
        self.label_fileName.setText(f_name[0])
        file = open(f_name[0], 'r')
        reader = csv.reader(file)
        final_table = ""

        for row in reader:
            self.list_of_matches.append(Match(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

        calc_points(self.list_of_matches, table)
        self.textBrowser_table.setText(sort_and_print(table))
        self.spinBox_RoundNumber.setMaximum(38)
        for team in table:
            self.comboBox_roundTeam.addItem(team)
        self.comboBox_goalsScoredConceded.addItem("---")
        self.comboBox_goalsScoredConceded.addItem("Gole strzelone")
        self.comboBox_goalsScoredConceded.addItem("Gole stracone")
        self.textBrowser_goalsScoredConceded.setText("")

    def on_comboBox_roundTeam_activated(self):
        self.spinBox_RoundNumber.setValue(0)

    def on_spinBox_RoundNumber_valueChanged(self):
        self.lineEdit_roundResult.setText(find_game(self.list_of_matches, self.comboBox_roundTeam.currentText(), self.spinBox_RoundNumber.value()))

    def on_comboBox_goalsScoredConceded_activated(self):
        if self.comboBox_goalsScoredConceded.currentText() == "Gole strzelone":
            calc_goals_scored(self.list_of_matches, table)
            self.textBrowser_goalsScoredConceded.setText(sort_and_print(table))
        elif self.comboBox_goalsScoredConceded.currentText() == "Gole stracone":
            calc_goals_conceded(self.list_of_matches, table)
            self.textBrowser_goalsScoredConceded.setText(sort_and_print(table))
        else:
            self.textBrowser_goalsScoredConceded.setText("")

a = QApplication([])
o = Nasza()
o.show()
a.exec()
