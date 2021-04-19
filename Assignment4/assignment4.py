# import mysql.connector
from faker import Faker
import csv
from datetime import date
import random

# db = mysql.connector.connect(
#     host="34.94.182.22",
#     user="myappuser",
#     passwd="barfoo",
#     database="Students"
# )

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

# import data


print("1. clients")
print("2. pets")
print("3. shelters")
print("4. employees")
user_file = input("Which file do you want to create? ")
while user_file not in ["1","2","3","4"]:
    user_file = input("Which file do you want to create? ")
user_file = int(user_file)
user_count = input("How many records do you want to generate? ")
while not user_count.isdigit():
    user_count = input("How many records do you want to generate? ")
user_count = int(user_count)