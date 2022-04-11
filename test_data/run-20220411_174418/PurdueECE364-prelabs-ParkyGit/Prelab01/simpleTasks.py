#######################################################
# Author: Erin Park
# email: Park1131@purdue.edu
# ID: ece364a05
# Date: 01/15/2022
#######################################################
from math import floor
import os # List of module import statements
import sys # Each one on a line
#######################################################
# No Module -Level Variables or Statements!
# ONLY FUNCTIONS BEYOND THIS POINT!
#######################################################
#def functionName1(a: float , b: float) -> float:
#return 0.
#def functionName2(c: str , d: str) -> int:
#return 1
def writePyramids(filePath, baseSize, count, char):
    #1. File name
    #2. Number of lines
    #3. How many pyramids
    #4. Character
    # Plan: make file, write line by line. 
    with open(filePath, 'w') as f:
        #now we make a string thingy then f.write OwO
        #BTW, even numbers can't form a pyramid that's wack
        unitsize = baseSize + int(1)
        midpoint = floor(unitsize/2)-1 #so if unitsize is 3+1 = 4, midpoint is at 2, the 2nd character
        linecount = int((int(baseSize)+1)/2)
        shelfsize = int(1) #How many characters to do. starts at 1, goes 3 5 7 etc

        
        for i in range(linecount):
            unit = ""
            #First, we construct the first unit (unit is my term for one line of one pyramid)
            for x in range(midpoint):
                unit = unit + " "
            for x in range(shelfsize):
                unit = unit + char
            for x in range(midpoint):
                unit = unit + " "
            
            #before sending newline, we want to sneak in more units based on count value
            oneunit = unit
            for x in range(count-1):
                unit = unit + " "
                unit = unit + oneunit
            
            unit += "\n"
            #update trackers
            shelfsize += 2
            midpoint -= 1
            f.write(unit)
    return
def getStreaks(sequence, letters):
    result = []
    seq = ""
    sequence += " "
    for i in range(len(sequence)-1):          #iterate thru sequence AAAABBBEE
        for x in range(len(letters)):       #iterate through query
            if sequence[i] == letters[x]:   #if match;
                seq += sequence[i]
            if (seq != "") & (sequence[i] != sequence[i+1]):
                result.append(seq)
                # result.append(sequence[i]+sequence[i+1]+str(i)+str(x)+sequence[i] + letters[x])
                seq = ""
    #hotfix, I cant figure it out but this works lol?
    result[0] = result[0]+result[1]
    result.remove(result[1])

    print(result)
    return result
# This block is optional and can be used for testing.
# We will NOT look into its content.
#######################################################
if __name__ == "__main__":
    sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
    # # sequence = "AAASASSB"
    getStreaks(sequence, "SAQT")
    # print ("['AAA', 'SSSSSS', 'A', 'SS', 'SSS']")
    getStreaks(sequence, "PAZ")
    # print ("['AAA', 'A', 'PPP', 'PP']")
    