# ######################################################
# Author : Lingyue Christine Fang
# email : fang245@purdue.edu
# ID : ee364b09
# Date : January 14, 2022
# ######################################################

import os
import sys

def writePyramids(filePath, baseSize, count, char):
    pyramid = []
    rows = int(baseSize/2+1)
    mid = 1
    space = int(baseSize /2)
    for k in range(rows):
        for i in range(count):
            for j in range(space):
                pyramid.append(" ")
            for j in range(mid):
                pyramid.append(char)
            for j in range(space):
                pyramid.append(" ")
            if i != count - 1:
                pyramid.append(" ")
        pyramid.append("\n")
        mid = mid + 2
        space = space - 1

    with open (filePath, 'w') as fp:
        for i in pyramid:
            fp.write("%s" % i)

def getStreaks(sequence, letters):
    streak = []
    char = sequence[0]
    string = char

    for i in range(1,len(sequence)):
        if sequence[i] != char:
            for j in range(len(letters)):
                if char == letters[j]:
                    streak.append(string)
            char = sequence[i]
            string = char
        else:
            string = string + char
        if i == len(sequence) - 1:
            for j in range(len(letters)):
                if char == letters[j]:
                    streak.append(string)
    return streak


if __name__ == "__main__":
    writePyramids('pyramid1.txt',15,5,'*')

    sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
    z = getStreaks(sequence, "ZQR")
    for i in z:
        print(i)
