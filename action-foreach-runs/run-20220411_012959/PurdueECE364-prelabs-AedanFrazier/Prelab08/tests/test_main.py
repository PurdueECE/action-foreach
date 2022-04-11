##########################################################
# Author    :   Aedan Frazier
# Email     :   frazie35@purdue.edu
# ID        :   ee364a06
# Date      :   3/1/2022
##########################################################

import sys
import unittest

sys.path.append('src')

from main import getStreakProduct
from main import convertToBoolean
from main import convertToInteger


class Tests(unittest.TestCase):

    def test_getStreakProduct(self):
        with self.subTest(key="9144576"):
            r = getStreakProduct("00112233445566778899", 10, 9144576)
            self.assertEqual(r, ["66778899"])
        with self.subTest(key="60480"):
            r = getStreakProduct("987654321123456789", 6, 60480)
            self.assertEqual(r, ["987654", "456789"])
        with self.subTest(key="999999999999"):
            input = "1111111111111111111111111"
            r = getStreakProduct(input, 4, 999999999999)
            self.assertEqual(r, [])

    def test_convertToBoolean(self):
        with self.subTest(key="Normal Input Test"):
            r = convertToBoolean(10, 5)
            self.assertEqual(r, [False, True, False, True, False])
        with self.subTest(key="Non-Integer Test"):
            r = convertToBoolean(3.3, 4)
            self.assertEqual(r, [])

    def test_convertToInteger(self):
        with self.subTest(key="Normal Input Test"):
            r = convertToInteger([True, False, True, False])
            self.assertEqual(r, 10)
        with self.subTest(key="Non-List Test"):
            r = convertToInteger("True False True False true")
            self.assertEqual(r, None)
        with self.subTest(key="Invalid List Test"):
            r = convertToInteger(["True", "False", "True", "False"])
            self.assertEqual(r, None)
        with self.subTest(key="Empty List Test"):
            r = convertToInteger([])
            self.assertEqual(r, None)


if __name__ == '__main__':
    with open('testrun.txt', "w") as file:
        runner = unittest.TextTestRunner(file)
        unittest.main(testRunner=runner)
