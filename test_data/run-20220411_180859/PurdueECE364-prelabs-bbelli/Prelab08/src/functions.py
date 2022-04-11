

def getStreakProduct(sequence, maxSize, product):
    current_product = 1
    current_streak = ""
    streaks = []

    for i in range(len(sequence)):
        for s in range(0, maxSize):
            index = i + s
            if (index <= len(sequence)-1):
                current_product = current_product * int(sequence[index])
                current_streak = current_streak + str(sequence[index])
                if(current_product == product):
                    streaks.append(current_streak)
        current_product = 1
        current_streak = ""

    return streaks


def convertToBoolean(num, size):
    binary_list = []

    if(int(num) != num):
        return binary_list

    binary_num = bin(num)[2:]
    binary = str(binary_num)

    for bit in binary:
        if(int(bit) == 0):
            binary_list.append('False')
        elif(int(bit) == 1):
            binary_list.append('True')
        else:
            binary_list = []
            return binary_list

    return binary_list


def convertToInteger(boolList):
    binary_string = ""
    if not boolList:
        return None
    if not isinstance(boolList, list):
        return None

    for bit in boolList:
        if(bit == 'True'):
            binary_string = binary_string + '1'
        elif(bit == 'False'):
            binary_string = binary_string + '0'
        else:
            return None
    int_num = int(binary_string, 2)

    return int_num
# if __name__ == '__main__':
#     sequence = "134235245234195234545478945645261"
#     print(getStreakProduct(sequence, 6, 419))
#     a = (convertToBoolean(112312321,100))
#     print(a)
#     b = convertToInteger(a)
#     print(b)
