########################################
# Author:   Aedan Frazier
# Email:    frazie35@purdue.edu
# ID:       ee364a06
# Date:     3/28/2022
########################################


class Student:
    def __init__(self, firstName, lastName, studentID):
        self.firstName  = firstName
        self.lastName   = lastName
        self.studentID  = studentID
        self.emailID    = lastName + "." + firstName + "@university.com"