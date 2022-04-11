def convertToInteger(boolList):
    if type(boolList) != list or len(boolList) == 0:
        return None
    sum = 0
    for i in range(len(boolList) - 1, -1, -1):
        if boolList[len(boolList) - 1 - i] is True:
            # print(2**i)
            sum += 2**(i)
        elif type(boolList[len(boolList) - 1 - i]) != bool:
            return None
    return sum
