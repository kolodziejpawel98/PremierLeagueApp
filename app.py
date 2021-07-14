import csv
file = open('sezon20202021.csv', 'r')

reader = csv.reader(file)

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

for row in reader:
    list_of_matches.append(Match(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

for match in list_of_matches:
    if match.round_num == '1':
        match.print_values()
        print("\n")
