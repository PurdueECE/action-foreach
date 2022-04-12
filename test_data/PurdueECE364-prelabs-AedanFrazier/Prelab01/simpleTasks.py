#######################################################
# Author : Aedan Frazier
# email : frazie35@purdue.edu
# ID : ee364a06
# Date : 1/14/22
#######################################################

##IMPORTS

#######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
#######################################################

def writePyramids(filePath: str, baseSize: int, count: int, char: str) -> None:
    file = open(filePath, "w")
    pyramid = ""
    height = int(baseSize/2) + 1
    for i in range(0,height):
        for j in range(0, count):
            if(j == count -1):
                pyramid = pyramid + " " * (int(baseSize/2)-i) + (char * i) + char + (char * i) + " " * int((baseSize/2) - i)
            else:
                pyramid = pyramid + " " * (int(baseSize/2)-i) + (char * i) + char + (char * i) + " " * int((baseSize/2) - i + 1)
        pyramid = pyramid + "\n"
    file.write(pyramid)
    file.close()
    return

def getStreaks(sequence: str, letters: str) -> list:
    streak = ""
    listOfStreaks = []
    for char in sequence:
        if(char in letters):
            if(len(streak) == 0):
                streak = streak + char
            elif(char in streak):
                streak = streak + char
            else:
                listOfStreaks.append(streak)
                streak = "" + char
        else:
            if(len(streak) != 0):
                listOfStreaks.append(streak)
                streak = ""
    if(len(streak) != 0):
        listOfStreaks.append(streak)
        streak = ""

    return listOfStreaks


# This block is optional and can be used for testing .
# We will NOT look into its content .
#######################################################
if __name__ == "__main__":  
    writePyramids("pyramids13_test.txt", 13, 6, 'X')
    writePyramids("pyramids15_test.txt", 15, 5, '*')
    sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
    getStreaks(sequence, "SAQT")
    getStreaks(sequence, "PAZ")

