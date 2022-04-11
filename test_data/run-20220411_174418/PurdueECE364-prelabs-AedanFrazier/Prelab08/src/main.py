##########################################################
# Author    :   Aedan Frazier
# Email     :   frazie35@purdue.edu
# ID        :   ee364a06
# Date      :   3/1/2022
##########################################################


def getStreakProduct(sequence, maxsize, product):
    products = []
    substrs = []
    i = 0
    while(i <= len(sequence)):
        for size in range(2, maxsize + 1):
            c = ""
            for j in range(0, size):
                if(i + j >= len(sequence)):
                    c = None
                else:
                    c = c + sequence[i + j]
            if(c):
                substrs.append(c)
        i = i + 1
    for sub in substrs:
        p = 1
        for dig in sub:
            p = p * int(dig)
        if(p == product):
            products.append(sub)
    return products


def convertToBoolean(num, size):
    binary = []

    if(type(num) != int):
        print("num is not an int")
        return binary
    if(type(size) != int):
        print("size is not an int")
        return binary

    while(num > (2 ** size)):
        size += 1

    for i in range(size, 0, -1):
        if((num - (2 ** (i - 1))) >= 0):
            binary.append(1)
            num = num - (2 ** (i - 1))
        else:
            binary.append(0)
    bools = []
    for n in binary:
        if(n and 1):
            bools.append(True)
        else:
            bools.append(False)
    return bools


def convertToInteger(boolList):
    if(type(boolList) != list):
        print("boolList is not a list!")
        return None
    if(len(boolList) == 0):
        print("boolList is empty!")
        return None

    decimal = 0
    size = len(boolList) - 1
    for i in boolList:
        if(type(i) != bool):
            print("List does not contain all bools!")
            return None
        if(i):
            decimal = decimal + (2 ** size)
        size = size - 1
    return decimal


if __name__ == "__main__":
    print(getStreakProduct("14822", 3, 32))
    print(convertToBoolean(4, 4))
    print(convertToInteger([False, True, False, False]))
