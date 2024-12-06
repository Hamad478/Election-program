"""""
import csv
file = open("EditedData.csv","rb")
print(file.readlines())
file.close()
"""


""""
def readthefile(filename):
    with open(filename, newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            mpName = row['Member first name'] + ' ' + row['Member surname']  # Include space between names
            con = row['Constituency name']
            party = row['First party']
            thisMP = MP(mpName, con, party)  # Create an MP object
            mpList.append(thisMP)
            if party =="Ind" or party == "spk":
                thisMP.addvotes(int(row['of which other winner']))
            else:
                thisMP.addvotes(int(row[party]))
                mpList.append(thisMP)
   csvfile.close()
"""
import csv

# List to store MP objects
mpList = []
partyList = {}

# Define the MP class
class MP:
    def __init__(self, name, conName, pName):
        self.name = name
        self.description = {'name': self.name, 'constituency': conName, 'party': pName, 'votes': 0}


    def addvotes(self, v):
        self.description['votes'] = v

    def getvotes(self):
        return self.description['votes']


# Define the Party class
class Party:
    def __init__(self, name):
        self.name = name
        self.total_mps = 0
        self.total_votes = 0
        self.new_mps = 0

    def add_mp(self, mp):
        self.total_mps += 1
        self.total_votes += mp.getvotes()


    def proportion_new(self):
        return self.new_mps / self.total_mps if self.total_mps > 0 else 0

    def proportion_of_votes(self):
        total_votes_all_parties = sum(party.total_votes for party in partyList.values())
        return self.total_votes / total_votes_all_parties if total_votes_all_parties > 0 else 0

    def __str__(self):
        return (f"Party: {self.name}, Total MPs: {self.total_mps}, "
                f"Proportion New: {self.proportion_new():.2%}, "
                f"Total Votes: {self.total_votes}, "
                f"Proportion of Votes: {self.proportion_of_votes():.2%}")


def readthefile(filename):
    with open(filename, newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            try:
                # Construct the MP name from first and surname
                mpName = row['Member first name'] + ' ' + row['Member surname']
                con = row['Constituency name']
                party = row['First party']
                thisMP = MP(mpName, con, party)  # Create an MP object

                # Helper function to parse vote numbers safely
                def parse_votes(vote_str):
                    return int(vote_str.replace(',', '').strip()) if vote_str else 0

                # Add votes based on the party condition
                if party in ["Ind", "spk"]:
                    thisMP.addvotes(parse_votes(row.get('Of which other winner', '0')))
                else:
                    thisMP.addvotes(parse_votes(row.get(party, '0')))

                # Check if the MP is new based on the Result column
                result = row.get('Result', '')
                thisMP.is_new = 'gain' in result  # Check if 'gain' is in the Result string

                # Debugging output to check if the MP is new
                print(f"MP: {thisMP.name}, Is New: {thisMP.is_new}")

                # Append MP object to the list
                mpList.append(thisMP)

                # Update party information
                if party not in partyList:
                    partyList[party] = Party(party)
                partyList[party].add_mp(thisMP)

            except KeyError as e:
                print(f"Missing data in row: {row}, Error: {e}")
            except ValueError as e:
                print(f"Invalid data format in row: {row}, Error: {e}")

# Read the file
readthefile('EditedData.csv')

# Print party summaries only
for party in partyList.values():
    print(party)