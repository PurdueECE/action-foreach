from random import randint


def alphanumericFuzzer():
    size = randint(0, 50)
    testcase = ""
    for i in range(0, size):
        testcase += chr(randint(33, 126))
    return testcase


def numericFuzzer():
    size = randint(0, 50)
    testcase = ""
    for i in range(0, size):
        testcase += chr(randint(48, 57))
    return testcase
