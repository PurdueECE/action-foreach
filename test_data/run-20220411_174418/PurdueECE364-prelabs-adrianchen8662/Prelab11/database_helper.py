import pysqlite3 as sqlite3
import student

def insertStudent(student):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    print(student.firstName)
    print(student.lastName)
    print(student.studentID)
    print(student.emailID)
    conn.execute('INSERT INTO students (firstname, lastname, id, email) VALUES (?, ?, ?, ?)', [student.firstName, student.lastName, student.studentID, student.emailID])
    conn.commit()

def getStudentsByName(lastname):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    lastList = conn.execute('SELECT * FROM students WHERE lastname = ?',[lastname]).fetchall()
    if not lastList:
        print("No students with last name "+lastname+" found")
        return
    return lastList

def updateID(student1, ID):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    print(student1.lastName)
    IDList = conn.execute("SELECT id FROM students").fetchall()
    for i in IDList:
        if ID in i:
            print("ID already in the database")
            return
    conn.execute('UPDATE students SET id=? WHERE lastname=?',[ID,student1.lastName])
    conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS students (firstname varchar(255), lastname varchar(255), id INTEGER PRIMARY KEY, email varchar(255))')