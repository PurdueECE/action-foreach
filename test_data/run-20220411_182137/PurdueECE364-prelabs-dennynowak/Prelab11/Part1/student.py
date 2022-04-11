################################
#   Author: Denny Nowak
#   Email:  nowak32@purdue.edu
#   ID:     ee364b14
#   Date:   04/01/2022
################################
import pysqlite3 as sqlite3


# Problem 1 Python Class
class Student:
    def __init__(self, firstName, lastName, studentID):
        self.firstName = firstName
        self.lastName = lastName
        self.studentID = studentID
        

    def getEmailID(self):
        return self.lastName + '.' + self.firstName + '@university.com'


if __name__ == '__main__':
    pass
