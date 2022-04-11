#######################################################
# Author: <Kevin Mi>
# email: <mi2@purdue.edu>
# ID: <ee364b07>
# Date: <1/16/2022>
#######################################################
import os # List of module import statements
import sys # Each one on a line
#######################################################
# No Module -Level Variables or Statements!
# ONLY FUNCTIONS BEYOND THIS POINT!
#######################################################

def writePyramids(filePath, baseSize, count, char):
    pyra = []
    spaces = 0
    while baseSize >= 1:
        build = (" " * spaces) + (char * baseSize) + (" " * spaces)
        pyra.append(build)
        baseSize -= 2
        spaces += 1
    pyra.reverse()
    with open(filePath, 'w') as f:
        for l in pyra:
            line = (l + " ") * count
            f.write(line[0:len(line) - 1] + '\n')

def getStreaks(sequence, letters):
    res = []
    letters = set([l for l in letters])
    i = 0
    while i < len(sequence):
        if sequence[i] in letters:
            streak = sequence[i]
            while i + 1 < len(sequence) and sequence[i+1] == sequence[i]:
                i += 1
                streak += sequence[i]
            res.append(streak)
        i += 1
    return res

# This block is optional and can be used for testing.
# We will NOT look into its content.
#######################################################
if __name__ == "__main__":
# Write anything here to test your code.
    writePyramids('test13.txt', 13, 6, 'X')
    writePyramids('test15.txt', 15, 5, '*')
    sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
    print(getStreaks(sequence, "SAQT"))
    print(getStreaks(sequence, "PAZ"))
