# ######################################################
# Author : < Nimal Padmanabhan >
# email : < npadmana@purdue.edu >
# ID : < ee364b17 >
# Date : < 3/5/2022 >
# ######################################################
from cgi import print_form
import os # List of module import statements
import sys
# from typing import List # Each one on a line
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
def getStreakProduct(sequence, maxSize, product):
    prodList = []
    seq = [int(x) for x in sequence]
    sequence = seq
    # print(seqStr)
    for num in range(0, len(seq)):
        curr = [sequence[num]]
        currProduct = sequence[num]
        for elem in range(num + 1, maxSize + num):
            if elem < len(sequence):
                curr.append(seq[elem])
                currProduct *= seq[elem]
                # print(currProduct, product)
                if product == currProduct:
                    prodStr = ""
                    for i in curr:
                        prodStr += str(i)
                    # prodStr += str(seq[num])
                    prodList.append(prodStr)

    return prodList



if __name__ == "__main__":
   result = getStreakProduct("29069112348066341242", 6, 32)
   print(result)