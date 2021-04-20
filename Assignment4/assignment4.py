# import mysql.connector
from faker import Faker
import csv
from datetime import date
import random
from random import randrange

# db = mysql.connector.connect(
#     host="34.94.182.22",
#     user="myappuser",
#     passwd="barfoo",
#     database="Students"
# )

# GENERATE FAKE DATA
fake = Faker()

states = ['CA', 'OR', 'WA']
preferences = ['cat','dog']
phases = ['fostering','adopting']
genders = ['female','male']

# generate clients data
def genClients(num: int):
    csv_file = open("./clients.csv", "w")
    writer = csv.writer(csv_file)
    writer.writerow(["FirstName","LastName","DOB","Phone","Email",
                     "Address","City","State","Zip",
                     "Occupation","Preference","Phase",
                     "Approved?","Update"])
    for x in range(0, num):
        writer.writerow(fake.first_name(),
                        fake.last_name(),
                        fake.date_between_dates(date_start=date(1970, 1, 1), date_end=date(2004, 1, 1)),
                        fake.numerify('###-###-####'),
                        fake.email(),
                        fake.street_address(),
                        fake.city(),
                        random.choice(states),
                        fake.pyint(min_value=90000, max_value=99500),
                        fake.job(),
                        random.choice(preferences),
                        random.choice(phases),
                        fake.boolean(),
                        fake.date_between_dates(date_start=date(2000, 1, 1), date_end=date(2004, 1, 1)))

# generate pets data
def genPets(num: int):
    csv_file = open("./pets.csv", "w")
    writer = csv.writer(csv_file)
    writer.writerow(["Name","DOB", "Gender"
                     "Type","HealthConcerns",
                     "Phase"])
    for x in range(0, num):
        writer.writerow(fake.first_name(),
                        fake.date_between_dates(date_start=date(1991, 1, 1), date_end=date(2021, 1, 1)),
                        random.choice(genders),
                        random.choice(preferences),
                        fake.boolean(),
                        random.choice(phases))

# generate shelters data
def genShelters(num: int):
    csv_file = open("./shelters.csv", "w")
    writer = csv.writer(csv_file)
    writer.writerow(["Phone","Email",
                     "Address","City","State","Zip"])
    for x in range(0, num):
        writer.writerow(fake.numerify('###-###-####'),
                        fake.last_name().lower()+"@pawsibleshelters.com",
                        fake.street_address(),
                        fake.city(),
                        random.choice(states),
                        fake.pyint(min_value=90000, max_value=99500))

# generate employees data
def genEmployees(num: int):
    csv_file = open("./employees.csv", "w")
    writer = csv.writer(csv_file)
    writer.writerow(["FirstName","LastName","DOB","Phone","Email",
                     "Address","City","State","Zip"])
    for x in range(0, num):
        writer.writerow(fake.first_name(),
                        fake.last_name(),
                        fake.date_between_dates(date_start=date(1970, 1, 1), date_end=date(2004, 1, 1)),
                        fake.numerify('###-###-####'),
                        fake.email(),
                        fake.street_address(),
                        fake.city(),
                        random.choice(states),
                        fake.pyint(min_value=90000, max_value=99500))

# IMPORT DATA
def importDatạ():
    mycursor = db.cursor()
    # fill Clients table
    with open("./clients.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print("importing clients")
            mycursor.execute("INSERT INTO Clients(FirstName, LastName, DateOfBirth, Phone, Email, "
                             "Address, City, State, Zip,"
                             "Occupation, Preference, Phase,"
                             "Status, StatusDate)"
                             "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
                             (row["FirstName"], row["LastName"], row["DOB"], row["Phone"], row["Email"],
                              row["Address"], row["City"], row["State"], row["Zip"],
                              row["Occupation"], row["Preference"], row["Phase"],
                              row["Approved?"], row["Update"]))
            db.commit()
            clientCount = mycursor.lastrowid
    # fill Pets table
    with open("./pets.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print("importing pets")
            mycursor.execute("INSERT INTO Pets(Name, DateOfBirth, Gender,"
                             "Type, HealthConcerns, Phase)"
                             "VALUES (%s,%s,%s,%s,%s,%s);",
                             (row["Name"], row["DOB"], row["Gender"],
                              row["Type"], row["HealthConcerns"], row["Phase"]))
            db.commit()
            petCount = mycursor.lastrowid
    # fill Shelters table
    with open("./shelters.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print("importing shelters")
            mycursor.execute("INSERT INTO Shelters(Phone, Email, "
                             "Address, City, State, Zip)"
                             "VALUES (%s,%s,%s,%s,%s,%s);",
                             (row["Phone"], row["Email"],
                              row["Address"], row["City"], row["State"], row["Zip"]))
            db.commit()
            shelterCount = mycursor.lastrowid
    # fill Employees table
    with open("./employees.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print("importing employees")
            mycursor.execute("INSERT INTO Employees(FirstName, LastName, DateOfBirth, Phone, Email, "
                             "Address, City, State, Zip)"
                             "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);",
                             (row["FirstName"], row["LastName"], row["DOB"], row["Phone"], row["Email"],
                              row["Address"], row["City"], row["State"], row["Zip"]))
            db.commit()
            employeeCount = mycursor.lastrowid
    # fill ClientToEmployee table
    for i in range(clientCount+1):
        mycursor.execute("INSERT INTO ClientToEmployee(ClientID,EmployeeID)"
                        "VALUES (%s,%s);",
                        (i, randrange(1, employeeCount)))
        db.commit()
    # fill PetToShelter table
    for i in range(petCount+1):
        mycursor.execute("INSERT INTO PetToShelter(petID,shelterID)"
                        "VALUES (%s,%s);",
                        (i, randrange(1, shelterCount)))
        db.commit()
    # fill EmployeeToShelter table
    for i in range(employeeCount+1):
        mycursor.execute("INSERT INTO EmployeeToShelter(employeeID,shelterID)"
                        "VALUES (%s,%s);",
                        (i, randrange(1, shelterCount)))
        db.commit()


# USER INPUT

# which file to write
print("1. clients")
print("2. pets")
print("3. shelters")
print("4. employees")
user_file = input("Which file do you want to create? ")
while user_file not in ["1","2","3","4"]:
    user_file = input("Which file do you want to create? ")
user_file = int(user_file)

# how many records to create
user_count = input("How many records do you want to generate? ")
while not user_count.isdigit():
    user_count = input("How many records do you want to generate? ")
user_count = int(user_count)

if user_file == 1:
    genClients(user_count)
elif user_file == 2:
    genPets(user_count)
elif user_file == 3:
    if user_count > 1000:
        print("There can't be more than 1,000 shelters")
        user_count = input("How many records do you want to generate? ")
        while not user_count.isdigit():
            user_count = input("How many records do you want to generate? ")
        user_count = int(user_count)
    genShelters(user_count)
elif user_file == 4:
    genEmployees(user_count)

print("Have you generated data for all four tables yet?")
user_input = input("Y/N").upper()
if user_input == "Y":
    print("Are you sure that you have a clients.csv, pets.csv, shelters.csv, and employees.csv?")
    user_input = input("Y/N").upper()
    if user_input == "Y":
        print("Would you like to import the data into the database tables?")
        user_input = input("Y/N").upper()
        if user_input == "Y":
            print("Importing data...")
            importDatạ()
        else:
            print("You have chosen to not import data at this time.")
            exit()
    else:
        print("Please generate data for all four tables.")
        exit()
else:
    print("Please generate data for all four tables.")
    exit()