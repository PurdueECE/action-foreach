def convertToBoolean(num, size):
    bool_list = []
    ''' Exceptions '''
    # Dealing with extreme sizes
    if type(num) == int:
        if num > 10000:
            raise ValueError('Too large a number!')
        if size > 1000:
            raise ValueError('Too large a size!')
    # Dealing with different types
    if type(num) != int:
        raise TypeError('Number (num) is not an integer!')
    if type(size) != int:
        raise TypeError('Size(size) is not an integer!')

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
