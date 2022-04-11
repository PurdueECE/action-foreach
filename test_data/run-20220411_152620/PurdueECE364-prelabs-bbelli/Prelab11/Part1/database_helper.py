import student
import pysqlite3 as sqlite3

def instertStudent(student1):
    name = student1.firstName
    lname = student1.lastName
    stid = student1.id
    email = student1.email
    c.execute("INSERT INTO students VALUES(?, ?, ?, ?)", (name, lname, stid, email))
    

def getStudentsByName(lastname):

    student = c.execute("SELECT * from students WHERE last_name = ?", (lastname))
    return student


def updateID(student1, ID):
    
    old_id = student1.id
    c.execute("UPDATE students SET id = ? WHERE id = ?", (ID, old_id))



if __name__ == "__main__":
    
    con = sqlite3.connect('database.db')
    c = con.cursor()
    c.execute('''CREATE TABLE students
               (first_name text, last_name text, id real, email text)''')
