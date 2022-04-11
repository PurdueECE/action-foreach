import pysqlite3 as sqlite3



class Student:
    def __init__(self, firstName, lastName, studentID):
        self.firstName = firstName
        self.lastName = lastName
        self.studentID = studentID
        self.email = lastName + "." + firstName + "@university.com"

