#################################
#   Author: Denny Nowak
#   Email:  nowak32@purdue.edu
#   ID:     ee364b14
#   Date:   03/02/2022
#################################
# Problem 1
def getStreakProduct(sequence, maxSize, product):
    productList = []
    seq = str(sequence)
    # Go through 2 digits to maxSize digits
    for i in range(maxSize+1)[2:]:
        for x in range(0, len(seq)-1):
            # Ignore repeats
            if (len(seq[x:x+i]) == i):
                # Check product
                prod = int(seq[x])
                for digit in seq[x+1:x+i]:
                    prod *= int(digit)
                if prod == product:
                    productList.append(seq[x:x+i])
    return productList


# Problem 2
def convertToBoolean(num, size):
    binList = []
    # Verify if positive integer
    if (isinstance(num, int) and num > 0):
        binary = bin(num)
        for i in binary[2:]:
            if (i == '1'):
                binList.append(True)
            elif (i == '0'):
                binList.append(False)
    else:
        return binList
    # Check list size
    if (len(binList) < size):
        for i in range(size-len(binList)):
            binList.insert(0, False)
    return binList


# Problem 3
def convertToInteger(boolList):
    # Verify if input is non empty list
    if (isinstance(boolList, list) and boolList != []):
        intStr = ''
        # Check if all elements are bools
        for x in boolList:
            if (not isinstance(x, bool)):
                return None
            else:
                # Convert to string
                if (x is True):
                    intStr += '1'
                elif (x is False):
                    intStr += '0'
        return int(intStr, 2)
    return None


if __name__ == '__main__':
    # print(getStreakProduct(14822,3,32))
    # print(getStreakProduct(54789654321687984, 9, 288))
    # print(convertToBoolean(9,3))
    # print(convertToBoolean(135,12))
    # print(convertToInteger([True, False, False, False, False, True, True, True]))
    # print(convertToInteger([False, False, True, False, False, True]))
    pass
