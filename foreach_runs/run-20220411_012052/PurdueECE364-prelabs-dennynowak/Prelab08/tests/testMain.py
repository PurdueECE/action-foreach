#################################
#   Author: Denny Nowak
#   Email:  nowak32@purdue.edu
#   ID:     ee364b14
#   Date:   03/02/2022
#################################

import os
import sys
import unittest

# Get main.py file from src folder
testDir = os.path.dirname(__file__)
srcDir = os.path.join(testDir, '..', 'src')
sys.path.append(srcDir)
import main as tasks # noqa


class TestSuite(unittest.TestCase):
    # Problem 1
    def test_getStreakProduct(self):
        # First two subtests seq > 20 and maxsize > 5
        with self.subTest(key="Problem 1 First Subtest"):
            expectedVal = ['8921', '892', '1289', '289']
            expectedVal.sort()
            actualVal = tasks.getStreakProduct(12567923892138012890312, 6, 144)
            actualVal.sort()
            self.assertListEqual(actualVal, expectedVal)
        with self.subTest(key="Problem 1 Second Subtest"):
            expectedVal = ['38', '38', '83', '324', '381', '234', '1234']
            expectedVal.sort()
            actualVal = tasks.getStreakProduct(62358832452381234984382, 7, 24)
            actualVal.sort()
            self.assertListEqual(actualVal, expectedVal)
        # Product does not have streak
        with self.subTest(key="Problem 1 Third Subtest"):
            expectedVal = []
            actualVal = tasks.getStreakProduct(893240293483244324323419, 6, 2423423432)
            self.assertListEqual(actualVal, expectedVal)

    # Problem 2
    def test_convertToBoolean(self):
        with self.subTest(key="Normal Input Test"):
            expectedVal = [False, False, True, True, False, True]
            actualVal = tasks.convertToBoolean(13, 6)
            self.assertListEqual(actualVal, expectedVal)
        with self.subTest(key="Non-Integer Input Test"):
            expectedVal = []
            actualVal = tasks.convertToBoolean(2.53, 7)
            self.assertListEqual(actualVal, expectedVal)

    # Problem 3
    def test_convertToInteger(self):
        with self.subTest(key="Normal Input Test"):
            expectedVal = 13
            actualVal = tasks.convertToInteger([True, True, False, True])
            self.assertEqual(actualVal, expectedVal)
        with self.subTest(key="Non-List Test"):
            expectedVal = None
            actualVal = tasks.convertToInteger('Test')
            self.assertEqual(actualVal, expectedVal)
        with self.subTest(key="Invalid List Test"):
            expectedVal = None
            actualVal = tasks.convertToInteger([5, '5'])
            self.assertEqual(actualVal, expectedVal)
        with self.subTest(key="Empty List Test"):
            expectedVal = None
            actualVal = tasks.convertToInteger([])
            self.assertEqual(actualVal, expectedVal)


if __name__ == '__main__':
    with open('testrun.txt', "w") as fptr:
        runner = unittest.TextTestRunner(fptr)
        unittest.main(testRunner=runner)
