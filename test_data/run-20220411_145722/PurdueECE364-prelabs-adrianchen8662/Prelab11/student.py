class Student:
    def __init__(self, firstName, lastName, studentID):
        self.firstName = firstName
        self.lastName = lastName
        self.studentID = studentID
        self.emailID = lastName+"."+firstName+"@university.com"
    