import csv

# List to store Constituency objects
Constituencylist = []

class Constituency:
    def __init__(self, name, region, country, ctype,electorate):
        self.cName = name
        self.cRegion = region
        self.cCountry = country
        self.cType = ctype
        self.cElectorate = electorate
        self.description = {
            'Country name': self.cCountry,
            'Region name': self.cRegion,
            'Constituency type': self.cType,
            'Electorate':self.cElectorate
        }

    def __str__(self):
        return self.cName

    def GetDescription(self):
        return self.description


# Function to read the file and populate Constituency objects
def readthefile(filename):
    with open(filename, newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                name = row['Country name']  # Extract country name
                region = row['Region name']  # Extract region name
                country = row['Country name']  # Country name again for clarity
                ctype = row['Constituency type']  # Constituency type
                electorate = row['Electorate']
                # Create a Constituency object
                constituency = Constituency(name, region, country, ctype,electorate)
                # Append it to the list
                Constituencylist.append(constituency)
            except KeyError as e:
                print(f"Missing data in row: {e}")
            except Exception as e:
                print(f"Error processing row: {e}")

# Read the file and print the Constituencies
readthefile('EditedData.csv')
for constituency in Constituencylist:
    print(constituency)
    print("Description:", constituency.GetDescription())



