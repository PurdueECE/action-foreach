######################################
# Author: Aedan Frazier
# Email : frazie35@purdue.edu
# ID    : ee364a06
# Date  : 3/10/2022
######################################

from simpleTasks import getStreaks
from random import choice
from random import randrange


def fuzz_st():
    size = randrange(1, 100)
    choices = '0123456789'
    choices = choices + 'abcdefghijklmnopqrstuvwxyz'
    choices = choices = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    r = ''.join((choice(choices) for i in range(size)))
    return r


def fuzz_seq():
    size = randrange(1, 5)
    choices = '0123456789'
    choices = choices + 'abcdefghijklmnopqrstuvwxyz'
    choices = choices = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    r = ''.join((choice(choices) for i in range(size)))
    return r


if __name__ == "__main__":
    trials = 500
    for i in range(0, trials):
        st = ''
        streak = ''
        try:
            st = fuzz_st()
            seq = fuzz_seq()
            print(getStreaks(st, seq))
        except ValueError:
            print("Value error for inputs")
            print("String: {}\nStreak: {}".format(st, seq))
            continue
        except OverflowError:
            print("Overflow error for inputs")
            print("String: {}\nStreak: {}".format(st, seq))
            continue
