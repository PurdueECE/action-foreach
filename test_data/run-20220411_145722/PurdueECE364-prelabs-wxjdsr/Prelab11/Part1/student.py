# ######################################################
# Author :  Xingjian Wang
# email :   wang5066@purdue.edu
# ID:       ee364b03
# Date :    Apr 3, 2022
# ######################################################


# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
class Student:
    def __init__(self, firstName, lastName, studentID):
        self.firstName = firstName
        self.lastName = lastName
        self.studentID = studentID
        self.emailID = f"{lastName}.{firstName}@university.com"
