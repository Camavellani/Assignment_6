import sqlite3
from unittest import result
from unittest.util import strclass
from user import user
from student import student
from instructor import instructor
from admin import admin

database = sqlite3.connect("data.db")
cursor = database.cursor()
parameters = []
course_list = []
roster = []

# Creating tables
sql_command = """CREATE TABLE IF NOT EXISTS STUDENT (
    ID TEXT PRIMARY KEY NOT NULL,
    FIRST TEXT NOT NULL,
    LAST TEXT NOT NULL,
    YEAR INT NOT NULL,
    MAJOR TEXT NOT NULL,
    EMAIL TEXT NOT NULL);"""
cursor.execute(sql_command)
sql_command = """CREATE TABLE IF NOT EXISTS INSTRUCTOR (
    ID TEXT PRIMARY KEY NOT NULL,
    FIRST TEXT NOT NULL,
    LAST TEXT NOT NULL,
    TITLE TEXT NOT NULL,
    HIRE_YEAR INT NOT NULL,
    DEPARTMENT TEXT NOT NULL,
    EMAIL TEXT NOT NULL);"""
cursor.execute(sql_command)
sql_command = """CREATE TABLE IF NOT EXISTS ADMIN (
    ID TEXT PRIMARY KEY NOT NULL,
    FIRST TEXT NOT NULL,
    LAST TEXT NOT NULL,
    TITLE TEXT NOT NULL,
    OFFICE TEXT NOT NULL,
    EMAIL TEXT NOT NULL);"""
cursor.execute(sql_command)
sql_command = """CREATE TABLE IF NOT EXISTS COURSE (
    CRN TEXT PRIMARY KEY NOT NULL,
    TITLE TEXT NOT NULL,
    DEPARTMENT TEXT NOT NULL,
    TIME TEXT NOT NULL,
    DAYS TEXT NOT NULL,
    SEMESTER TEXT NOT NULL,
    YEAR INT NOT NULL,
    CREDITS INT NOT NULL);"""
cursor.execute(sql_command)
sql_command = """INSERT INTO STUDENT VALUES('000000', 'Andrew', 'Lee', 2023, 'BSCO', 'leea');"""
#cursor.execute(sql_command)
sql_command = """INSERT INTO COURSE VALUES('000000', 'Applied Programming Concepts', 'BSCO', '8:00AM-10:00AM', 'TR', 'Summer', 2022, 4);"""
#cursor.execute(sql_command)
sql_command = """INSERT INTO ADMIN VALUES('000000', 'George', 'Washington', 'President', 'Dobbs 140', 'washingtong');"""
#cursor.execute(sql_command)
sql_command = """INSERT INTO INSTRUCTOR VALUES('1', 'John', 'Hancock', 'Prof', '2000', 'BSCO', 'hancockj');"""
#cursor.execute(sql_command)

user_choice = int(input(f'Choose a user type\n1. Student\n2. Instructor\n3. Admin\n'))

# UI - enter credentials
first = input("Enter your first name: \n")
last = input("Enter your last name: \n")
id = input("Enter your ID number without the W: \n")
if(user_choice == 1):
    # Verify student credentials
    cursor.execute("""SELECT ID FROM STUDENT WHERE ID = ?""", (id,))
    query_result1 = cursor.fetchall()
    cursor.execute("""SELECT FIRST FROM STUDENT WHERE FIRST = ?""", (first,))
    query_result2 = cursor.fetchall()
    cursor.execute("""SELECT LAST FROM STUDENT WHERE LAST = ?""", (last,))
    query_result3 = cursor.fetchall()
    if(len(query_result1) == 0):
        result_id = "er404"
    else:
        result_id = id
    if(len(query_result2) == 0):
        result_first = "er404"
    else:
        result_first = first
    if(len(query_result3) == 0):
        result_last = "er404"
    else:
        result_last = last
    
elif(user_choice == 2):
    # Verify instructor credentials
    cursor.execute("""SELECT ID FROM INSTRUCTOR WHERE ID = ?""", (id,))
    query_result1 = cursor.fetchall()
    cursor.execute("""SELECT FIRST FROM INSTRUCTOR WHERE FIRST = ?""", (first,))
    query_result2 = cursor.fetchall()
    cursor.execute("""SELECT LAST FROM INSTRUCTOR WHERE LAST = ?""", (last,))
    query_result3 = cursor.fetchall()
    if(len(query_result1) == 0):
        result_id = "er404"
    else:
        result_id = id
    if(len(query_result2) == 0):
        result_first = "er404"
    else:
        result_first = first
    if(len(query_result3) == 0):
        result_last = "er404"
    else:
        result_last = last
    
elif(user_choice == 3):
    # Verify admin credentials
    cursor.execute("""SELECT ID FROM ADMIN WHERE ID = ?""", (id,))
    query_result1 = cursor.fetchall()
    cursor.execute("""SELECT FIRST FROM ADMIN WHERE FIRST = ?""", (first,))
    query_result2 = cursor.fetchall()
    cursor.execute("""SELECT LAST FROM ADMIN WHERE LAST = ?""", (last,))
    query_result3 = cursor.fetchall()
    if(len(query_result1) == 0):
        result_id = "er404"
    else:
        result_id = id
    if(len(query_result2) == 0):
        result_first = "er404"
    else:
        result_first = first
    if(len(query_result3) == 0):
        result_last = "er404"
    else:
        result_last = last
    
else:
    print("That was not a valid input. Please try again.\n")
    result_first = "er404"
    result_last = "er404"
    result_id = "er404"

# Successful Log In
if(id == result_id) and (first == result_first) and (last == result_last):
    while user_choice != 0:
    # Student
        if(user_choice == 1):
            student_user = student(first, last, id)
            print("Welcome, " + student_user.show_first() + " " + student_user.show_last() + "!")
            action_choice = int(input("Choose an option:\n1. Search courses\n2. Add courses\n3. Remove courses\n4. Print schedule\n5. Search course by parameter\n0. Exit\n"))
            if(action_choice == 1):
                cursor.execute(student_user.search_courses())
                query_result = cursor.fetchall()
                print(query_result)
            elif(action_choice == 2):
                print(student_user.add_courses(course_list))
            elif(action_choice == 3):
                print(student_user.remove_courses(course_list))
            elif(action_choice == 4):
                print(student_user.print_schedule(course_list))
            elif(action_choice == 5):
                parameters = student_user.search_by_parameters()
                print(cursor.execute("""SELECT * FROM COURSE WHERE (CRN = ? AND TITLE = ? AND DEPARTMENT = ? AND TIME = ? AND DAYS = ? AND SEMESTER = ? AND YEAR = ? AND CREDITS = ?)""" , (parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5], parameters[6], parameters[7])))
                query_result = cursor.fetchall()
                if(len(query_result) != 0):
                    print(query_result)
                else:
                    print("There was an error finding the course in the system.\n")
            elif(action_choice == 0):
                break
        
    # Instructor
        elif(user_choice == 2):
            instructor_user = instructor(first, last, id)
            print("Welcome, " + instructor_user.show_first() + " " + instructor_user.show_last() + "!")
            action_choice = int(input("Choose an option:\n1. Assemble roster\n2. Print roster\n3. Search courses\n4. Search courses by parameter\n0. Exit\n"))
            if(action_choice == 1):
                print(instructor_user.assemble(roster))
            elif(action_choice == 2):
                print(instructor_user.print_roster(roster))
            elif(action_choice == 3):
                cursor.execute(instructor_user.search_courses())
                query_result = cursor.fetchall()
                print(query_result)
            elif(action_choice == 4):
                parameters = instructor_user.search_by_parameters()
                print(cursor.execute("""SELECT * FROM COURSE WHERE (CRN = ? AND TITLE = ? AND DEPARTMENT = ? AND TIME = ? AND DAYS = ? AND SEMESTER = ? AND YEAR = ? AND CREDITS = ?)""" , (parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5], parameters[6], parameters[7])))
                query_result = cursor.fetchall()
                if(len(query_result) != 0):
                    print(query_result)
                else:
                    print("There was an error finding the course in the system.\n")
            elif(action_choice == 0):
                break

    # Admin
        elif(user_choice == 3):
            admin_user = admin(first, last, id)
            print("Welcome, " + admin_user.show_first() + " " + admin_user.show_last() + "!")
            action_choice = int(input("Choose an option:\n1. Add course\n2. Remove course\n3. Add user\n4. Remove user\n5. Add student\n6. Remove student\n7. Add instructor\n8. Remove instructor\n9. Search courses\n10. Search courses by parameter\n0. Exit\n"))
            if(action_choice == 1):
                parameters = admin_user.add_course()
                cursor.execute("""INSERT INTO COURSE VALUES(?, ?, ?, ?, ?, ?, ?, ?);""", (parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5], parameters[6], parameters[7]))
            elif(action_choice == 2):
                crn = admin_user.remove_course()
                cursor.execute("""DELETE FROM COURSE WHERE CRN = ?;""", (crn,))
            elif(action_choice == 3):
                parameters = admin_user.add_user()
                cursor.execute("""INSERT INTO ADMIN VALUES(?, ?, ?, ?, ?, ?);""", (parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5]))
            elif(action_choice == 4):
                id = admin_user.remove_user()
                cursor.execute("""DELETE FROM ADMIN WHERE ID = ?;""", (id,))
            elif(action_choice == 5):
                parameters = admin_user.add_student()
                cursor.execute("""INSERT INTO STUDENT VALUES(?, ?, ?, ?, ?, ?);""", (parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5]))
            elif(action_choice == 6):
                id = admin_user.remove_student()
                cursor.execute("""DELETE FROM STUDENT WHERE ID = ?;""", (id,))
            elif(action_choice == 7):
                parameters = admin_user.add_instuctor()
                cursor.execute("""INSERT INTO INSTRUCTOR VALUES(?, ?, ?, ?, ?, ?, ?);""", (parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5], parameters[6]))
            elif(action_choice == 8):
                id = admin_user.remove_instructor()
                cursor.execute("""DELETE FROM INSTRUCTOR WHERE ID = ?;""", (id,))
            elif(action_choice == 9):
                cursor.execute(admin_user.search_courses())
                query_result = cursor.fetchall()
                print(query_result)
            elif(action_choice == 10):
                parameters = admin_user.search_by_parameters()
                print(cursor.execute("""SELECT * FROM COURSE WHERE (CRN = ? AND TITLE = ? AND DEPARTMENT = ? AND TIME = ? AND DAYS = ? AND SEMESTER = ? AND YEAR = ? AND CREDITS = ?)""" , (parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5], parameters[6], parameters[7])))
                query_result = cursor.fetchall()
                if(len(query_result) != 0):
                    print(query_result)
                else:
                    print("There was an error finding the course in the system.\n")
            elif(action_choice == 0):
                break
else:
    print("There was an error signing in. Your name or W number might have been spelled incorrectly. Please try again.\n")

database.commit()
database.close()