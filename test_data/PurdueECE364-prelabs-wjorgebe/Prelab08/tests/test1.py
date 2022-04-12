import unittest
from Prelab08.src import problems as tasks


class TestSuite(unittest.TestCase):

    def test_getStreakProduct(self):

        with self.subTest(key="5478965432168798474549886132"):
            expectedValue = ['547', '745']
            actualValue = tasks.getStreakProduct("54789654321687"
                                                 + "98474549886132", 6, 140)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="3023051966636400120289525"):
            expectedValue = ['19666', '9666']
            actualValue = tasks.getStreakProduct("3023051966636400120289525",
                                                 6, 1944)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="442659832034816902100"):
            actualValue = tasks.getStreakProduct("442659832034816902100",
                                                 10, 37)
            self.assertEqual(actualValue, [])

    def test_convertToBoolean(self):

        with self.subTest(key="Normal Input Test"):
            expectedValue = [False, False, False, False,
                             True, False, False, False,
                             False, True, True, True]
            actualValue = tasks.convertToBoolean(135, 12)
            self.assertEqual(actualValue, expectedValue)

        with self.subTest(key="Non-Integer Input Test"):
            expectedValue = []
            actualValue = tasks.convertToBoolean(1.32, 5)
            self.assertEqual(actualValue, expectedValue)

    def test_convertToInteger(self):

        with self.subTest(key="Normal Input Test"):
            expectedValue = 80
            actualValue = tasks.convertToInteger([True, False, True,
                                                  False, False, False, False])
            self.assertEqual(actualValue, expectedValue)

        with self.subTest(key="Non-List Test"):
            expectedValue = None
            actualValue = tasks.convertToInteger('hello')
            self.assertEqual(actualValue, expectedValue)

        with self.subTest(key="Invalid List Test"):
            expectedValue = None
            actualValue = tasks.convertToInteger([True, True, True, 'hey'])
            self.assertEqual(actualValue, expectedValue)

        with self.subTest(key="Empty List Test"):
            expectedValue = None
            actualValue = tasks.convertToInteger([])
            self.assertEqual(actualValue, expectedValue)


if __name__ == '__main__':
    with open('testrun.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
