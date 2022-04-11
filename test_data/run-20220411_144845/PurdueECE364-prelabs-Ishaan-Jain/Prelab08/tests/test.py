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
        tVal3 = "00780207910792197361"
        actualVal = getStreakProduct.getStreakProduct(tVal, 8, 60)
        actVal2 = getStreakProduct.getStreakProduct(tVal2, 6, 32)
        self.assertEqual(expectedVal, actualVal)
        self.assertEqual(exVal2, actVal2)
        actVal3 = getStreakProduct.getStreakProduct(tVal3, 6, 5)
        self.assertEqual(actVal3, exVal3)
    
    def test_convertToBoolean(self):
         # Test 1: Valid positive number, valid size
         bin1exp =  [False, False, False, False, False, True, True, True, True, False, False, False]
         with self.subTest(key="Normal Input Test"):
             actualValue = convertToBoolean.convertToBoolean(120,12)
             self.assertListEqual(actualValue, bin1exp)
         # Test 2: Invalid positive number, valid size
         bin2exp = []
         with self.subTest(key="Non-Integer Input Test"):
             actualValue = convertToBoolean.convertToBoolean(74.2, 9)
             self.assertListEqual(actualValue, bin2exp)

         with self.subTest(key="Invalid Integer Test"):
             actualValue = convertToBoolean.convertToBoolean(-73, 9)
             self.assertListEqual(actualValue, bin2exp)

         with self.subTest(key="Invalid Size Integer Test"):
             actualValue = convertToBoolean.convertToBoolean(-93, -1)
             self.assertListEqual(actualValue, bin2exp)

     

    def test_convertToInteger(self):
         test1 = 9
         with self.subTest(key="Normal Input Test"):
             actual1 = convertToInteger.convertToInteger([False,False,True, False, False, True])  
             self.assertEqual(test1, actual1)

         nonList = None
         with self.subTest(key="Non-List Test"):
             actual2 = convertToInteger.convertToInteger("lbjkkas")
             self.assertEqual(nonList, actual2)

         invList = [5, 5, 7, 8]
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