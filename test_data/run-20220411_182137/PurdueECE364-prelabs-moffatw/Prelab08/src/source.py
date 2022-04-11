from xmlrpc.client import Boolean


def getStreakProduct(sequence, maxSize, product):

    return_list = []

    for i in range(len(sequence)):
        for j in range(2, maxSize + 1):
            if ((i + j) > len(sequence)):
                continue

            sub_sequence = sequence[i:i + j]

            calc_product = 1

            for char in sub_sequence:
                calc_product = calc_product * int(char)

            if (calc_product == product):
                return_list.append(sub_sequence)

    return return_list


def convertToBoolean(num, size):

    if (isinstance(num, int) is False):
        return []

    if (isinstance(size, int) is False):
        return []

    return_list = [None] * size
    binary = str(format(num, "b"))

    for i in range(len(binary)):
        if (i < size):
            if (binary[i] == "1"):
                return_list[i] = True
            else:
                return_list[i] = False
        else:
            if (binary[i] == "1"):
                return_list.append(True)
            else:
                return_list.append(False)

    return return_list


def convertToInteger(boolList):

    if (isinstance(boolList, list) is False):
        return None

    for element in boolList:
        if (isinstance(element, Boolean) is False):
            print("element is not boolean")
            return None

    if (len(boolList) == 0):
        print("empty list")
        return None

    return_string = ""

    for bool in boolList:
        if (bool is True):
            return_string = return_string + "1"
        else:
            return_string = return_string + "0"

    return int(return_string, 2)
