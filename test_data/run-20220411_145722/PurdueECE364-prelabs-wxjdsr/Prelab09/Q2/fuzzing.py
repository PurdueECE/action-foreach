# ######################################################
# Author :  Xingjian Wang
# email :   wang5066@purdue.edu
# ID:       ee364b03
# Date :    Mar 6, 2022
# ######################################################

import random
from Lab01Module import *


# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
def fuzzer(max_length=100, char_start=32, char_range=32):
    string_length = random.randrange(0, max_length + 1)
    out = ""
    for i in range(0, string_length):
        out += chr(random.randrange(
            char_start, char_start + char_range))
    return out


# Test for evenResult() in Lab01Module.py
trials = 10
for i in range(trials):
    size = fuzzer()
    try:
        evenResult(size, "sum")
    except OverflowError as err:  # Throw error but does not crash the program
        print(f"Overflow error for input {size}")
        continue
