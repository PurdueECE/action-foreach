#########################################################
#   Author: William Jorge
#   email:  wjorgebe@purdue.edu
#   ID:     wjorgebe
#   Date:   January 16, 2021
#########################################################

import os
import sys
import re

#########################################################
# No Module-Level Variables or Statements!
# ONLY FUNCTIONS BEYOND THIS POINT!
#########################################################

def writePyramids(filePath, baseSize, count, char):
    pyramid_list = []
    for i in range(1, baseSize + 1, 2):
        pyramid_list.append((char*i).center(baseSize))

    with open(filePath, 'w') as fo:
        for i in pyramid_list:
            fo.write((' '.join([i] * count)) + '\n')

def getStreaks(sequence, letters):
    present_letters = []
    for i in list(letters):
        present_letters.append(i + '+')

    streaks = re.findall('|'.join(list(present_letters)), sequence)
    return streaks


#########################################################
# This block is optional and can be used for testing.
# We will NOT look into its content.
#########################################################

if __name__ == "__main__":
    # Write anything here to test your code.
    #writePyramids('output2.txt', 15, 5, '*')
    sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
    z1 = getStreaks(sequence, "SAQT")
    z2 = getStreaks(sequence, "OHQ")
    writePyramids('output1.txt', 13, 6, 'X')
    writePyramids('output2.txt', 15, 5, '*')
