#######################################################
#   Author: Aakash Sivasankar
#   email: sivasank@purdue.edu
#   ID: ee364b15
#   Date: 01/14/2022
#######################################################

import os   # List of module import statement
import sys  # Each one on a line

#######################################################
# No Module -Level Variables or Statements!
# ONLY FUNCTIONS BEYOND THIS POINT!
#######################################################

def writePyramids(filePath, baseSize, count, char):
    f = open(filePath, 'w')

    i = 0
    space = int((baseSize - 1) / 2)

    while i < baseSize:
        for j in range(count):
            for k in range(0, space):
                f.write(" ")

            for x in range(0, i + 1):
                f.write(char)

            for y in range(0, space):
                f.write(" ")

            if j + 1 != count:
                f.write(" ")

        f.write("\n")

        space = space - 1
        i = i + 2

    f.close()

def getStreaks(sequence, letters):
    newL = []
    strng = ""
    i = 0

    for i in range(len(sequence)):
        for j in range(len(letters)):
            if sequence[i] == letters[j]:
                if strng == "":
                    strng += str(sequence[i])

                elif(sequence[i - 1] == sequence[i]):
                    strng += str(sequence[i])

                else:
                    newL.append(strng)
                    strng = sequence[i]

        if strng != "" and i == len(sequence) - 1:
            newL.append(strng)

    print(newL)

# This block is optional and can be used for testing.
# We will NOT look into its content.
#######################################################
#if __name__ == "__main__":
    # Write anything here to test your code.