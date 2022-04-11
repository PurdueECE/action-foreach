# ######################################################
# Author : Christine Fang
# email : fang245@purdue.edu
# ID : ee364b09
# Date : 04/03/2021
# ######################################################

class Student:
    def __init__(self,firstname: str,lastname: str,ID: int):
        self.firstName = firstname
        self.lastName = lastname
        self.studentID = ID
        self.emailID = self.lastName + '.' + self.firstName + '@university.com'
