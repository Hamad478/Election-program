""""
import csv
mpList = []

class MP:
    def__int__(self,name.conName,pName):
    self.name = name
    self.descraption={'name':self.name,'constituency':conName,'party':pName}
    def Getname(self):
        return self.name
    def_str_(self):
    data = self.descraption['name'] + 'MP for' + self.descraption['constituency']
    return data

def readthefile(filename)
    with open(filename,newline='') as csvfile:
        reader =csv.DictReader('EditedData.csv')
        for row in reader:
            mpName = row['Member first name'] + '' + row['Member surname']
            con = row['constituency name']
            party = row['First party']
            thisMP = MP(mpName,con,party)
            mpList.append(thisMP)
    csvfile.close()

readthefile('EditedData.csv')
for mp in mpList:
    print(mp)
"""""

import csv

# List to store MP objects
mpList = []


# Define the MP class
class MP:
    def __init__(self, name, conName, pName):
        self.name = name
        self.description = {'name': self.name, 'constituency': conName, 'party': pName,'votes':0 }

    def Getname(self):
        return self.name

    def __str__(self):
        data = f"{self.description['name']} MP for {self.description['constituency']} ({self.description['party']})"
        return data
    def addvotes(self,v):
        self.description['votes'] = v
    def getvotes(self):
        return self.description['votes']

def readthefile(filename):
        with open(filename, newline='', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    mpName = row['Member first name'] + ' ' + row['Member surname']  # Include space between names
                    con = row['Constituency name']
                    party = row['First party']
                    thisMP = MP(mpName, con, party)  # Create an MP object

                    # Helper function to parse vote numbers safely
                    def parse_votes(vote_str):
                        return int(vote_str.replace(',', '').strip()) if vote_str else 0

                    # Add votes based on the party condition
                    if party == "Ind" or party == "spk":
                        thisMP.addvotes(parse_votes(row.get('of which other winner', '0')))
                    else:
                        thisMP.addvotes(parse_votes(row.get(party, '0')))

                    # Append MP object to the list
                    mpList.append(thisMP)
                except KeyError as e:
                    print(f"Missing data in row: {e}")
                except ValueError as e:
                    print(f"Invalid data format in row: {e}")


# Function to read the file and populate MP objects



# Read the file and print the MPs
readthefile('EditedData.csv')
for mp in mpList:
    print(mp)
    print("votes were",mp.getvotes())




