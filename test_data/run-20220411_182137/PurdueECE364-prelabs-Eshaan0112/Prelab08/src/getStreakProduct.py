def getStreakProduct(sequence, maxSize, product):
    subsequence = []
    for index in range(len(sequence)-1):
        for size in range(2, maxSize + 1):
            if groupProduct(sequence, index, size) == product:
                subsequence.append(sequence[index:index+size])
    return subsequence


def groupProduct(sequence, index, size):
    if len(sequence) < index + size:
        return 0
    prod = 1
    for i in range(size):
        prod *= int(sequence[index+i])
    return prod


if __name__ == "__main__":
    sequence = "12345678912345678922"
    print(len(sequence))
    maxSize = 7
    product = 32
    print(getStreakProduct(sequence, maxSize, product))
