from student import Student 
import pysqlite3 as sqlite3

def insertStudent(student1):
    insert = "INSERT INTO students (firstName, lastName, id, email) VALUES(?,?,?,?)"
    data = (student1.firstName, student1.lastName, student1.studentID, student1.emailID)
    cursor.execute(insert, data)
    connection.commit() # Commit the changes to the table

def getStudentsByName(lastname):
    get = f"SELECT * FROM students WHERE lastName = '{lastName}'"
    # cursor.execute(get)
    records = cursor.fetchall()
    #for col in records: # Test
    #    print(col)
    if len(records) == 0:
        print (f"No records match Last Name {lastName}")
    #else:
    #   print(f'Records = {records}')
    return records

def updateID(student1, ID):
    get_id = f"SELECT id FROM students"
    cursor.execute(get_id)
    ids = cursor.fetchall()
    id_list =[]
    #print(f'ids = {ids}')
    for tup in ids:
        id_list.append(tup[0])
    if ID in id_list:
        print(f'ID {ID} is already taken up by another user')
        return

    update = f"UPDATE students SET id = {ID} WHERE firstName = '{student1.firstName}' AND lastName = '{student1.lastName}'"
    cursor.execute(update)
    connection.commit()
    
if __name__=="__main__":
    # Connecting to data/database.db
    connection =  sqlite3.connect("data/database.db")
    cursor = connection.cursor()
    
    # Creating a table using cursor.execute if it doesn't exist already
    stmt = "DROP TABLE IF EXISTS students"
    cursor.execute(stmt)
    create_table = "CREATE TABLE students (firstName text, lastName text, id int PRIMARY KEY UNIQUE, email text UNIQUE)"
    cursor.execute(create_table)
    
    # Part1.2.1
    student1 = Student("Eshaan", "Minocha", 123)
    student2 = Student("Pragati", "Minocha", 111)
    student3 = Student("Priyanshi", "Sethi", 314)
    insertStudent(student1) 
    insertStudent(student2)
    insertStudent(student3)

    # Part1.2.2
    lastName = "Minocha"
    getStudentsByName(lastName)

    #Part1.2.3
    updateID(student3, 321)
    #updateID(student1, 321)
    #updateID(student2, 123) 
    connection.close()

    

    





    