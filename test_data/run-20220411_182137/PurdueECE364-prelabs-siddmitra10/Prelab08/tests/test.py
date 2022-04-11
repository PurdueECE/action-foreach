import unittest
import sys
sys.path.insert(0, "./")
from src import getStreakProduct, convertToBoolean, convertToInteger


class TestSuite(unittest.TestCase):

    def test_getStreakProduct(self):
        expectedVal = ['256']
        exVal2 = ['84']
        exVal3 = []
        tVal = "82725665152796337442"
        tVal2 = "52323392709620842110"
        tVal3 = "0000000000000000000"
        actualVal = getStreakProduct.getStreakProduct(tVal, 8, 60)
        actVal2 = getStreakProduct.getStreakProduct(tVal2, 6, 32)
        actVal3 = getStreakProduct.getStreakProduct(tVal3, 6, 5)
        self.assertEqual(expectedVal, actualVal)
        self.assertEqual(exVal2, actVal2)
        self.assertEqual(actVal3, exVal3)

    def test_convertToBoolean(self):
        # Test 1: Valid positive number, valid size
        bin1exp = [False, False, False, False, True, False,
                   False, False, False, True, True, True]
        with self.subTest(key="Normal Input Test"):
            actualValue = convertToBoolean.convertToBoolean(135, 12)
            self.assertListEqual(actualValue, bin1exp)
        # Test 2: Invalid positive number, valid size
        bin2exp = []
        with self.subTest(key="Non-Integer Input Test"):
            actualValue = convertToBoolean.convertToBoolean(34.2, 9)
            self.assertListEqual(actualValue, bin2exp)

    def test_converToInteger(self):
        test1 = 11
        with self.subTest(key="Normal Input Test"):
            act1 = convertToInteger.convertToInteger([True, False, True, True])
            self.assertEqual(test1, act1)
        nonList = None
        with self.subTest(key="Non-List Test"):
            act2 = convertToInteger.convertToInteger("lakejfl;aksjfd;laeoifae")
            self.assertEqual(nonList, act2)

        invList = ["haahha", 1, 2]
        expVal = None
        with self.subTest(key="Invalid List Test"):
            actual3 = convertToInteger.convertToInteger(invList)
            self.assertEqual(expVal, actual3)

        emptyList = []
        expVal = None
        with self.subTest(key="Empty List Test"):
            actual4 = convertToInteger.convertToInteger(emptyList)
            self.assertEqual(expVal, actual4)


if __name__ == '__main__':
    with open('testrun.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
