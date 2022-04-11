
import random


def getStreakProduct(sequence, maxSize, product):

    return_list = []

    for i in range(len(sequence)):
        for j in range(2, maxSize + 1):
            if ((i + j) > len(sequence)):
                continue

            sub_sequence = sequence[i:i + j]

            calc_product = 1

            for char in sub_sequence:
                try:
                    calc_product = calc_product * int(char)
                except ValueError:
                    print(f"Value error for input {char}")
                    continue

            if (calc_product == product):
                return_list.append(sub_sequence)

    return return_list


def grammar_fuzzer(extra_length=5, char_start=33, char_range=14):
    out = ''.join((random.choice('1234567890') for i in range(5)))
    for i in range(0, extra_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out


input_sequence = grammar_fuzzer()

getStreakProduct(input_sequence, 6, 100)
