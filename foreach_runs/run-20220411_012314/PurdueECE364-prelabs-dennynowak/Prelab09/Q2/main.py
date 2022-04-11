#################################
#   Author: Denny Nowak
#   Email:  nowak32@purdue.edu
#   ID:     ee364b14
#   Date:   03/11/2022
#################################
import random


# Test Function from Prelab08
def getStreakProduct(sequence, maxSize, product):
    productList = []
    seq = str(sequence)
    # Error handling code for sequence input
    for digit in seq:
        try:
            int(digit)
        except ValueError:
            print("Incorrect input for sequence!")
            raise ValueError
    # Error handling code for maxSize input
    if type(maxSize) != int:
        print("Incorrect input for maxSize!")
        raise TypeError
    # Go through 2 digits to maxSize digits
    for i in range(maxSize+1)[2:]:
        for x in range(0, len(seq)-1):
            # Ignore repeats
            if (len(seq[x:x+i]) == i):
                # Check product
                prod = int(seq[x])
                for digit in seq[x+1:x+i]:
                    prod *= int(digit)
                if prod == product:
                    productList.append(seq[x:x+i])

    return productList


# Fuzzer program for value / type errors
def fuzzer(extra_length=5, char_start=33, char_range=14):
    out = ''.join((random.choice('1234567890') for i in range(5)))
    for i in range(0, extra_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out


if __name__ == '__main__':
    # Demonstrations for Problem 2
    fuzz = fuzzer()
    try:
        print(getStreakProduct(fuzz, 3, 32))
    except ValueError:
        print(f"Value error for input sequence: {fuzz}")
    fuzz2 = fuzzer()
    try:
        print(getStreakProduct(14822, fuzz2, 32))
    except TypeError:
        print(f"Type error for input maxSize: {fuzz2}")
    pass
