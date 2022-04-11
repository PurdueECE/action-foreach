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

def convertToBoolean(num, size):

    lis = []

    if num< 0 or size< 0:
        return lis 
    if type(num) is not int:
        return lis

    number = ""
    number = str(bin(num))

    
    if size < 0 or len(number) < 0:
        return lis


    b = size - (len(number) - 2) 
    print(b)

    while b != 0:
          lis.append(False)
          b -= 1

    for i in range(2,len(number)):
        lis.append(bool(int(number[i])))

    return lis    


# if __name__ == "__main__":
#     lis = convertToInteger([False,False,True,False,False,True])
#     print(lis)
