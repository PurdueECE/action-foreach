import random

'''
Fuzzing - https://en.wikipedia.org/wiki/Fuzzing
Originated in 1988 (Prof. Barton Miller). Caused 25% - 33% of UNIX based Utilities to crash.
'''
'''
Random Input
    Malformed input with random data
    ASCII Table: https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
'''
def fuzzer(max_length = 100, char_start = 32, char_range = 32):
    string_length = random.randrange(0, max_length + 1)
    out = ""
    for i in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out


print(fuzzer())
print(fuzzer())
def buffer_size_check(s):
    buffer_size = 20
    if len(s) > buffer_size:
        raise OverflowError

trials = 10
for i in range(trials):
    size = fuzzer()
    try:
        buffer_size_check(size)
    except OverflowError as err: #Throws Errors but does not crash the program
        print(f"Overflow error for input {size}")
        continue


'''
Grammar based Fuzzing
    Define fuzzy inputs based on some predetermined grammar (Eg: Program that checks for input size before executing)
'''
def grammar_fuzzer(extra_length = 5, char_start = 33, char_range = 14):
    out = ''.join((random.choice('1234567890') for i in range(5)))
    for i in range(0, extra_length):
        out += chr(random.randrange(char_start, char_start + char_range)) #Fuzzy inputs always are of size 10 but contains invalid characters
    return out

print(grammar_fuzzer())
print(grammar_fuzzer())

def grammar_test_program(number):
    input_size = 10
    if len(number) > input_size:
        raise OverflowError
    else:
        exponent = int(number)**2
    return exponent

trials = 10
for i in range(trials):
    input = grammar_fuzzer()
    try:
        grammar_test_program(input)
    except ValueError as err: #Throws Errors but does not crash the program
        print(f"Value error for input {input}")
        continue
    except OverflowError as err:
        print(f"Overflow error for input {input}")
        continue


'''
Out of bounds fuzzing
    Input exponentially growing data of right type to a program causing the program to hang leading to DoS(Denial of Service).
    Use of timers to exit if execution time exceeds threshold
'''
def out_of_bounds_fuzzer(extra_length = 5, char_start = 49, char_range = 8):
    out = ''.join((random.choice('1234567890') for i in range(5)))
    for i in range(0, extra_length):
        out += chr(random.randrange(char_start, char_start + char_range)) #Fuzzy inputs always are of size 10 but contains invalid characters
    return out

print(out_of_bounds_fuzzer())
print(out_of_bounds_fuzzer())

def out_of_bounds_test_program(number):
    exponent = int(number)**2
    return exponent

trials = 100
for i in range(trials):
    input = out_of_bounds_fuzzer(i**5)
    try:
        print(out_of_bounds_test_program(input))
    except ValueError as err: #Throws Errors but does not crash the program
        print(f"Value error for input {input}")
        continue
    except OverflowError as err:
        print(f"Overflow error for input {input}")
        continue