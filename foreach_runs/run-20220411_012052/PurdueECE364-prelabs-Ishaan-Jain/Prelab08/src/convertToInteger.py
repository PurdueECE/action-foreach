# ######################################################
# Author : Ishaan Jain
# email : jain343@purdue.edu
# ID : ee364b04
# Date : 03/06/2022
# ######################################################
import os
from re import X
#import readline
from signal import pthread_kill # List of module import statements
import sys
from unittest import result # Each one on a line
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def convertToInteger(boolList):
    ans = ""

    if len(boolList) == 0:
        return None 

    for x in boolList:
        if x != True and x != False:
            return None    
        if x == False:
            ans = ans + "0"
        elif x == True:
            ans = ans + "1"

    num = int(ans,2)

    return num            

# if __name__ == "__main__":
#       lis = convertToInteger([False,False,True, False, False, True])
#       print(lis)  