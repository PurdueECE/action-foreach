

def getStreakProduct(sequence, maxSize, product):
    prodeq = []     # final thing to return
    prodeqplace = []

    for size in range(2, maxSize+1, 1):  # increments for from 2 to maxsize //for item in items 
        # print(size)
        searchIndex = 0
        maxSearchIndex = len(sequence) - size  # thingy has 3 things in it so we need to stop 3 before max index
        # print("Searching from ", searchIndex, " to ", maxSearchIndex, ", size is ", size)
        for i in range(maxSearchIndex+1):
            # print(searchIndex, i)
            result = 1
            # now we know the starting index and have size. get the product.
            for x in range(searchIndex, searchIndex + size, 1):  # x is now 0 1, 1 2, 2 3, 3 4 etc.
                result = int(result) * int(sequence[x])
                # print(x)
            # print(result)

            if result == product: #use is instead of ==
                seqSection = sequence[searchIndex:searchIndex+size]
                prodeq.append(seqSection)
                prodeqplace.append(searchIndex)
                # print(seqSection, result)
            searchIndex = searchIndex + 1
        # print(result, sequence[i:i+size])

    # now we reorder prodeq based on prodeqplace
    Z = [prodeq for _, prodeq in sorted(zip(prodeqplace, prodeq))]

    # print(sequence[1])
    # print(prodeqplace)
    # print(Z)
    return Z


def convertToBoolean(num, size):
    if isinstance(num, int) & isinstance(size, int):
        boolarr = []
    else:
        return []

    binary = str(bin(num))
    binary = binary.split("b", 1)[1]

    for x in binary:
        if x == str(1):
            boolarr.append(bool(1))
        else:
            boolarr.append(bool(0))
        # print(x)

    # print("owo", )
    sizediff = size-len(boolarr)

    for x in range(sizediff):
        boolarr.insert(0, bool(0))
        # print("hi")

    return boolarr


def convertToInteger(boolList):
    if isinstance(boolList, list) is False:
        return None

    for i in boolList:
        if isinstance(i, bool) is False:
            return None

    if not boolList:
        return None

    finalInt = 0
    listLen = len(boolList)-1

    n = 0
    for i in range(listLen, -1, -1):
        # print(i)
        if boolList[i] is True:
            # print("i: ", i, " finalInt: ", finalInt, " n: ", n)
            finalInt = finalInt + (2**n)
            # print(finalInt)
        n = n+1

    return int(finalInt)

# getSquared([1,2])
# testGreaterThan10(12)
# getExponential(2, 3)

# bList = [False, False, True, False, False, True]
# print(convertToInteger(bList))
# bList = [True, False, False, False, False, True, True, True]
# # bList = 'asdf'
# print(convertToInteger(bList))
# print(type(convertToInteger(bList)))

# input = "23876543703213534643"
# print(getStreakProduct(input, 7, 69)) #should return 148, 48, 822

# print(convertToBoolean('1asdf35', 12))
# print(convertToBoolean(9, 3)) #should return [True, False, False, True]
