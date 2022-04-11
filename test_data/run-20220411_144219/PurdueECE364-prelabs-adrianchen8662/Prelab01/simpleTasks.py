# ######################################################
# Author : Adrian Chen
# email : chen3124@purdue.edu
# ID : ee364b10
# Date : 1/13/2022
# ######################################################

import math

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

# assumes that baseSize is odd
def writePyramids(filepath, baseSize, count, char):
    f = open(filepath,"w")
    second = 1
    while baseSize > 0:
        test = math.floor(baseSize / 2)
        for i in range(count):
            for x in range(test):
                f.write(" ")
            for x in range(second):
                f.write(char)
            for x in range(test):
                f.write(" ")
            if i != count-1:
                f.write(" ")
        f.write("\n")
        baseSize -= 2
        second += 2
    f.close()

def getStreaks(sequence, letters):
    output = []
    counter = 0
    character = ''
    i = 0
    while i < len(sequence):
        x = 0
        while x < len(letters):
            if i < len(sequence) and sequence[i] == letters[x]:
                character = sequence[i]
                counter = 0
                if (sequence[i-1] == character):
                    counter=1
                while (i < len(sequence) and sequence[i] == letters[x]):
                    counter+=1
                    i+=1
                output.append(counter * character)
            x+=1
        i+=1
    return output