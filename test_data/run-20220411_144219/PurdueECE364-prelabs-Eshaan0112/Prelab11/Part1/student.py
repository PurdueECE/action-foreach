
class Student():
    def __init__(self, firstName, lastName, studentID):
        self.firstName = firstName
        self.lastName = lastName
        self.studentID = studentID
        self.emailID = self.lastName+'.'+self.firstName+'@university.com'

#s = Student('g', 'l', 12)
#print(s.emailID)