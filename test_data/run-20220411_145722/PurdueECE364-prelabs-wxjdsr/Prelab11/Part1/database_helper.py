# ######################################################
# Author :  Xingjian Wang
# email :   wang5066@purdue.edu
# ID:       ee364b03
# Date :    Apr 3, 2022
# ######################################################

from student import *
import sqlite3

DATABASE_PATH = "data/database.db"
DEBUG_MODE = 0

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
# A helper function that builds the connection
# Return the connection and cursor
def _connect():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    return conn, cursor


# All functionality below
def insertStudent(student1: Student):
    conn, cursor = _connect()
    student_data = (student1.firstName, student1.lastName,
                    student1.studentID, student1.emailID)
    try:
        cursor.execute('''INSERT INTO students(first_name, last_name, id, email)
                VALUES(?, ?, ?, ?)''', student_data)
    except sqlite3.IntegrityError as err:
        raise ValueError(f'Student id {student1.studentID} already exists, cannot insert')
    else:
        conn.commit()


def getStudentsByName(lastname):
    conn, cursor = _connect()
    sql = "SELECT * FROM students WHERE last_name = '%s'" %lastname
    fetchall = cursor.execute(sql)
    data = fetchall.fetchall()
    # Check if there is match
    if (len(data) == 0):    # no match
        return f'There is no match with lastname {lastname}'
    else:
        return data


def updateID(student1, ID):
    conn, cursor = _connect()
    sql = '''UPDATE students 
        SET id= '%d' 
        WHERE id= '%d'
        AND first_name = '%s' 
        AND last_name = '%s'
        ''' % (ID, student1.studentID, student1.firstName, student1.lastName)
    try:
        cursor.execute(sql)
    except sqlite3.IntegrityError as err:
        raise ValueError(f'ID {ID} already exists, cannot update')
    else:
        conn.commit()


# ######################################################
# Build the database manually
# ######################################################
if __name__ == "__main__":
    conn, cursor = _connect()
    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                ([first_name] text,
                [last_name] text,
                [id] INTEGER PRIMARY KEY,
                [email] text)''')
    conn.commit()
    
    
# ######################################################
# Optional Test Block
# ######################################################
if DEBUG_MODE:
    student_sample = Student("Letter", "Wang", 33125)
    # Test insertStudent
    insertStudent(student_sample)
    # Test getStudentsByName
    print(getStudentsByName("fgfd"))
    # Test updateID(student1, ID)
    updateID(student_sample, 21322)
    