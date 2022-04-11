import unittest
from itertools import combinations
#sequence = string 
def getProduct(n):
 
    product = 1
 
    while (n != 0):
        product = product * (n % 10)
        n = n // 10
 
    return product

def getStreakProduct(sequence, maxSize,product):
    result = [sequence[i: j] for i in range(len(sequence)) for j in range(i + 1, len(sequence) + 1) if (2<= len(sequence[i:j]) <= maxSize ) ]
    
    # turns them into integers
    for i in range(len(result)):
        result[i] = int(result[i])

    result2 = []
    for i in range(len(result)):
        n = result[i]
        prod = getProduct(n)
        if prod != product:
            result2.append(result[i]) # second list that has elements that dont fit
    for i in result[:]:
        if i in result2:
            result.remove(i)

    return result


