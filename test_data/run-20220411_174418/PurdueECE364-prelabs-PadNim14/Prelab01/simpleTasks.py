# ######################################################
# Author : < Nimal Padmanabhan >
# email : < npadmana@purdue.edu >
# ID : < ee364b17 >
# Date : < 1/12/2022 >
# ######################################################
import os # List of module import statements
import sys
from typing import List # Each one on a line
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
## Problem 1: writePyramids
def getPyramid(baseSize, char):
    # initialize the pyramid
    # baseSize = number of character
    pyramid = ''
    rowLimit = (baseSize // 2) + 1
    # for each row in the pyramid
    for row in range(rowLimit):
        # get the number of spaces to add to the pyramid
        spaces = baseSize - row - 1
        # get the number of chars to add to the pyramid
        chars = row * 2 + 1
        # add the spaces to the pyramid
        pyramid += ' ' * spaces
        # add the chars to the pyramid
        pyramid += char * chars
        # add a new line to the pyramid
        pyramid += '\n'
    # return the pyramid
    return pyramid

def writePyramids(filePath, baseSize, count, char):
    # open the file
    pyrlist = []
    with open(filePath, 'w') as f:
        # for each pyramid in the pyramid list
        for pyramid in range(count):
            # get the pyramid
            pyr = getPyramid(baseSize, char)
            pyrlist.append(pyr)
            # write the pyramid to the file
        for pyr in pyrlist:
           f.write(pyr)

## Problem 2: getStreaks, returns a list of repeated letters
## Input: sequence(string), letters(string)
def getStreaks(sequence, letters):
    streaks = []
    for letter in letters:
        streak = ''
        for i in range(len(sequence)):
            if sequence[i] == letter:
                streak += letter
            else:
                if len(streak) > 0:
                    streaks.append(streak)
                streak = ''
        if len(streak) > 0:
            streaks.append(streak)
    return streaks

# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == "__main__":
    writePyramids("pyramid13_nimal.txt", 13, 6, "X")
    writePyramids('pyramid15_nimal.txt', 15, 5, '*')

    sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
    print(getStreaks(sequence, "SAQT"))
    print(getStreaks(sequence, "PAZ"))
    print(getStreaks(sequence, "WXY"))


