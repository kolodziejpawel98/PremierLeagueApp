import csv
file = open('sezon20202021.csv', 'r')

reader = csv.reader(file)

# for row in reader:
#     print(row[0])

# next(reader)
# row1 = next(reader)
# print(row1)

class Match:
    def __init__(self, match_num, round_num, date, location, h_team, a_team, result):
        self.match_num = match_num
        self.round_num = round_num
        self.date = date
        self.location = location
        self.h_team = h_team
        self.a_team = a_team
        self.result = result

    def print_values(self):
        print("Match number: " + self.match_num)
        print("Round number: " + self.round_num)
        print("Date: " + self.date)
        print("Location: " + self.location)
        print("Home team: " + self.h_team)
        print("Away team: " + self.a_team)
        print("Result: " + self.result)

# match1 = Match(row1[0], row1[1], row1[2], row1[3], row1[4], row1[5], row1[6])
# match1.print_values()

list_of_matches = []

for row in reader:
    list_of_matches.append(Match(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

list_of_matches[1].print_values()
# interestingrows=[row for idx, row in enumerate(reader) if idx == 1]
# print(interestingrows)


# list_of_matches.append(Match(row1[0], row1[1], row1[2], row1[3], row1[4], row1[5], row1[6]))
# row1 = next(reader)
# list_of_matches.append(Match(row1[0], row1[1], row1[2], row1[3], row1[4], row1[5], row1[6]))
# row1 = next(reader)
# list_of_matches.append(Match(row1[0], row1[1], row1[2], row1[3], row1[4], row1[5], row1[6]))
#
# pom = 1
#
# for obj in list_of_matches:
#     print(pom)
#     obj.print_values()
#     pom = pom + 1
#     print("\n")
