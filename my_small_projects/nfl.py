"""Add code that reads the data from nfl.csv and stores it in the new property self.nfl property within the __init__ method.
Alter the code in the count_total_wins method so that it uses the self.nfl property instead of the nfl variable (which no longer exists).
Use this instance method to assign the number of wins by the "Jacksonville Jaguars" to jaguars_wins."""



import csv
class Team():
    def __init__(self, name):
        self.name = name
        f = open('nfl.csv','r')
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count

jaguars = Team('Jacksonville Jaguars')
jaguars_wins = jaguars.count_total_wins()
