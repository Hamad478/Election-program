import csv

# List to store MP objects
mpList = []
partyList = {}

# Define the MP class
class MP:
    def __init__(self, name, conName, pName):
        self.name = name
        self.description = {'name': self.name, 'constituency': conName, 'party': pName, 'votes': 0}
        self.is_new = False  # Flag to indicate if the MP is new

    def addvotes(self, v):
        self.description['votes'] = v

    def getvotes(self):
        return self.description['votes']

    def __str__(self):
        return f"{self.description['name']} MP for {self.description['constituency']} ({self.description['party']})"


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
        if mp.is_new:
            self.new_mps += 1

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


# Function to read MPs from the CSV file
def read_mps(filename):
    with open(filename, newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                mpName = row['Member first name'] + ' ' + row['Member surname']
                con = row['Constituency name']
                party = row['First party']
                theMP = MP(mpName, con, party)

                # Helper function to parse vote numbers safely
                def parse_votes(vote_str):
                    return int(vote_str.replace(',', '').strip()) if vote_str else 0

                # Add votes based on the party condition
                if party in ["Ind", "spk"]:
                    theMP.addvotes(parse_votes(row.get('Of which other winner', '0')))
                else:
                    theMP.addvotes(parse_votes(row.get(party, '0')))

                # Check if the MP is new based on the Result column
                result = row.get('Result', '')
                theMP.is_new = 'gain' in result

                # Append MP object to the list
                mpList.append(theMP)

                # Update party information
                if party not in partyList:
                    partyList[party] = Party(party)
                partyList[party].add_mp(theMP)

            except KeyError as e:
                print(f"Missing data in row: {e}")
            except ValueError as e:
                print(f"Invalid data format in row: {e}")


# List to store Constituency objects
constituencyList = []

# Define the Constituency class
class Constituency:
    def __init__(self, name, region, country, ctype, electorate):
        self.cName = name
        self.cRegion = region
        self.cCountry = country
        self.cType = ctype
        self.cElectorate = electorate
        self.description = {
            'Country name': self.cCountry,
            'Region name': self.cRegion,
            'Constituency type': self.cType,
            'Electorate': self.cElectorate,
 }

    def __str__(self):
        return self.cName

    def GetDescription(self):
        return self.description


# Function to read Constituencies from the CSV file
def read_constituencies(filename):
    with open(filename, newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                name = row['Constituency name']
                region = row['Region name']
                country = row['Country name']
                ctype = row['Constituency type']
                electorate = row['Electorate']
                constituency = Constituency(name, region, country, ctype, electorate)
                constituencyList.append(constituency)
            except KeyError as e:
                print(f"Missing data in row: {e}")
            except Exception as e:
                print(f"Error processing row: {e}")


# Function to display the menu and handle user input
def display_menu():
    while True:
        print("\nMenu:")
        print("1. Candidate party")
        print("2. Constituency’s mp  ")
        print("3. Parliamentary Seat details  ")
        print("4. Total registered voters in the seat")
        print("5. Total of votes cast")
        print("6. Votes cast for the candidate")
        print("7. Votes for a given party received as a percentage of total votes cast")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            candidate_name = input("Enter candidate name: ")
            for mp in mpList:
                if mp.name.lower() == candidate_name.lower():
                    print(f"Candidate Party: {mp.description['party']}")
                    break
            else:
                print("Candidate not found.")

        elif choice == '2':
            candidate_name = input("Enter candidate name: ")
            for mp in mpList:
                if mp.name.lower() == candidate_name.lower():
                    print(f"Candidate Name: {mp.name} mp for {mp.description['constituency']} " )
                    break
            else:
                print("Candidate not found.")

        elif choice == '3':
            constituency_name = input("Enter parliamentary seat name: ")
            for constituency in constituencyList:
                if constituency.cName.lower() == constituency_name.lower():
                    print(f"Parliamentary Seat: {constituency.cName} Country:{constituency.cCountry} Region:{constituency.cRegion} constituency type:{constituency.cType}")
                    break
            else:
                print("Constituency not found.")

        elif choice == '4':
            constituency_name = input("Enter parliamentary seat name: ")
            for constituency in constituencyList:
                if constituency.cName.lower() == constituency_name.lower():
                    print(f"Total registered voters in the seat: {constituency.cElectorate}")
                    break
            else:
                print("Constituency not found.Make sure a"
                      "you added the constituency")

        elif choice == '5':
            total_votes = sum(mp.getvotes() for mp in mpList)
            print(f"Total votes cast: {total_votes}")

        elif choice == '6':
            candidate_name = input("Enter candidate name: ")
            for mp in mpList:
                if mp.name.lower() == candidate_name.lower():
                    print(f"Votes cast for {mp.name}: {mp.getvotes()}")
                    break
            else:
                print("Candidate not found.")

        elif choice == '7':
            party_name = input("Enter party name: ")
            total_votes = sum(mp.getvotes() for mp in mpList)
            party_votes = sum(mp.getvotes() for mp in mpList if mp.description['party'].lower() == party_name.lower())
            if total_votes > 0:
                percentage = (party_votes / total_votes) * 100
                print(f"Votes for {party_name} received as a percentage of total votes cast: {percentage:.2f}%")
            else:
                print(" there is no party in this name.")


        elif choice == '8':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


# Read the files
read_mps('EditedData.csv')
read_constituencies('EditedData.csv')
display_menu()

#StephenKinnock
#Aberafan Maesteg
