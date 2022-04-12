# ######################################################
#   Author :    William Jorge
#   email :     wjorgebe@purdue.edu
#   ID :        ee364b12   
#   Date :      April 3, 2022
# ######################################################

class Student:
    def __init__(self, firstName, lastName, studentID):
        self.firstName = firstName
        self.lastName = lastName
        self.studentID = studentID
        self.emailID = lastName.lower() + "." + firstName.lower() + "@university.com"