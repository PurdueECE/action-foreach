from sqlite3 import Cursor
from unittest.mock import NonCallableMagicMock
from urllib.parse import ParseResultBytes
import student as student1
import pysqlite3 as sqlite3

def insertStudent(student1):
    firstName = student1.firstName
    lastName = student1.lastName
    id_num = student1.studentID
    email = student1.emailID
    with sqlite3.connect("data/database.db") as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (first_name, last_name, id, email) VALUES (?,?,?,?)", 
        (firstName, lastName, id_num, email))

def getStudentsByName(lastName):
    with sqlite3.connect("data/database.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students WHERE last_name = ?", (lastName,))
        match = cursor.fetchall()
        # print(match)
        if match is None:
            print("There are no records with this last name.")
        else:
            return match

def updateID(student1, ID):
    firstName = student1.firstName
    student1.id = ID
    with sqlite3.connect("data/database.db") as connection:
        cursor = connection.cursor()
        query = """UPDATE students SET id = ? WHERE first_name = ?"""
        test = cursor.execute(query, (student1.id, firstName))


if __name__ == "__main__":
    nimal = student1.Student("Nimal", "Padmanabhan", 123)
    # insertStudent(nimal)
    # joe = student1.Student("Joe", "Man", 456)
    # carl = student1.Student("Carl", "Sandburg", 122)
    # insertStudent(joe)
    # insertStudent(carl)
    mom = student1.Student("Hey", "Mom", 2335)
    # insertStudent(mom)

    # print(getStudentsByName("Padmanabhan"))
    updateID(mom, 691)
    updateID(nimal, 234)
