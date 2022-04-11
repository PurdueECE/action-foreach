# ######################################################
# Author : Adrian Chen
# email : chen3124@purdue.edu
# ID : ee364b10
# Date : 3/19/2022
# ######################################################

import random
import string
import multiprocessing
import time

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

# original getStreaks function, taken from Prelab 01
def getStreaks(sequence, letters):
    output = []
    counter = 0
    character = ''
    i = 0
    while i < len(sequence):
        x = 0
        while x < len(letters):
            if i < len(sequence) and sequence[i] == letters[x]:
                character = sequence[i]
                counter = 0
                if (sequence[i-1] == character):
                    counter=1
                while (i < len(sequence) and sequence[i] == letters[x]):
                    counter+=1
                    i+=1
                output.append(counter * character)
            x+=1
        i+=1
    return output

def randomfuzzer():

    poslarge = 1000000000
    neglarge = -1000000000

    type = random.randrange(0,4,1)
    if type == 0: # return a random int
        return random.randrange(neglarge,poslarge,1) 
    elif type == 1: # return a random float
        return random.uniform(neglarge,poslarge)
    elif type == 2: # return a randomly sized list of random floats
        size = random.randrange(0,100,1) # limited to speed up inputs
        returnList = []
        for i in range(size):
            returnList.append(random.randrange(neglarge,poslarge,1))
        return returnList
    elif type == 3: # return a random string of random length
        size = random.randrange(0,100,1)
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))
    return

def outofboundsfuzzer(size):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))

if __name__ == '__main__':
    trials = 100
    for i in range(trials):
        sequence = randomfuzzer()
        letters = randomfuzzer()
        try:
            getStreaks(sequence, letters)
        except TypeError as err:
            print(f"Type error for input {sequence}, {letters}")
    trials = 21
    for x in range(1,trials,1):
        sequence = outofboundsfuzzer(x**5)
        letters = outofboundsfuzzer(x**5)
        try:
            p = multiprocessing.Process(target=getStreaks,name="getStreaks",args=(sequence, letters))
            p.start()
            p.join(10)
            print(x)
            if p.is_alive():
                print(f"Timeout error for input size {len(sequence)}, {len(letters)}")
                p.kill()
        except ValueError as err:
            print(f"Value error for input of size {len(sequence)}, {len(letters)}")
            continue