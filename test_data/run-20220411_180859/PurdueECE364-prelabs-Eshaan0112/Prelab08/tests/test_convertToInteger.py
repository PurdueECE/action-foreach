import unittest
from src import convertToInteger as tasks


class TestSuite(unittest.TestCase):
    def test_convertToInteger(self):
        with self.subTest(key="Normal Input Test"):
            expectedValue = 135
            actualValue = tasks.convertToInteger([True, False, False, False, False, True, True, True])  # First test
            self.assertEqual(expectedValue, actualValue)
        with self.subTest(key="Non-List Test"):
            expectedValue = None
            actualValue = tasks.convertToInteger("Not a list")  # Second test
            self.assertEqual(expectedValue, actualValue)
        with self.subTest(key="Invalid List Test"):
            expectedValue = None
            actualValue = tasks.convertToInteger(["1", "2", "3"])  # Third test
            self.assertEqual(expectedValue, actualValue)
        with self.subTest(key="Empty List Test"):
            expectedValue = None
            actualValue = tasks.convertToInteger([])  # Fourth test
            self.assertEqual(expectedValue, actualValue)
        with self.subTest(key="Extra"):
            expectedValue = None
            actualValue = tasks.convertToInteger([False, "2", False])  # Extra test
            self.assertEqual(expectedValue, actualValue)
        with self.subTest(key="Extra"):
            expectedValue = 7
            actualValue = tasks.convertToInteger([True, True, True])  # Extra test
            self.assertEqual(expectedValue, actualValue)


if __name__ == "__main__":
    with open('testrun.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
