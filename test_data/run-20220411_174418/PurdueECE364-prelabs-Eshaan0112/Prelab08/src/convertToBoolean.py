def convertToBoolean(num, size):
    bool_list = []
    if type(num) != int:
        return bool_list
    if type(size) != int:
        return bool_list
    binary = str(bin(num)[2:])
    for i in binary:
        if int(i) == 1:
            bool_list.append(True)
        else:
            bool_list.append(False)
    if len(bool_list) < size:
        while len(bool_list) != size:
            bool_list.insert(0, False)
    return bool_list


if __name__ == "__main__":
    print(convertToBoolean(135, 12))
