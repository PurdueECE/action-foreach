import unittest
from src import getStreakProduct as tasks


class TestSuite(unittest.TestCase):
    def test_getStreakProduct(self):
        with self.subTest(key="Product value tested: 32"):
            expectedValue = ['1234567', '234567', '1234567', '234567']
            actualValue = tasks.getStreakProduct("12345678912345678922", 7, 5040)  # First test
            self.assertEqual(expectedValue, actualValue)
        with self.subTest(key="Product value tested: 125"):
            expectedValue = ['355444']
            actualValue = tasks.getStreakProduct("555355444544244412200", 6, 4800)  # Second test
            self.assertEqual(expectedValue, actualValue)
        with self.subTest(key="Returning empty list, Product value tested: 32"):
            expectedValue = []
            actualValue = tasks.getStreakProduct("12345678912345678922", 7, 32)  # Third test -> Should return empty list
            self.assertEqual(expectedValue, actualValue)


if __name__ == "__main__":
    unittest.main()
