def getStreakProduct(sequence, maxSize, product):
    current_product = 1
    current_streak = ""
    streaks = []

    for i in range(len(sequence)):
        for s in range(0, maxSize):
            index = i + s
            if (index <= len(sequence)-1):
                current_product = current_product * int(sequence[index])
                current_streak = current_streak + str(sequence[index])
                if(current_product == product):
                    streaks.append(current_streak)
        current_product = 1
        current_streak = ""

    return streaks