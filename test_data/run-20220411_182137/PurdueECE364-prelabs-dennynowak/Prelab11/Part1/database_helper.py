################################
#   Author: Denny Nowak
#   Email:  nowak32@purdue.edu
#   ID:     ee364b14
#   Date:   04/01/2022
################################
import student
import pysqlite3 as sqlite3


# Insert student object to db
def insertStudent(student1):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("INSERT INTO students (first_name, last_name, id, email) VALUES (?, ?, ?, ?)", (str(student1.firstName), str(student1.lastName), int(student1.studentID), str(student1.getEmailID())))
    con.commit()
    con.close()


# Get students by last name
def getStudentsByName(lastname):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT * from students where last_name = ?", (lastname,))
    rows = cur.fetchall()
    con.close()
    if not rows:
        return 'No matching students with last name: ' + lastname
    return rows


def updateID(student1, ID):
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    # Check if existing id 
    cur.execute("SELECT * from students where id = ?", (ID,))
    rows = cur.fetchall()
    if rows:
        raise Exception('ID already exists: ' + str(ID))
    
    # Update id otherwise
    cur.execute("UPDATE students SET id = ? where id = ?", (ID, str(student1.studentID),))
    con.commit()
    con.close()



if __name__ == '__main__':
    # Create database manually
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE students (first_name text, last_name text, id int primary key, email text)''')
    con.commit()
    con.close()

    # Testing
    # testStudent = student.Student('student', 'test', 6)
    # insertStudent(testStudent)
    # updateID(testStudent, 0)
    # print(getStudentsByName('test'))