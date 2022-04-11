import unittest
import sys
from src import app as tasks
sys.path.insert(0, './')


class TestSuite(unittest.TestCase):

    def test_getStreakProduct(self):
        with self.subTest(key="84"):
            expectedValue = ['726', '374', '743', '374']
            actualValue = tasks.getStreakProduct(897263485729374329374, 6, 84)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="324"):
            expectedValue = ['3349', '3349', '9433', '3349',
                             '3493', '4933', '9334', '33433', '3349']
            actualValue = tasks.getStreakProduct(43349443349433493343349,
                                                 7, 324)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="329"):
            expectedValue = []
            actualValue = tasks.getStreakProduct(813799138479837419847393,
                                                 3, 329)
            self.assertEqual(expectedValue, actualValue)

    def test_convertToBoolean(self):
        with self.subTest(key="Normal Input Test"):
            expectedValue = [False, False, True, True, False, True]
            actualValue = tasks.convertToBoolean(13, 6)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Non-Integer Input Test"):
            expectedValue = []
            actualValue = tasks.convertToBoolean('13', 4)
            self.assertEqual(expectedValue, actualValue)

    def test_convertToInteger(self):
        with self.subTest(key="Normal Input Test"):
            expectedValue = 135
            bList = [True, False, False, False, False, True, True, True]
            actualValue = tasks.convertToInteger(bList)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Non-List Test"):
            expectedValue = None
            bList = 'This is a string'
            actualValue = tasks.convertToInteger(bList)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Invalid List Test"):
            expectedValue = None
            bList = [True, False, False, False, False, '84', 'yes', True]
            actualValue = tasks.convertToInteger(bList)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Empty List Test"):
            expectedValue = None
            bList = []
            actualValue = tasks.convertToInteger(bList)
            self.assertEqual(expectedValue, actualValue)


if __name__ == '__main__':
    with open('textrun.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
