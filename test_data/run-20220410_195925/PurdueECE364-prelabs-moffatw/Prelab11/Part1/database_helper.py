import student
import sqlite3
from sqlite3 import Error

def insertStudent(student1):
    conn = sqlite3.connect("data/database.db")

    sql = ''' INSERT INTO students(first_name, last_name, id, email)
              VALUES(?,?,?,?) '''

    cur = conn.cursor()

    try:
        cur.execute(sql, (student1.firstName, student1.lastName, student1.studentID, student1.emailID))
    except Error as e:
        print(e)

    conn.commit()

def getStudentsByName(lastname):
    conn = sqlite3.connect("data/database.db")

    sql = ''' SELECT * FROM students WHERE last_name = ? '''

    cur = conn.cursor()

    cur.execute(sql, (lastname,))

    result = cur.fetchall()

    if result == []:
        return "No students found"
    else:
        return result

def updateID(student1, ID):
    conn = sqlite3.connect("data/database.db")

    sql = ''' SELECT * FROM students WHERE ID = ? '''

    cur = conn.cursor()

    cur.execute(sql, (ID,))

    result = cur.fetchall()

    if result != []:
        raise Exception("ID already in use")

    sql = ''' UPDATE students
              SET id = ?
              WHERE id = ? '''

    cur.execute(sql, (ID, student1.studentID))

    conn.commit()


if __name__ == "__main__":

    conn = None
    try:

        # Create database
        conn = sqlite3.connect("data/database.db")
        
        # Create table
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS students")

        table = """ CREATE TABLE students (
                    first_name String,
                    last_name String,
                    id Integer PRIMARY KEY,
                    email String
                ); """

        cur.execute(table)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

    # Test functions

    test_student = student.Student("Will", "Moffat", 1)
    insertStudent(test_student)
    print(getStudentsByName("Moffat"))
    updateID(test_student, 2)
    print(getStudentsByName("Moffat"))