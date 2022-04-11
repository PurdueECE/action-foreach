# import pysqlite3 as sqlite3
import sqlite3
import student

# CREATE TABLE students (
#     first_name string,
#     last_name string,
#     id int primary key,
#     email string
# );

def insertStudent(student1):
    con = sqlite3.connect('data/database.db')
    cur = con.cursor()
    firstName = str(student1.firstName)
    lastName = str(student1.lastName)
    studentID = str(student1.studentID)
    emailID = str(student1.emailID)

    cur.execute(f'''INSERT INTO students VALUES 
                    ('{firstName}','{lastName}',
                    '{studentID}','{emailID}')''')
    
    # con.commit()
    # con.close()
    return


def getStudentsByName(lastname):
    con = sqlite3.connect('data/database.db')
    cur = con.cursor()

    # cur.execute(f'''SELECT '{lastname}' FROM students''')

    cur.execute(f'''SELECT first_name,last_name,id,email FROM students WHERE last_name = ('{lastname}')''')
    i = 0
    rows = cur.fetchall()
    # print(rows)
    for row in rows:
        i = i + 1
        print(str(row))
    if i == 0:
        print('Error, no entries found')
    return


def updateID(student1, ID):
    oldID = student1.studentID
    newStudent1 = student.Student(student1.firstName, student1.lastName, ID, student1.emailID)

    #verify duplicates first
    cur.execute(f'''SELECT id FROM students WHERE id = ('{ID}')''')
    items = cur.fetchall()
    if items:
        print('ID Already Exists!')
        return
    #delete + replace
    cur.execute(f'''DELETE FROM students WHERE id = {oldID}''')
    insertStudent(newStudent1)
    return


if __name__ == '__main__':
    con = sqlite3.connect('data/database.db')
    cur = con.cursor()

    # cur.execute('''CREATE TABLE students
    #                 (first_name text, last_name text, 
    #                 id int primary key, email text)''')

    student1 = student.Student('a','b',4,'c')
    # print(student1.firstName, student1.lastName, student1.studentID, student1.emailID)
    # insertStudent(student1)
    # getStudentsByName('b')
    updateID(student1, 5)


    con.commit()
    con.close()

