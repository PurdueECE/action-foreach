# ######################################################
# Author : Will Moffat
# email : moffatw@purdue.edu
# ID : ee364b13
# Date : 1/16/22
# ######################################################

import os
import sys

def writePyramids(filePath, baseSize, count, char):
    
    pyramid_list = []

    # Generate each line of the file
        
    for i in range(baseSize, 0, -2):
        
        line = ""
        
        for j in range (count):
            line += " " * int(((baseSize - i) / 2))
            line += char * i
            line += " " * int(((baseSize - i) / 2))

            if (j != (count - 1)):
                line += " "

        pyramid_list.append(line)

    
    # Write list to file

    pyramid_list.reverse()

    file = open(filePath, "w")
    for element in pyramid_list:
        file.write(element + "\n")
    file.close()

    return

def getStreaks(sequence, letters):

    letter_list = list(letters)
    streak_list = []
    return_list = []
    previous_char = sequence[0]
    letter_string = ""

    for i, letter in enumerate(sequence):
        if (letter == previous_char):
            letter_string += letter
        else:
            streak_list.append(letter_string)
            letter_string = letter

        if (i == (len(sequence) - 1)):
            streak_list.append(letter_string)

        previous_char = letter

    for streak in streak_list:
        for letter in letter_list:
            if (letter == streak[0]):
                return_list.append(streak)

    return return_list