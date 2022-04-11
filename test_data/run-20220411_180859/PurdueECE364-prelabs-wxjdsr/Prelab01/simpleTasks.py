# ######################################################
# Author : Xingjian Wang
# email : wang5066@purdue.edu
# ID: ee364b03
# Date : Jan 16, 2022
# ######################################################

from math import ceil
from types import NoneType


# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

# Problem 1 Helper functions

# Build a single pyramid with given @baseSize and @char
def buildSinglePyramid(baseSize: int, char: str) -> list[list[str]]:
    height = ceil(baseSize / 2)     # round up
    mid_index = baseSize // 2       # round down

    # builds a pyramid with all empty
    pyramid = [[' ' for element in range(baseSize)] for idx in range(height)]

    # change the corresponding space to @char (symmetrically)
    for level in range(height):
        left_index = mid_index - level
        right_index = mid_index + level
        for element_index in range(left_index, right_index + 1):
            pyramid[level][element_index] = char

    return pyramid


# Concatenate two pyramid lists into a single one
# Prereq: range(pyramid1) = range(pyramid2)
# Save the result in @pyramid1
def concatPyramids(pyramid1: list[list[str]], pyramid2: list[list[str]]) -> NoneType:
    for row in range(len(pyramid1)):
        for element in pyramid2[row]:
            pyramid1[row].append(element)


# This function adds the space after a pyramid
def addSpace(pyramid: list[list[str]]) -> NoneType:
    for row in range(len(pyramid)):
        pyramid[row].append(' ')


# Given a list, write it into a file
def writeList(list: list[list[str]], filePath: str) -> NoneType:
    f = open(filePath, 'w')
    for row in list:
        for element in row:
            f.write(element)
        f.write('\n')
    f.close()


# Problem 1 Function
def writePyramids(filePath: str, baseSize: int, count: int, char: str) -> NoneType:
    # Do nothing if count is 0
    if (count == 0):
        return

    # Build a single pyramid when count >= 1
    pyramid_single = buildSinglePyramid(baseSize, char)
    pyramids = buildSinglePyramid(baseSize, char)

    # Then, print the space and another pyramid
    for times in range(count - 1):      # "-1" since the first pyramid is already processed
        addSpace(pyramids)
        concatPyramids(pyramids, pyramid_single)

    writeList(pyramids, filePath)

# Problem 2 Helper functions

# Find the length of a continuous letter
# e.g. findLength("AAA", 'A') returns 3
# Prereq: @sequence should begins with @letter
def findLength(sequence: str, letter: str) -> int:
    length = 0
    for index in range(len(sequence)):
        if sequence[index] == letter:
            length += 1
        else:
            break
    return length


# Problem 2 Function
def getStreaks(sequence: str, letters: str) -> list[str]:
    # identify the individual letters
    letter_list = []
    for single_letter in letters:
        if single_letter not in letter_list:
            letter_list.append(single_letter)
    
    # find the sequence
    match_sequence = []
    index = 0

    # make sure there is no index-out-of-bound
    while index < len(sequence):
        if sequence[index] in letter_list:      # if found, put it into the result list
            length = findLength(sequence[index:], sequence[index])
            match_sequence.append(sequence[index] * length)
            index += length     # continue searching after these found letters
        else:                   # if not found, go to the next index
            index += 1

    return match_sequence


# Self-testing block
# ######################################################

# p  = buildSinglePyramid(7, '*')
# p1 = buildSinglePyramid(7, '*')
# p2 = buildSinglePyramid(7, '*')
# p_empty = []
# p_empty = p
# print(p_empty)
# addSpace(p_empty)
# print(p_empty)
# concatPyramids(p, p1)
# print(p_empty)
# print(addSpace(p1))
# print(concatPyramids([], p1))
# concatPyramids(p, p1)
# print(p)
# print(p1)
# concatPyramids(p, p2)
# print(p)
# print(p2)
### Final Test ###
# writePyramids('test1.txt', 13, 6, 'X')
# writePyramids('test2.txt', 15, 5, '*')
# sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
# print(getStreaks(sequence, "SAQT"))
# print(getStreaks(sequence, "PAZ"))