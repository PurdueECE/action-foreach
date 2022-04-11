def getStreakProduct(sequence, maxSize, product):
    seq = str(sequence)
    outlist = []
    for i in range(len(seq)):
        tmp = seq[i]
        num = seq[i]
        if (i + maxSize) > len(seq):
            up = len(seq)
        else:
            up = (i + maxSize)
        for j in range(i+1, up):
            num = num + seq[j]
            tmp = int(tmp) * int(seq[j])

            if tmp == product:
                outlist.append(num)
    return outlist


def convertToBoolean(num, size):
    out = []
    if type(num) is not int:
        return out
    binval = str(format(num, "b"))
    if len(binval) < size:
        for j in range(size - len(binval)):
            out.append(False)

    for i in range(len(binval)):
        if binval[i] == '1':
            out.append(True)
        else:
            out.append(False)
    return out


def convertToInteger(boolList):
    if type(boolList) != list:
        return None
    for i in range(len(boolList)):
        if (boolList[i] is not True) & (boolList[i] is not False):
            return None

    if boolList:
        blist = '0'
        for j in range(len(boolList)):
            if boolList[j] is True:
                blist = blist + '1'
            elif boolList[j] is False:
                blist = blist + '0'
        binval = int(blist, 2)
    else:
        return None
    return binval


if __name__ == "__main__":
    print(getStreakProduct(43349443349433493343349, 7, 324))
    print(convertToBoolean(9, 12))
    bList = [True, False]
    print(convertToInteger(bList))
