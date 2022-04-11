def getStreakProduct(sequence, maxSize, product):
    sequence = [int(x) for x in sequence]
    # print(sequence)
    data = []
    for i in range(len(sequence) - 1):  # missing last one
        prev = [sequence[i]]
        prevProd = sequence[i]
        # print(f'i: {sequence[i]}')
        for j in range(i + 1, i + maxSize):
            if j >= len(sequence):
                continue
            prev.append(sequence[j])
            prevProd *= sequence[j]
            # print(f'\tj: {sequence[j]} currProd: {prevProd}')
            if prevProd == product:
                temp = ''
                for x in prev:
                    temp += str(x)
                data.append(temp)
    return data
