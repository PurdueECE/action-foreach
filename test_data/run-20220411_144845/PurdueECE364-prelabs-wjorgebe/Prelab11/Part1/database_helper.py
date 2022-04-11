# ######################################################
#   Author :    William Jorge
#   email :     wjorgebe@purdue.edu
#   ID :        ee364b12   
#   Date :      April 3, 2022
# ######################################################

from inspect import currentframe
import student
import sqlite3

def insertStudent(student1):
    try:
        cur.execute('''INSERT INTO students VALUES (?, ?, ?, ?)''',
                        (student1.firstName, student1.lastName, student1.studentID, student1.emailID))
        con.commit()
    except sqlite3.Error:
        print("Could not add student " + student1.firstName + " " + student1.lastName)

def getStudentsByName(lastname):
    try:
        cur.execute('''SELECT * FROM students WHERE last_name= ?''', (lastname,))
        students = cur.fetchall()
        return students
    except sqlite3.Error:
        print("No students match last name " + lastname)

def updateID(student1, ID):
    try:
        cur.execute('''UPDATE students SET id=? WHERE id=?''', (ID, student1.studentID))
        con.commit()
    except sqlite3.Error:
        print("New ID must not already be in use")

if __name__ == "__main__":
    con = sqlite3.connect("data/database.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS students
                (first_name text, last_name text, id int primary key, email text)''')
    new_student = student.Student(firstName='William', lastName='Jorge', studentID=2)
    # insertStudent(new_student)
    # print(getStudentsByName(new_student.lastName))
    # print(getStudentsByName(new_student.lastName))
