import unittest
import problems as tasks
import random


class TestSuite(unittest.TestCase):

    def test_getStreakProduct(self):

        with self.subTest(key="547896543216879847454988613"):
            expectedValue = ['547', '745']
            try:
                actualValue = tasks.getStreakProduct("54789654321687"
                                                     + "9847454988613", 6, 140)
            except OverflowError:
                print("Overflow error: input is too large")
            except TypeError:
                print("Input has to be a number")
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="3023051966636400120289525"):
            expectedValue = ['19666', '9666']
            try:
                actualValue = tasks.getStreakProduct("3023051966636" +
                                                     "400120289525",
                                                     6, 1944)
            except OverflowError:
                print("Overflow error: input is too large")
            except TypeError:
                print("Type Error: values have to be integers")
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="442659832034816902100"):
            try:
                actualValue = tasks.getStreakProduct("44265983203" +
                                                     "4816902100",
                                                     10, 37)
            except OverflowError:
                print("Overflow error: input is too large")
            except TypeError:
                print("Type Error: values have to be integers")
            self.assertEqual(actualValue, [])

    def test_randomFuzzing(self):

        with self.subTest(key="Random input on Streak Product"):
            for i in range(10):  # 10 trials
                input = grammar_fuzzer()
                try:
                    tasks.getStreakProduct(input)
                except TypeError:
                    print("Type error for input ", input)
                    continue

    def test_convertToBoolean(self):

        with self.subTest(key="Normal Input Test"):
            expectedValue = [False, False, False, False,
                             True, False, False, False,
                             False, True, True, True]
            actualValue = tasks.convertToBoolean(135, 12)
            self.assertEqual(actualValue, expectedValue)

        with self.subTest(key="Non-Integer Input Test"):
            expectedValue = []
            actualValue = tasks.convertToBoolean(1.32, 5)
            self.assertEqual(actualValue, expectedValue)

    def test_convertToInteger(self):

        with self.subTest(key="Normal Input Test"):
            expectedValue = 80
            actualValue = tasks.convertToInteger([True, False, True,
                                                  False, False, False, False])
            self.assertEqual(actualValue, expectedValue)

        with self.subTest(key="Non-List Test"):
            expectedValue = None
            actualValue = tasks.convertToInteger('hello')
            self.assertEqual(actualValue, expectedValue)

        with self.subTest(key="Invalid List Test"):
            expectedValue = None
            actualValue = tasks.convertToInteger([True, True, True, 'hey'])
            self.assertEqual(actualValue, expectedValue)

        with self.subTest(key="Empty List Test"):
            expectedValue = None
            actualValue = tasks.convertToInteger([])
            self.assertEqual(actualValue, expectedValue)


def grammar_fuzzer(extra_length=5, char_start=33, char_range=14):
    out = ''.join((random.choice('1234567890') for i in range(5)))
    for i in range(0, extra_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out


if __name__ == '__main__':
    with open('testrun.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
