import unittest
from main import *
class TestSuite(unittest.TestCase):
    def test_getStreakProduct(self):
        with self.subTest(key='1'):
            self.assertEqual(getStreakProduct('1234512322231234611345',5,6),[123, 23, 123, 23, 32, 23, 231, 312, 123, 23, 61, 611])
        with self.subTest(key='2'):
            self.assertEqual(getStreakProduct('222434262283116224683222612',5,24),[243, 342, 262, 622, 83, 831, 8311, 11622, 1622, 622, 46, 83, 3222, 226, 2261, 2612])
        with self.subTest(key='3'):
            self.assertEqual(getStreakProduct('222234564123456347651',3,7),[])

if __name__ == '__main__':
    f = open("testrun.txt",'w')
    runner = unittest.TextTestRunner(f)
    unittest.main(testRunner=runner)
    f.close()