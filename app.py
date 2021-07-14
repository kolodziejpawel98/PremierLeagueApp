from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog
import csv

cls, wnd = uic.loadUiType('app.ui')

class Nasza(wnd, cls):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def on_pushButton_openFile_pressed(self):
        f_name = QFileDialog.getOpenFileName(self, 'Open file')
        self.label_fileName.setText(f_name[0]) #zmienic ta sciezke do pliku !!!!!!!!!!!!!!!!!!!!!!
        calc_points_for_game(list_of_matches, table)
        self.textBrowser_table.setText(str(table))


file = open('sezon20202021.csv', 'r') #????????????????????????????? zmienic ta sciezke do pliku
reader = csv.reader(file)

table = { #zmienić to na klase table z polami team i points!!!!!!!!!!!!!!!!!! 
    "Sheffield Utd" : 0,
    "West Brom" : 0,
    "Fulham" : 0,
    "Burnley" : 0,
    "Brighton" : 0,
    "Southampton" : 0,
    "Crystal Palace" : 0,
    "Wolves" : 0,
    "Newcastle" : 0,
    "Aston Villa" : 0,
    "Everton" : 0,
    "Leeds" : 0,
    "Arsenal" : 0,
    "Spurs" : 0,
    "West Ham" : 0,
    "Leicester" : 0,
    "Chelsea" : 0,
    "Liverpool" : 0,
    "Man Utd" : 0,
    "Man City" : 0,
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


list_of_matches = []

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

for row in reader:
    list_of_matches.append(Match(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

# for match in list_of_matches:
#     if match.round_num == '1':
#         match.print_values()
#         print("\n")

# calc_points_for_game(list_of_matches, table)


#------------------------------------------------------------------------



a = QApplication([])
o = Nasza()
o.show()
a.exec()
