Use Case	Test	Expected result 	Actual result 
. Candidate party
	User input (StephenKinnock)
	Lab 	Lab 
Candidate party	User input (yassir)	Candidate not found
	Candidate not found

Constituency’s mp
	User input (Aberafan Maesteg)
	StephenKinnock	StephenKinnock
Constituency’s mp
	User input(hfh)	Candidate not found
	Candidate not found

"Enter parliamentary seat name:
	User input(Aberafan Maesteg)
	Aberafan Maesteg Country:Wales Region:Wales constituency type:County	Aberafan Maesteg Country:Wales Region:Wales constituency type:County
Enter parliamentary seat name:
	User input(ruuu)	Constituency not found.	Constituency not found.
Enter parliamentary seat name
	User input (Aberafan Maesteg)
	Total registered voters in the seat: 72,580	Total registered voters in the seat: 72,580
 
Use Case	Test	Expected result 	Actual result 
Enter parliamentary seat name
	User input(eee)	Constituency not found.Make sure ayou added the constituency	Constituency not found.Make sure ayou added the constituency
Total of votes cast"
		Total votes cast: 12126972	Total votes cast: 12126972
Votes cast for the candidate"
	User input(Stephen Kinnock	Votes cast for Stephen Kinnock: 17838	Votes cast for Stephen Kinnock: 17838
Votes cast for the candidate	User input (yyy)	mp not found.	mp not found.
Votes for a given party received as a percentage of total votes cast	User input (Lab)	Votes for lab received as a percentage of total votes cast: 62.65%	Votes for lab received as a percentage of total votes cast: 62.65%
Votes for a given party received as a percentage of total votes cast	User input(df)	there is no party in this name.")
	Votes for df received as a percentage of total votes cast: 0.00%
 
Class MP	Crate object 	Successful 	
Class party 	Crate object	Successful	
Class Constituency	Crate object	Successful	


simple and useful program.  

Crtaqe:
The progam porvids limted optine
The program does not provide all data 
The program could have provided more sophisticated options 
The program can provide a  
 




About the program:
This is a program designed to help users get the information they want from the election data. It uses three classes: MP class, party class and Constituency class. It has a simple and straightforward menu that provides the user with eight options: Candidate party Constituency’s MP Parliamentary Seat details, Total registered voters in the seat, Total of votes cast, Votes cast for the candidate and Votes for a given party received as a percentage of total votes cast. It is a simple and useful program.  
C:
The progam porvids limted optine
The program does not provide all data 
The program could have provided more sophisticated options 
The program can provide a more developed user interface   

START

// Initialize lists for MPs and parties
mpList = []
partyList = {}

// Define MP class
CLASS MP
    FUNCTION __init__(name, conName, pName)
        SET self.name = name
        SET self.description = {'name': name, 'constituency': conName, 'party': pName, 'votes': 0}
        SET self.is_new = False

    FUNCTION addvotes(v)
        SET self.description['votes'] = v

    FUNCTION getvotes()
        RETURN self.description['votes']

    FUNCTION __str__()
        RETURN self.description['name'] + " MP for " + self.description['constituency'] + " (" + self.description['party'] + ")"

// Define Party class
CLASS Party
    FUNCTION __init__(name)
        SET self.name = name
        SET self.total_mps = 0
        SET self.total_votes = 0
        SET self.new_mps = 0

    FUNCTION add_mp(mp)
        INCREMENT self.total_mps
        INCREMENT self.total_votes by mp.getvotes()
        IF mp.is_new THEN
            INCREMENT self.new_mps

    FUNCTION proportion_new()
        RETURN self.new_mps / self.total_mps IF self.total_mps > 0 ELSE 0

    FUNCTION proportion_of_votes()
        total_votes_all_parties = SUM(party.total_votes FOR party IN partyList)
        RETURN self.total_votes / total_votes_all_parties IF total_votes_all_parties > 0 ELSE 0

    FUNCTION __str__()
        RETURN "Party: " + self.name + ", Total MPs: " + self.total_mps + ", Proportion New: " + self.proportion_new() + ", Total Votes: " + self.total_votes + ", Proportion of Votes: " + self.proportion_of_votes()

// Function to read MPs from CSV file
FUNCTION read_mps(filename)
    OPEN filename AS csvfile
    reader = CSV.DictReader(csvfile)
    FOR row IN reader
        TRY
            mpName = row['Member first name'] + ' ' + row['Member surname']
            con = row['Constituency name']
            party = row['First party']
            theMP = MP(mpName, con, party)

            FUNCTION parse_votes(vote_str)
                RETURN INT(vote_str.replace(',', '').strip()) IF vote_str ELSE 0

            IF party IN ["Ind", "spk"] THEN
                theMP.addvotes(parse_votes(row.get('Of which other winner', '0')))
            ELSE
                theMP.addvotes(parse_votes(row.get(party, '0')))

            result = row.get('Result', '')
            theMP.is_new = 'gain' IN result

            APPEND theMP TO mpList

            IF party NOT IN partyList THEN
                partyList[party] = Party(party)
            partyList[party].add_mp(theMP)

        EXCEPT KeyError AS e
            PRINT "Missing data in row: " + e
        EXCEPT ValueError AS e
            PRINT "Invalid data format in row: " + e

// Define Constituency class
CLASS Constituency
    FUNCTION __init__(name, region, country, ctype, electorate)
        SET self.cName = name
        SET self.cRegion = region
        SET self.cCountry = country
        SET self.cType = ctype
        SET self.cElectorate = electorate
        self.description = {'Country name': self.cCountry, 'Region name': self.cRegion, 'Constituency type': self.cType, 'Electorate': self.cElectorate}

    FUNCTION __str__()
        RETURN self.cName

    FUNCTION GetDescription()
        RETURN self.description

// Function to read Constituencies from CSV file
FUNCTION read_constituencies(filename)
    OPEN filename AS csvfile
    reader = CSV.DictReader(csvfile)
    FOR row IN reader
        TRY
            name = row['Constituency name']
            region = row['Region name']
            country = row['Country name']
            ctype = row['Constituency type']
            electorate = row['Electorate']
            constituency = Constituency(name, region, country, ctype, electorate)
            APPEND constituency TO constituencyList

        EXCEPT KeyError AS e
            PRINT "Missing data in row: " + e
        EXCEPT Exception AS e
            PRINT "Error processing row: " + e

// Function to display the menu and handle user input
FUNCTION display_menu()
    WHILE True
        PRINT "\nMenu:"
        PRINT "1. Candidate party"
        PRINT "2. Constituency’s mp"
        PRINT "3. Parliamentary information"
        PRINT "4. Exit"
        choice = INPUT("Select an option: ")

        IF choice == "1" THEN
            DISPLAY partyList
        ELSE IF choice == "2" THEN
            constituency_name = INPUT("Enter constituency name: ")
            DISPLAY MPs in constituency_name
        ELSE IF choice == "3" THEN
            DISPLAY all parliamentary information
        ELSE IF choice == "4" THEN
            PRINT "Exiting..."
            BREAK
        ELSE
            PRINT "Invalid option, please try again."

// Main execution
FUNCTION main()
    read_mps("mps_data.csv")
    read_constituencies("constituencies_data.csv")
    display_menu()

END FUNCTION

main()
 
