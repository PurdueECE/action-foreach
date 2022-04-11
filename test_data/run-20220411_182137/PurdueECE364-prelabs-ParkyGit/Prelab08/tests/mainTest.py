import unittest
from src import main as tasks


class TestSuite(unittest.TestCase):

    def test_getStreakProduct(self):
        with self.subTest(key="long bois"):
            input = "3522897235267345822832258652238"
            expected = ['3522', '2352', '526', '345', '3225', '652', '5223']
            actualValue = tasks.getStreakProduct(input, 6, 60)  # should return 148, 48, 822
            self.assertListEqual(actualValue, expected)
        with self.subTest(key="longbois2"):
            input = "22223579999114453711111"
            expected = ['2222357', '1144537', '144537', '1445371', '44537', '445371', '4453711']
            actualValue = tasks.getStreakProduct(input, 7, 1680)  # should return 148, 48, 822
            self.assertListEqual(actualValue, expected)

        with self.subTest(key="nostreaks"):
            input = "23876543703213534643"
            expected = []
            actualValue = tasks.getStreakProduct(input, 7, 69)
            self.assertListEqual(actualValue, expected)

    def test_convertToBoolean(self):
        with self.subTest(key="Normal Input Test"):
            actualValue = tasks.convertToBoolean(9, 3)
            self.assertListEqual(actualValue, [True, False, False, True])
        with self.subTest(key="Non-Integer Input Test"):
            actualValue = tasks.convertToBoolean(13.5, 12)
            self.assertListEqual(actualValue, [])

    def test_convertToInteger(self):
        with self.subTest(key="Normal Input Test"):
            list = [True, False, False, False, False, True, True, True]
            expected = 135
            actualValue = tasks.convertToInteger(list)
            self.assertEqual(actualValue, expected)
        with self.subTest(key="Non-List Test"):
            list = "hi lol"
            expected = None
            actualValue = tasks.convertToInteger(list)
            self.assertEqual(actualValue, expected)
        with self.subTest(key="Invalid List Test"):
            list = ["owo", "uwu", "umu"]
            expected = None
            actualValue = tasks.convertToInteger(list)
            self.assertEqual(actualValue, expected)
        with self.subTest(key="Empty List Test"):
            list = []
            expected = None
            actualValue = tasks.convertToInteger(list)
            self.assertEqual(actualValue, expected)


if __name__ == '__main__':
    unittest.main()
    with open('testrun.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
