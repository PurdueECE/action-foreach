import student
import sqlite3


insertStudent(student1):
    conn = sqlite3.connect("database.db")
    conn.execute("INSERT INTO students(first_name, last_name, id, email) VALUES(?,?,?,?)",(student1.firstName, student1.lastName, student1.studentID, student1.emailID))
    conn.commit()
    conn.close()

getStudentsByName(lastname):
    conn = sqlite3.connect("database.db")
    c = con.cursor()
    students = (c.execute("SELECT first_name,last_name,id,email FROM students WHERE last_name = ?",(lastname)).fetchall())
    conn.close()
    if len(students) == 0 :
        print("no students match the lastname.")
    return students

updateID(student1, ID):
    conn = sqlite3.connect("database.db")
    c = con.cursor()
    students = (c.execute("UPDATE students SET id = ? WHERE id = ?",(ID,student1.id)))
    conn.close()

if __name__ == "__main__":
    print("hello")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    students = (cursor.execute("CREATE TABLE students(first_name STRING, last_name STRING, id PRIMARY KEY, email STRING)"))
    conn.close()
