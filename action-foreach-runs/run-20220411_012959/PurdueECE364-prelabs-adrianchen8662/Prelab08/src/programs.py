def getStreakProduct(sequence, maxSize, product):
    # generate empty arrays
    arr = [1]
    arr.remove(1)
    arrtest = [1]
    arrtest.remove(1)

    # convert sequence to array of ints
    intarr = [int(x) for x in str(sequence)]

    # generate combinations of sequential numbers with lengths less than or equal to maxSize
    for i in range(1,maxSize+1):
        for r in range(len(intarr)-i+1):
            arrpart = intarr[r:r+i]
            arrtest.append(arrpart)
            
    # multiply subarrays and compare
    for i in arrtest:
        prod = 1
        for x in i:
            prod *= x
        if prod == product:
            arr.append(int("".join([str(integer) for integer in i])))

    return arr

def convertToBoolean(num,size):
    # prevents non-int inputs
    if not isinstance(num,int) or not isinstance(num,int):
        arr = [1]
        arr.remove(1)
        return arr

    # convert num into an array of bits
    binaryarr = [int(x) for x in str(format(num,"b"))]

    # substitute for boolean values
    for i in range(len(binaryarr)):
        if binaryarr[i] == 0:
            binaryarr[i] = False
        else:
            binaryarr[i] = True

    # pad bits
    if len(binaryarr) < size:
        for i in range(0,size - len(binaryarr)):
            binaryarr.insert(0,False)
    
    return binaryarr

def convertToInteger(boolList):
    if not type(boolList) == list:
        return None

    for i in boolList:
        if not type(i) == bool:
            return None

    if len(boolList) == 0:
        return None

    # convert boolean list to 1's and 0's
    for i in range(len(boolList)):
        if boolList[i] == True:
            boolList[i] = 1
        if boolList[i] == False:
            boolList[i] = 0

    # convert list of ints to int
    intoutput = int("".join([str(integer) for integer in boolList]),2)
    return intoutput

def writeSomething():
    with open('testrun.txt','a+') as f:
        print("")