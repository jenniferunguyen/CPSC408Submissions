import sqlite3, re, string

conn = sqlite3.connect('./assignment3.sqlite')
mycursor = conn.cursor()

# # import data from csv
# with open('./students.csv') as inputfile:
#     columns = inputfile.readline()
#     data = inputfile.readlines()
#
# columns = columns.strip().split(',')
#
# name_dictionary = {}
# for i in range(len(columns)):
#     name_dictionary[i] = columns[i]
#
# records = []
# for i in data[:]:
#     i = i.strip().split(",")
#     records.append(i)
#
# conn.executemany("INSERT INTO StudentDB(FirstName,LastName,Address,City,State,ZipCode,MobilePhoneNumber,Major,GPA)"
#                  "VALUES(?,?,?,?,?,?,?,?,?)", records)
# conn.commit()

def option1():
    query = '''
    SELECT *
    FROM StudentDB;
    '''
    mycursor = conn.execute(query)
    for row in mycursor:
        if row[11] != 1:
            print("Student ID: ", row[0])
            print("Name: ", row[1], row[2])
            print("GPA: ", row[3])
            print("Major: ", row[4])
            print("Faculty Advisor: ", row[5])
            print("Address: ", row[6], ",", row[7], ",", row[8], row[9])
            print("Mobile Phone Numbmer: ", row[10])
            print("\n")

def option2():
    entry = [None] * 10
    entry[0] = string.capwords(input("Enter first name: "))
    entry[1] = string.capwords(input("Enter last name: "))
    entry[2] = string.capwords(input("Enter street address: "))
    entry[3] = string.capwords(input("Enter city: "))
    entry[4] = string.capwords(input("Enter state: "))
    entry[5] = input("Enter zip code: ")
    # check zip code is valid
    zipPattern = "^\d{5}$"
    isZip = re.match(zipPattern, entry[5])
    while not isZip:
        entry[5] = input("Enter 5-digit zip code: ")
        isZip = re.match(zipPattern, entry[5])
    entry[6] = input("Enter mobile phone number: ")
    entry[7] = string.capwords(input("Enter major: "))
    entry[9] = input("Enter faculty advisor: ") # forgot about this field :)
    entry[8] = input("Enter GPA, round to one decimal: ")
    # check gpa is valid
    gpaPattern = "^\d{1}.\d{1}$"
    isGPA = re.match(gpaPattern, entry[8])
    while not isGPA:
        entry[8] = input("Enter a valid GPA: ")
        isGPA = re.match(gpaPattern, entry[8])
    query = '''
    INSERT INTO StudentDB(FirstName,LastName,Address,City,State,ZipCode,MobilePhoneNumber,Major,GPA,FacultyAdvisor)
    VALUES (?,?,?,?,?,?,?,?,?,?);
    '''
    mycursor = conn.execute(query,entry)
    print("\n")

def option3():
    id = (input("Enter student id: "))
    # check valid numeric student id
    while not id.isdigit():
        id = (input("Enter student id (numeric only): "))
    id = int(id)
    print("Choose an option:")
    print("Enter 1 to edit major.")
    print("Enter 2 to edit faculty advisor.")
    print("Enter 3 to edit mobile number.")
    user_choice = (input("Enter option here: "))
    # check that user input is part of options of actions
    while user_choice not in ["1","2","3"]:
        user_choice = input("Enter valid option here: ")
    user_choice = int(user_choice)
    if user_choice == 1:
        value = string.capwords(input("Enter major: "))
        query = '''
            UPDATE StudentDB
            SET Major = (?)
            WHERE StudentID = (?);
            '''
    elif user_choice == 2:
        value = input("Enter faculty advisor: ")
        query = '''
            UPDATE StudentDB
            SET FacultyAdvisor = (?)
            WHERE StudentID = (?);
            '''
    elif user_choice == 3:
        value = input("Enter mobile phone number: ")
        query = '''
            UPDATE StudentDB
            SET MobilePhoneNumber = (?)
            WHERE StudentID = (?);
            '''
    mycursor = conn.execute(query,(value,id,))
    print("\n")

def option4():
    entry = input("Enter student id: ")
    # check valid numeric student id
    while not entry.isdigit():
        entry = input("Enter student id (numeric only): ")
    entry = int(entry)
    query = '''
    UPDATE StudentDB
    SET isDeleted = 1
    WHERE StudentID = (?);
    '''
    mycursor = conn.execute(query,(entry,))
    print("\n")

def option5():
    print("Choose an option:")
    print("Enter 1 to search by major.")
    print("Enter 2 to search by GPA.")
    print("Enter 3 to search by city.")
    print("Enter 4 to search by state.")
    print("Enter 5 to search by advisor.")
    user_choice = (input("Enter option here: "))
    # check that user input is part of options of actions
    while user_choice not in ["1", "2", "3","4","5"]:
        user_choice = input("Enter valid option here: ")
    user_choice = int(user_choice)
    if user_choice == 1:
        value = string.capwords(input("Enter major: "))
        query = '''
                SELECT *
                FROM StudentDB
                WHERE Major = (?);
                '''
    elif user_choice == 2:
        value = input("Enter GPA, round to one decimal: ")
        # check gpa is valid
        gpaPattern = "^\d{1}.\d{1}$"
        isGPA = re.match(gpaPattern, value)
        while not isGPA:
            value = input("Enter a valid GPA: ")
            isGPA = re.match(gpaPattern, value)
        query = '''
                        SELECT *
                        FROM StudentDB
                        WHERE GPA = (?);
                        '''
    elif user_choice == 3:
        value = string.capwords(input("Enter city: "))
        query = '''
                        SELECT *
                        FROM StudentDB
                        WHERE City = (?);
                        '''
    elif user_choice == 4:
        value = string.capwords(input("Enter state: "))
        query = '''
                        SELECT *
                        FROM StudentDB
                        WHERE State = (?);
                        '''
    elif user_choice == 5:
        value = string.capwords(input("Enter faculty advisor: "))
        query = '''
                        SELECT *
                        FROM StudentDB
                        WHERE FacultyAdvisor = (?);
                        '''
    mycursor = conn.execute(query,(value,))
    print("\n")
    for row in mycursor:
        if row[11] != 1:
            print("Student ID: ", row[0])
            print("Name: ", row[1], row[2])
            print("GPA: ", row[3])
            print("Major: ", row[4])
            print("Faculty Advisor: ", row[5])
            print("Address: ", row[6], ",", row[7], ",", row[8], row[9])
            print("Mobile Phone Numbmer: ", row[10])
            print("\n")


exit = False

while not exit:
    # user options
    print("Choose an option:")
    print("Enter 1 to view all students.")
    print("Enter 2 to add a student.")
    print("Enter 3 to update a student's information.")
    print("Enter 4 to delete a student.")
    print("Enter 5 to search students.")
    print("Enter 6 to EXIT.")
    user_choice = input("Enter option here: ")
    # check valid option chosen
    while user_choice not in ["1","2","3","4","5","6"]:
        user_choice = input("Enter valid option here: ")
    user_choice = int(user_choice)
    print("\n")

    if user_choice == 1:
        option1()
    elif user_choice == 2:
        option2()
    elif user_choice == 3:
        option3()
    elif user_choice == 4:
        option4()
    elif user_choice == 5:
        option5()
    elif user_choice == 6:
        exit = True
        print("Goodbye!")

conn.close()
