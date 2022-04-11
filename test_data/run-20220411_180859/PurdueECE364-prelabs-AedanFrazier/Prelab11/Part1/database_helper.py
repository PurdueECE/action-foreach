########################################
# Author:   Aedan Frazier
# Email:    frazie35@purdue.edu
# ID:       ee364a06
# Date:     3/28/2022
########################################

from ctypes import sizeof
from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE
from student import *
import pysqlite3 as sqlite3


def insertStudent(student1: Student):
    sqlconnect = sqlite3.connect('data/database.db')
    cursor = sqlconnect.cursor()
    cursor.execute("INSERT INTO students VALUES(?,?,?,?)", [student1.firstName, student1.lastName, student1.studentID, student1.emailID])
    sqlconnect.commit()

def getStudentsByName(lastname: str):
    sqlconnect = sqlite3.connect('data/database.db')
    cursor = sqlconnect.cursor()
    cursor.execute("SELECT * FROM students WHERE last_name = ?;", [lastname])
    students = cursor.fetchall()
    if(len(students) == 0):
        return("No students with the last name '" +  lastname + "'")
    else:
        return students
    
def updateID(student1: Student, ID: int):
    sqlconnect = sqlite3.connect('data/database.db')
    cursor = sqlconnect.cursor()
    cursor.execute("UPDATE students SET id = ? WHERE id = ?;", [ID, student1.studentID])
    sqlconnect.commit()

if __name__ == "__main__":
    sqlconnect = sqlite3.connect('data/database.db')
    cursor = sqlconnect.cursor()
    #command =   "CREATE TABLE students(first_name string,last_name string,id int PRIMARY KEY,email string);"
    #command = "DROP TABLE students"
    #cursor.execute(command)

    James = Student("James", "Franco", 111111111)
    # insertStudent(James)
    # Dave = Student("Dave", "Franco", 222222222)
    # insertStudent(Dave)
    # print(getStudentsByName("Franco"))

    updateID(James, 333333333)
    print(getStudentsByName("Franco"))