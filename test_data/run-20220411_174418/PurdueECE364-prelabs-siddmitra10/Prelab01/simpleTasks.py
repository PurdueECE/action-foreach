#######################################################
# Author:
# email:
# ID:
# Date: 
# #######################################################
# import os  # List of module import statements 
# import sys # Each one on a line
import re
####################################################### 
# # No Module -Level Variables or Statements!
# ONLY FUNCTIONS BEYOND THIS POINT! 
# #######################################################

def writePyramids(filePath, baseSize, count, char):
    with open(filePath, 'w') as file:
        # file.write("Hi")
        pMid = int((baseSize + 1) / 2)
        offset = 0
        rows = pMid
        pyramid = ""
        print(pMid)
        for i in range(1, pMid+1):
            printed = 0
            for j in range(rows - i):
                # file.write(" ")
                pyramid += " "
                printed += 1
            for j in range(i + offset):
                # file.write(char)
                pyramid += char
                printed += 1
            offset += 1
            # file.write(f'\n')
            for j in range(baseSize - printed):
                pyramid += " "
            pyramid += f'\n'
        # print(pyramid) 
        for line in pyramid.split('\n'):
            # file.write(line * count)
            for i in range(count):
                file.write(line)
                if i != count - 1:
                    file.write(" ")
            file.write(f'\n')

    file = open(filePath, 'r')
    data = file.readlines()
    file.close()
    
    with open(filePath, 'w') as file:
        file.writelines(data[:-1])

    pass


def getStreaks(sequence, letters):
    
    data = [char for char in letters]

    pattern = r'(([a-zA-z])\2*)'
    matches = re.findall(pattern, sequence)

    finalAns = []
    for match in matches:
        if match[1] in data:
            finalAns.append(match[0])

    return finalAns
    
# This block is optional and can be used for testing.
# We will NOT look into its content. 
# ####################################################### 
if __name__ == "__main__":
    # Write anything here to test your code. 
    # writePyramids("./test.txt", 13, 6, 'X')
    # print(getStreaks("AAASSSSSSAPPPSSPPBBCCCSSS", "PAZ"))
    pass