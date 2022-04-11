# ######################################################
# Author :  Xingjian Wang
# email :   wang5066@purdue.edu
# ID:       ee364b03
# Date :    Mar 6, 2022
# ######################################################

import unittest
from src import DataTypeConverter as DTC


# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
class TestSuite(unittest.TestCase):

    # Q1
    def test_getStreakProduct(self):
        with self.subTest(key="32"):
            expectedValue = ["822", "8221", "2218", "184", "84", "244"]
            sequence = "3982218436903582443621902173"
            maxSize = 7
            product = 32
            actualValue = DTC.getStreakProduct(sequence, maxSize, product)
            self.assertEqual(expectedValue, actualValue,
                             "key==32 test case failed")
        with self.subTest(key="180"):
            expectedValue = ['3625', '5236', '211925', '119252',
                             '19252', '9252', '2529']
            sequence = "362523622119252939078658374021"
            maxSize = 12
            product = 180
            actualValue = DTC.getStreakProduct(sequence, maxSize, product)
            self.assertEqual(expectedValue, actualValue,
                             "key==180 test case failed")
        with self.subTest(key="105"):   # empty test
            expectedValue = []
            sequence = "5478923673694131386534832378653489327284756361"
            maxSize = 15
            product = 105
            actualValue = DTC.getStreakProduct(sequence, maxSize, product)
            self.assertEqual(expectedValue, actualValue,
                             "empty list test case failed")

    # Q2
    def test_convertToBoolean(self):
        with self.subTest(key="Normal Input Test"):
            expectedValue = [False, False, True, False, False,
                             False, True, True, True, True]
            actualValue = DTC.convertToBoolean(143, 10)
            self.assertEqual(expectedValue, actualValue,
                             "Normal Input Test failed")
        with self.subTest(key="Non-Integer Input Test"):
            expectedValue = []
            actualValue = DTC.convertToBoolean(3.14, 6)
            self.assertEqual(expectedValue, actualValue,
                             "Non-Integer Input Test failed")

    # Q3
    def test_convertToInteger(self):
        with self.subTest(key="Normal Input Test"):
            expectedValue = 143
            boolList = [False, False, True, False, False,
                        False, True, True, True, True]
            actualValue = DTC.convertToInteger(boolList)
            self.assertEqual(expectedValue, actualValue,
                             "Normal Input Test failed")
        with self.subTest(key="Non-List Test"):
            expectedValue = None
            boolList = "I am not list hahaha"
            actualValue = DTC.convertToInteger(boolList)
            self.assertEqual(expectedValue, actualValue,
                             "Non-List Test failed")
        with self.subTest(key="Invalid List Test,"):
            expectedValue = None
            boolList = [True, False, 1, False]
            actualValue = DTC.convertToInteger(boolList)
            self.assertEqual(expectedValue, actualValue,
                             "Invalid List failed")
        with self.subTest(key="Empty List Test"):
            expectedValue = None
            boolList = []
            actualValue = DTC.convertToInteger(boolList)
            self.assertEqual(expectedValue, actualValue,
                             "Empty List Test failed")


if __name__ == '__main__':
    with open('testrun.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
    # See if test works
