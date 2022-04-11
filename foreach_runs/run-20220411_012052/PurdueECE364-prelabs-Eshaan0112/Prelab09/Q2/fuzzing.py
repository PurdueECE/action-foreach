from random import random
from convertToBoolean import convertToBoolean
import sys
import string


def fuzzer():
    # Test 1 -> Extreme numbers
    maximum = sys.maxsize
    num = random.randint(0, maximum)
    size = random.randint(0, maximum)
    bool_list = convertToBoolean(num, size)
    print(f'Extreme numbers test -> bool_list = {bool_list}')

    # Test 2 -> Passing random strings
    num = string.ascii_lowercase
    size = string.ascii_lowercase
    bool_list = convertToBoolean(num, size)
    print(f'Passing strings test -> bool_list = {bool_list}')

    # Test 3 -> Passing random Lists
    num = random.sample(range(10, 30), 5)
    size = random.sample(range(10, 30), 5)
    bool_list = convertToBoolean(num, size)
    print(f'Passing lists test -> bool_list = {bool_list}')


if __name__ == "__main__":
    fuzzer()
