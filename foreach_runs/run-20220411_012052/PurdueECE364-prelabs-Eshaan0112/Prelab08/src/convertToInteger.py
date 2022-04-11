def convertToInteger(boolList):
    if type(boolList) != list:  # Check if it is a list
        return None
    if len(boolList) == 0:  # Check if list is empty
        return None
    bool_str = ''
    for value in boolList:
        if type(value) == bool:  # Check if values are bool
            if value:
                bool_str += '1'
            else:
                bool_str += '0'
        else:
            return None
    val = int(bool_str, 2)
    return val


if __name__ == "__main__":
    bList = ["1", "2"]
    print(convertToInteger(bList))
