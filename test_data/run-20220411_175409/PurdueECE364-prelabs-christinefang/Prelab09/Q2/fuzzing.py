import random


def convertToBoolean(num, size):
    out = []
    if type(num) is not int:
        return out
    if size > 150:
        raise OverflowError
    else:
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


def fuzzer(extra_length=100, char_start=49, char_range=9):
    string_length = random.randrange(0, extra_length + 1)
    out = ''.join((random.choice('1234567890') for i in range(string_length)))
    for i in range(0, extra_length):
        # Fuzzy inputs always are of size 10 but contains invalid characters
        out += chr(random.randrange(char_start, char_start + char_range))
    return out


def grammar_fuzzer(extra_length=10, char_start=33, char_range=14):
    out = ''
    for i in range(0, extra_length):
        out += chr(random.randrange(char_start, char_start + char_range))
        return out


def list_fuzzer(extra_length=10, char_start=49, char_range=14):
    out = []
    for i in range(0, extra_length):
        out.append(chr(random.randrange(char_start, char_start + char_range)))
        return out


trials = 3
for i in range(trials):
    inputg1 = grammar_fuzzer()
    try:
        convertToBoolean(int(inputg1), len(inputg1))
    except ValueError:
        print(f"Value error for input1 {inputg1}")
        continue
    except TypeError:
        print(f"Type error for input1 {inputg1}")
        continue


trials = 3
for i in range(trials):
    inputl1 = list_fuzzer()
    try:
        convertToBoolean(int(inputl1), len(inputl1))
    except ValueError:
        print(f"Value error for input1 {inputl1}")
        continue
    except TypeError:
        print(f"Type error for input1 {inputg1}")
        continue
