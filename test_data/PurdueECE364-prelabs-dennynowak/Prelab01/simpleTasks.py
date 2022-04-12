#############################################
#   Author:     Denny Nowak
#   Email:      nowak32@purdue.edu
#   ID:         ee364b14
#   Date:       01/14/2022
#############################################

import os  
import sys

#############################################
# No Module-Level Variables or Statements
# Only Functions Beyond This Point
#############################################

# Problem 1
def writePyramids(filePath, baseSize, count, char):
    # Generate pyramid string
    pyramid = ''
    if (count != 0):
        # Each line of pyramid
        for n in range(1, baseSize+1, 2):
            numOfSpaces = int((baseSize-n) / 2)
            spaceStr = ''
            for x in range(0, numOfSpaces, 1):
                spaceStr += ' '
            # Include all pyramids
            for i in range(0, count, 1):
                pyramid += spaceStr
                for x in range (0, n, 1):
                    pyramid += char
                pyramid += spaceStr
                if (i != count - 1):
                    pyramid += ' '
            # New line of pyramid
            pyramid += '\n'

    # Write pyramid string to target file
    fptr = open(filePath, "w")
    fptr.write(pyramid)
    fptr.close()
    return

# Problem 2
def getStreaks(sequence, letters):
    streakList = []

    # Iterate through sequence
    prevChar = sequence[0]
    streakStr = ''
    for char in sequence:
        # Check if char in list
        if char in letters:
            # Check if streak
            if char == prevChar or streakStr == '':
                # Continue/start streak
                streakStr += char                
            else:
                # End streak and start new
                if streakStr != '':
                    streakList.append(streakStr) 
                streakStr = char
        prevChar = char  

    # Check if no streaks
    if streakStr == '':
        return streakList
    
    streakList.append(streakStr) 
    return streakList

# This block is optional and can be used for testing.
# We will not look into its content.
########################################################
if __name__ == "__main__":
    # Write anything here to test your code.
    #writePyramids('test.txt', 13, 6, 'X')
    #writePyramids('test2.txt', 15, 5, '*')
    #writePyramids('test3.txt', 13, 0, 'X')
    #print(getStreaks("AAASSSSSSAPPPSSPPBBCCCSSS", "SAQT"))
    #print(getStreaks("AAASSSSSSAPPPSSPPBBCCCSSS", "PAZ"))
    #print(getStreaks("XXXXXXXXXX", "PAZ"))
    #print(getStreaks("AAASSSSSSAPPPSSPPBBCCCSSS", "PAZSAQTCB"))
    pass