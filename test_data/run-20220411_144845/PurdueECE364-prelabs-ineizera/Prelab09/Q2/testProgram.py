#######################################################
# Author: Insherah Neizer-Ashun 
# email: ineizera@purdue.edu 
# ID: ee364a20
# Date: 03/20/22
#######################################################
import os
import sys
import random

#######################################################
# No Module -Level Variables or Statements!
# ONLY FUNCTIONS BEYOND THIS POINT!
#######################################################

# For the fuzzing of list input ########################
def inputListFuzzer():
    randomList = []
    randomSize = random.randint(2,30)

    for i in range(1,randomSize):
        n = random.randint(1,randomSize)
        randomList.append(n)
    return randomList

def evenResult(number_list,string) :

    #function stuff
    if (string == "sum"):
        result = 0
        for i in range(len(number_list)):
            if (number_list[i] % 2) == 0:
                result += number_list[i]
        return result
    elif (string == "product") :
        result = 1
        for i in range(len(number_list)):
            if (number_list[i] % 2) == 0:
                result *= number_list[i]
        return result

#######################################################
if __name__ == "__main__":
    # Write anything here to test your code.
    randomList = inputListFuzzer()
    answer = evenResult(randomList, "product")
    print(answer)