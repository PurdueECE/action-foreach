# ######################################################
# Author : Christine Fang
# email : fang245@purdue.edu
# ID : ee364b09
# Date : 04/03/2021
# ######################################################

import pysqlite3 as sqlite3
import student

def insertStudent(student1):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute("INSERT into students VALUES (?, ?, ?, ?)",(student1.firstName,student1.lastName,student1.studentID,student1.emailID))
    cursor.execute("SELECT * FROM students ")
    database.commit()
    database.close()

def getStudentsByName(lastname):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute("SELECT * from students WHERE last_name=?",(lastname,))
    if cursor.fetchall() == []:
        return "last name is not in the students database"
    else:
        cursor.execute("SELECT * from students WHERE last_name=?",(lastname,))
        return (cursor.fetchall())

def updateID(student1,ID):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute("SELECT * from students WHERE id=? and email=?", (student1.studentID,student1.emailID))
    if cursor.fetchall() == []:
        raise KeyError("student is not in the database")
    cursor.execute("SELECT * from students WHERE id=?", (ID,))
    if cursor.fetchall() != []:
        raise KeyError ("ID already exists in the database")
    cursor.execute("UPDATE students SET id = ? WHERE id=? and email=?",(ID,student1.studentID,student1.emailID))
    student1.studentID = ID
    database.commit()
    cursor.execute("SELECT * FROM students ")
    print(cursor.fetchall())
    database.close()

if __name__ == "__main__" :
    # conn = sqlite3.connect('database.db')
    # c = conn.cursor()
    # create_tasks = """CREATE TABLE IF NOT EXISTS students (
    #                             first_name STRING,
    #                             last_name STRING,
    #                             id INTEGER PRIMARY KEY,
    #                             email STRING
    #                             );"""
    # c.execute(create_tasks)

    student1 = student.Student('chriine','fang',245)
    # insertStudent(student1)
    student2 = student.Student('erin','fang',234)
    # insertStudent(student2)
    student3 = student.Student("erin","tran",902)
    # insertStudent(student3)
    print(getStudentsByName('fang'))
    updateID(student3, 2342)

