#######################################################
# Author: Insherah Neizer-Ashun 
# email: ineizera@purdue.edu 
# ID: ee364a20
# Date: 01/13/22
#######################################################

import os # List of module import statements
import sys # Each one on a line

#######################################################
# No Module -Level Variables or Statements!
# ONLY FUNCTIONS BEYOND THIS POINT!
#######################################################
def writePyramids(fileName, baseSize, count, char):
    file = open(fileName, "a")
    spaces = baseSize -1
    for i in range(0,baseSize):
        for j in range(0, spaces):
            file.write(" ")
        spaces = spaces - 1
        for j in range(0, i+1):
            file.write(char)
        file.write("\r")       
    file.close() 
def getStreaks(sequence, letters):
    return 1
# This block is optional and can be used for testing.
# We will NOT look into its content.
#######################################################
if __name__ == "__main__":
    # Write anything here to test your code.
    
    writePyramids('pyramid5_1.txt', 5, 3, 'X')
