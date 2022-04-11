import random


# Test function
def convertToBoolean(num, size):

    if isinstance(num, int) & isinstance(size, int):
        boolarr = []
    else:
        return []

    binary = str(bin(num))
    # print(binary)
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


def testString(string_length):
    char_start = 32
    char_range = 32
    out = ""
    for i in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))

    try:
        convertToBoolean(out)
    except TypeError:  # Throws Errors but does not crash the program
        print(f"Type error for input {out}")
    return


def testArr(string_length):
    char_start = 32
    char_range = 32
    outarr = []
    for i in range(0, string_length):
        # out=""
        out = chr(random.randrange(char_start, char_start + char_range))
        outarr.append(out)
    try:
        convertToBoolean(outarr)
    except TypeError:  # Throws Errors but does not crash the program
        print(f"Type error for input {outarr}")
    return


def testFloat(string_length):
    out = random.uniform(-string_length, string_length)
    try:
        convertToBoolean(out)
    except TypeError:  # Throws Errors but does not crash the program
        print(f"Type error for input {out}")
    return


def testBools(string_length):
    out = bool(random.getrandbits(1))
    try:
        convertToBoolean(out)
    except TypeError:  # Throws Errors but does not crash the program
        print(f"Type error for input {out}")
    return


def testToups(string_length):
    out = bool(random.getrandbits(1))
    out2 = bool(random.getrandbits(1))
    boolout = (out, out2)
    try:
        convertToBoolean(boolout)
    except TypeError:  # Throws Errors but does not crash the program
        print(f"Type error for input {boolout}")
    return


def fuzzer(length):
    max_length = 100

    for i in range(length):
        string_length = random.randrange(0, max_length + 1)
        print(string_length)
        testString(string_length)
        testArr(string_length)
        testFloat(string_length)
        testBools(string_length)
        testToups(string_length)
    return "Success"


fuzzer(10000)
