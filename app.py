from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog
import csv

cls, wnd = uic.loadUiType('app.ui')


# file = open('sezon20202021.csv', 'r')
# reader = csv.reader(file)

table = { #zmienić to na klase table z polami team i points!!!!!!!!!!!!!!!!!!
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

print("po table")

# for y in table:
#     print(y,':',table[y])

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


# list_of_matches = []

def calc_points_for_game(list_of_matches, table):
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

def find_game(list_of_matches, team, round):
    for match in list_of_matches:
        if match.h_team == team:
            if match.round_num == str(round):
                return match.h_team + " " + match.h_goals + " - " + match.a_goals + " " + match.a_team
        elif match.a_team == team:
            if match.round_num == str(round):
                return match.h_team + " " + match.h_goals + " - " + match.a_goals + " " + match.a_team



# for row in reader:
#     list_of_matches.append(Match(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

# for match in list_of_matches:
#     if match.round_num == '1':
#         match.print_values()
#         print("\n")

# calc_points_for_game(list_of_matches, table)


#------------------------------------------------------------------------
class Nasza(wnd, cls):

    list_of_matches = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def on_pushButton_openFile_pressed(self):
        f_name = QFileDialog.getOpenFileName(self, 'Open file')
        self.label_fileName.setText(f_name[0])
        file = open(f_name[0], 'r')
        reader = csv.reader(file)

        for row in reader:
            self.list_of_matches.append(Match(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

        calc_points_for_game(self.list_of_matches, table)
        self.textBrowser_table.setText(str(table))
        self.spinBox_RoundNumber.setMaximum(38)
        for team in table:
            self.comboBox_roundTeam.addItem(team)

    def on_comboBox_roundTeam_activated(self):
        self.spinBox_RoundNumber.setValue(0)

    def on_spinBox_RoundNumber_valueChanged(self):
        self.lineEdit_roundResult.setText(find_game(self.list_of_matches, self.comboBox_roundTeam.currentText(), self.spinBox_RoundNumber.value()))





a = QApplication([])
o = Nasza()
o.show()
a.exec()
