

class Student:

    def __init__(self, first, last, id):
        self.firstName = first
        self.lastName = last
        self.studentID = id
        self.emailID = last + "." + first + "@university.com"
