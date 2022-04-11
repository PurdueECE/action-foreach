def convertToBoolean(num, size):
    if type(num) != int:
        return []
    orig = list(str(bin(num)[2:])[::-1])
    if len(orig) > size:
        size = len(orig)
    data = [False] * size
    for i in range(size - 1, -1, -1):
        if (size - 1 - i) >= len(orig):
            return data
        if orig[size - i - 1] == '1':
            data[i] = True
        else:
            data[i] = False
    return data
