#######################################################
# Author:   William Jorge
# email:    wjorgebe@purdue.edu
# ID:       ee364b12
# Date:     March 6, 2022
# #######################################################

def getStreakProduct(sequence, maxSize, product):
    if sum(c.isdigit() for c in sequence) != len(sequence):
        raise TypeError
    combinations = []
    for i in range(len(sequence)):
        for j in range(2, maxSize+1):
            combinations.append(int(sequence[i:i+j]))
    products = []
    for i in combinations:
        temp = i
        result = 1
        while temp != 0:
            remainder = temp % 10
            result = result * remainder
            temp = temp // 10
        products.append(result)
    matches = []
    matches = [combinations[i]
               for i in range(len(combinations))
               if products[i] == product]
    distinct_matches = []
    for i in matches:
        if i not in distinct_matches:
            distinct_matches.append(str(i))

    return distinct_matches


def convertToBoolean(num, size):

    if isinstance(num, int) is False or isinstance(size, int) is False:
        return []
    num_list = list(bin(num).replace("0b", ""))
    bool_list = []
    for i in num_list:
        if i == '0':
            bool_list.append(False)
        elif i == '1':
            bool_list.append(True)
    while len(bool_list) < size:
        bool_list.insert(0, False)

    return bool_list


def convertToInteger(boolList):

    if isinstance(boolList, list) is False or len(boolList) == 0:
        return None
    for i in boolList:
        if isinstance(i, bool) is False:
            return None
    number = str()
    for i in boolList:
        if i is True:
            number += "1"
        else:
            number += "0"
    return int(number, 2)


if __name__ == "__main__":
    print(getStreakProduct('442659832034816902100484984570085172230', 10, 37))
    print(convertToBoolean(135, 12))
    print(convertToInteger([False, False, True, False, False, True]))
    print(getStreakProduct("hello", 10, 37))
