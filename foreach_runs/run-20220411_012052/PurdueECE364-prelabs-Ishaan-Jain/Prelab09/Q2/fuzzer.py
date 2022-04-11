from curses import intrflush
import random

def fuzzer(max_length = 100, char_start = 32, char_range = 32):
    string_length = random.randrange(0, max_length + 1)
    out = ""
    for i in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out

def grammar_fuzzer(extra_length = 5, char_start = 33, char_range = 14):
    out = ''.join((random.choice('1234567890') for i in range(5)))
    for i in range(0, extra_length):
        out += str(random.randrange(char_start, char_start + char_range)) #Fuzzy inputs always are of size 10 but contains invalid characters
    return out
# print(fuzzer())
# print(fuzzer())



def getStreakProduct(sequence, maxSize, product):
    List = []
    seq = [int(x) for x in sequence]
    sequence = seq
    for num in range(0, len(seq)):
        cur = [sequence[num]]
        curp = sequence[num]

        for elem in range(num + 1, maxSize + num):
            if elem < len(sequence):
                cur.append(seq[elem])

                curp *= seq[elem]

                if product == curp:
                    proS = ""
                    for i in cur:
                        proS += str(i)
                    List.append(proS)

    return List

if __name__ == "__main__":
    # for i in range(0, 20):
    #     randSeq = fuzzer()
    #     print(randSeq)
    #     test1 = getStreakProduct(randSeq, 3, 35)
    #     print(test1)
    

    for i in range(0, 2):
         fuzSeq1 = grammar_fuzzer()
         print(f"Grammar fuzzer value 1: {fuzSeq1}")
         test1 = getStreakProduct(fuzSeq1, 18, 24)
         print(f"\n1st Value of getStreakProduct: {test1}")

         fuzSeq2 = grammar_fuzzer(6000000, 30, 1200)
         print(f"Grammar fuzzer value 2:{fuzSeq2}")
         test2 = getStreakProduct(fuzSeq2, 2, 40)
         print(f"\n2nd Value of getStreakProduct: {test2}")