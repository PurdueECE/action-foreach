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


def getStreakProduct(sequence, maxSize, product):
    lis = []
    for i in range(len(sequence) - 1):
         for j in range(2, maxSize+1):
             if getNum(sequence, i, j) == product:
                 f = sequence[i:i+j]
                 lis.append(f)
    return lis   

def getNum(sequence, start, num):
	if len(sequence) < start + num:
		return 0
	total = 1
	for i in range(num):
		total = total * int(sequence[start+i])
	return total



# if __name__ == "__main__":
#     result = getStreakProduct("00780207910792197361",6,5)
#     print(result)
				