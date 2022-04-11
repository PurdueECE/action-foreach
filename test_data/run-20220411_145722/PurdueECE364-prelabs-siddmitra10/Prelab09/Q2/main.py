from fuzzer import alphanumericFuzzer, numericFuzzer
from functions import getStreakProduct

if __name__ == "__main__":
    for i in range(0, 20):
        seq = numericFuzzer()
        data = getStreakProduct(seq, 3, 35)
    for i in range(0, 20):
        seq = alphanumericFuzzer()
        data = getStreakProduct(seq, 5, 8)
