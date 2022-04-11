import pysqlite3 as sqlite3
import student as student1

def insertStudent(student1):
    firstName = student1.firstName
    lastName = student1.lastName
    Id = student1.studentID
    email = student1.emailID
    with sqlite3.connect("data/database.db") as connection:
        cur = connection.cursor()
        cur.execute("INSERT INTO students (first_name, last_name,id, email) VALUES (?,?,?,?)", (firstName, lastName, Id,email))

def getStudentsByName(lastname):
    with sqlite3.connect("data/database.db") as connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM students WHERE last_name = ?",(lastname,))
        match = cur.fetchall()
        if match is None:
            print("No matching records")
        else:
            return match

def updateID(student1, ID):
    firstName = student1.firstName
    student1.id = ID
    with sqlite3.connect("data/database.db") as connection:
        cur = connection.cursor()
        q = """UPDATE students SET id = ? WHERE first_name = ?"""
        test = cur.execute(q,(student1.id,firstName))


if __name__ == "__main__":
    Ishaan = student1.Student("Ishaan", "Jain", 1807)
    dad = student1.Student("Nitin", "Jain", 134)
    # insertStudent(Ishaan)
    # insertStudent(dad)

    #print(getStudentsByName("Jain"))
    updateID(Ishaan, 465)        
