import unittest
import sys
sys.path.insert(0, "./")
from src import application1, application2

class TestSuite(unittest.TestCase):

    def test_getStreakProduct(self):
        expectedVal = ['534']
        exVal2 = ['48', '4124']
        exVal3 = []
        tVal = "37253421669109145924"
        tVal2 = "29069112348066341242"
        tVal3 = "226939368101877349784325540665"
        actualVal = application1.getStreakProduct(tVal, 8, 60)
        actVal2 = application1.getStreakProduct(tVal2, 6, 32)
        self.assertEqual(expectedVal, actualVal)
        self.assertEqual(exVal2, actVal2)
        actVal3 = application1.getStreakProduct(tVal3, 6, 5)
        self.assertEqual(actVal3, exVal3)
    
    def test_convertToBoolean(self):
        # Test 1: Valid positive number, valid size
        bin1exp =  [False, False, False, False, True, False, False, False, False, True, True, True]
        with self.subTest(key="Normal Input Test"):
            actualValue = application2.convertToBoolean(135,12)
            self.assertListEqual(actualValue, bin1exp)
        # Test 2: Invalid positive number, valid size
        bin2exp = []
        with self.subTest(key="Non-Integer Input Test"):
            actualValue = application2.convertToBoolean(34.2, 9)
            self.assertListEqual(actualValue, bin2exp)

        with self.subTest(key="Invalid Integer Test"):
            actualValue = application2.convertToBoolean(-23, 9)
            self.assertListEqual(actualValue, bin2exp)

        with self.subTest(key="Invalid Size Integer Test"):
            actualValue = application2.convertToBoolean(-23, -1)
            self.assertListEqual(actualValue, bin2exp)

     

    def test_converToInteger(self):
        test1 = 10
        with self.subTest(key="Normal Input Test"):
            actual1 = application2.convertToInteger([True, False, True, False])  
            self.assertEqual(test1, actual1)
        nonList = None
        with self.subTest(key="Non-List Test"):
            actual2 = application2.convertToInteger("lakejfl;aksjfd;laeoifae")
            self.assertEqual(nonList, actual2)

        invList = [1, 3, 6, 7]
        expVal = None
        with self.subTest(key="Invalid List Test"):
            actual3 = application2.convertToInteger(invList)
            self.assertEqual(expVal, actual3)

        emptyList = []
        expVal = None
        with self.subTest(key="Empty List Test"):
            actual4 = application2.convertToInteger(emptyList)
            self.assertEqual(expVal, actual4)

    
if __name__ == '__main__':
    with open('testrun.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
