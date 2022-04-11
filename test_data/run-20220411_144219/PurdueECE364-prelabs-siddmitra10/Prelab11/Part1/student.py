class Student:
    def __init__(self, firstName, lastName, studentID):
        self.firstName = firstName
        self.studentID = studentID
        self.lastName = lastName
        self.emailID = lastName + "." + firstName + "@university.com"