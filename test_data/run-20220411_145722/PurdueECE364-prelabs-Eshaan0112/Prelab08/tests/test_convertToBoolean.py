import unittest
from src import convertToBoolean as tasks


class TestSuite(unittest.TestCase):
    def test_convertToBoolean(self):
        with self.subTest(key="Normal Input Test"):
            expectedValue = [False, False, False, False, True, False, False, False, False, True, True, True]
            actualValue = tasks.convertToBoolean(135, 12)  # First test
            self.assertEqual(expectedValue, actualValue)
        with self.subTest(key="Non-Integer Input Test"):
            expectedValue = []
            actualValue = tasks.convertToBoolean('Not a valid integer', 12)  # Second test
            self.assertEqual(expectedValue, actualValue)


if __name__ == "__main__":
    unittest.main()
