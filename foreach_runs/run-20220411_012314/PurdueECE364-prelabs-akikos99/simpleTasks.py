# ######################################################
# Author : <Andrew Kikos>
# email : <akikos@purdue.edu>
# ID : <ee364j20>
# Date : <01/11/22>
# ######################################################

import os # List of module import statements
import sys # Each one on a line


# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def writePyramids(filePath, baseSize, count, char):
    # Write base line
    charCount = 0
    while charCount < baseSize:
        print(char)
        charCount += 1
    
    return 0


# def getStreaks(sequence, letters):
    
#     return 1

    
# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == " __main__ " :
    # Write anything here to test your code .
    z = writePyramids ('pyramid13.txt', 13, 6, '*')
    x = writePyramids ('pyramid15.txt', 15, 5, 'X')
    print ( z )
    print ( x )