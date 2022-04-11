import student
import pysqlite3 as sqlite3


def insertStudent(student1):
    first_name = student1.firstName
    last_name = student1.lastName
    id = student1.studentID
    email = student1.emailID
    with sqlite3.connect("data/database.db") as connection:
        cur = connection.cursor()
        cur.execute(f'INSERT INTO students VALUES("{first_name}", "{last_name}",{id}, "{email}")')

def getStudentsByName(lastname):
    with sqlite3.connect("data/database.db") as connection:
        cur = connection.cursor()
        match = cur.execute(f'SELECT * FROM students WHERE last_name = "{lastname}"').fetchall()
        if match is None:
            print("Invalid lastname entered")
        else:
            return match

def updateID(student1, ID):
    first_name = student1.firstName
    last_name = student1.lastName
    student1.id = int(ID)
    with sqlite3.connect("data/database.db") as connection:
        cur = connection.cursor()
        test = cur.execute(f'UPDATE students SET id = {student1.id} WHERE first_name = "{first_name}" AND last_name="{last_name}"')

if __name__ == "__main__":
    sidd = student.Student("Sidd", "Mitra", 12)
    updateID(sidd, 100)
    # print(sidd)
    # insertStudent(student.Student("Suhani", "Mitra", 11))
    print(getStudentsByName("Mitra"))
