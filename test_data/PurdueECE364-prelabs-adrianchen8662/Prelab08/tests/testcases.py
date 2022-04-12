import unittest
import sys
import os

testcases_dir = os.path.dirname(__file__)
program_dir = os.path.join(testcases_dir,'..','src')
sys.path.append(program_dir)

import programs as tasks

class TestSuite(unittest.TestCase):

    def test_getStreakProduct(self):
        with self.subTest(key="32"):
            actualValue = tasks.getStreakProduct(148221723095871309581703985170329857103,6,32)
            self.assertEqual(actualValue,[48, 148, 822, 8221])

        with self.subTest(key="26"):
            actualValue = tasks.getStreakProduct(148221723095873857019385601931309581703985170329857103,8,27)
            self.assertEqual(actualValue,[93, 93, 39, 193, 193, 931, 1931])

        with self.subTest(key="17"):
            actualValue = tasks.getStreakProduct(53015986103958607123956710293581670593861509283650,11,4172)
            self.assertEqual(actualValue,[])

    def test_convertToBoolean(self):
        with self.subTest(key="Normal Input Test"):
            actualValue = tasks.convertToBoolean(135,12)
            self.assertEqual(actualValue,[False, False, False, False, True, False, False, False, False, True, True, True])

        with self.subTest(key="Non-Integer Input Test"):
            actualValue = tasks.convertToBoolean(151.12,10)
            self.assertEqual(actualValue,[])

    def test_convertToInteger(self):
        with self.subTest(key="Normal Input Test"):
            actualValue = tasks.convertToInteger([False, False, False, False, True, False, False, False, False, True, True, True])
            self.assertEqual(actualValue,135)

        with self.subTest(key="Non-List Test"):
            actualValue = tasks.convertToInteger("Not a list")
            self.assertEqual(actualValue,None)

        with self.subTest(key="Invalid List Test"):
            actualValue = tasks.convertToInteger([14,0,2,75,2,7,4,787,"Invalid list",1,6,5])
            self.assertEqual(actualValue,None)

        with self.subTest(key="Empty List Test"):
            actualValue = tasks.convertToInteger([])
            self.assertEqual(actualValue,None)

if __name__ == '__main__':
    with open('testrun.txt','a+') as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)