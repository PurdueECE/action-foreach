# ######################################################
# Author : < Nimal Padmanabhan >
# email : < npadmana@purdue.edu >
# ID : < ee364b17 >
# Date : < 3/5/2022 >
# ######################################################
from cgi import print_form
import os # List of module import statements
import sys
# from typing import List
from unicodedata import decimal # Each one on a line
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
def convertToBoolean(num, size):
    boolList = []
    if type(num) is not int:
        return boolList
    if num < 0 or size < 0:
        return boolList
    binary = bin(num).replace("0b", "").zfill(size) # Appends leading zeros based on size
    for digit in binary:
        boolList.append(bool(int(digit)))
    return boolList

def convertToInteger(boolList):
    if type(boolList) is not list or len(boolList) == 0:
        return None
    intList = []
    for boolean in boolList:
        if type(boolean) is not bool:
            return None
        intList.append(int(bool(boolean)))
    intList = [str(x) for x in intList]
    intStrNum = int("".join(intList), 2)
    return intStrNum
    

# if __name__ == "__main__":
# #    print("135: "+str(convertToBoolean(135, 12)))
# #    print("9: "+str(convertToBoolean(9, 3)))
#    print(convertToInteger([True, False, False, True]))
