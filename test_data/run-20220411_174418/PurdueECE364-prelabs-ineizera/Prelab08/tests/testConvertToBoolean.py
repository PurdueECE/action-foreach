import unittest
from convertoBoolean import *
class TestSuite(unittest.TestCase):
    def test_convertToBoolean(self):
        with self.subTest(key='Normal Input Test'):
            self.assertEqual(convertToBoolean(8,5),['False', 'True', 'False', 'False', 'False'])
        with self.subTest(key='Non-Integer Input Test'):
            self.assertEqual(convertToBoolean("8",5),[])
if __name__ == '__main__':
    f = open("testrun.txt",'w')
    runner = unittest.TextTestRunner(f)
    unittest.main(testRunner=runner)
    f.close()