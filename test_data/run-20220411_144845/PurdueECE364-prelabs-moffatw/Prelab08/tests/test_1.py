import unittest

from src import source as tasks


class TestSuite(unittest.TestCase):

    def test_getStreakProduct(self):

        # 2 Tests with sequence >= 20 digits and maxSize > 5
        with self.subTest(key="getStreakProduct valid 1"):
            string = "39272924723474196738"
            product = 252
            expectedValue = ["9272", "2729", "7292", "7419"]
            actualValue = tasks.getStreakProduct(string, 6, product)
            self.assertListEqual(actualValue, expectedValue)

        with self.subTest(key="getStreakProduct valid 2"):
            string = "39272924723474196738"
            product = 1008
            expectedValue = ["72924", "29247", "92472", "47419", "6738"]
            actualValue = tasks.getStreakProduct(string, 6, product)
            self.assertListEqual(actualValue, expectedValue)

        # test for a product that does not have a streak in the sequence given
        with self.subTest(key="getStreakProduct invalid"):
            string = "39272924723474196738"
            product = 40
            expectedValue = []
            actualValue = tasks.getStreakProduct(string, 6, product)
            self.assertListEqual(actualValue, expectedValue)

    def test_convertToBoolean(self):

        # Pass in a valid positive number and a valid size to the function
        with self.subTest(key="convertToBoolean valid"):
            expectedValue = [True, False, False, False, True, True, True, True]
            actualValue = tasks.convertToBoolean(143, 8)
            self.assertListEqual(actualValue, expectedValue)

        # Pass in a invalid positive decimal and a valid size to the function
        with self.subTest(key="convertToBoolean invalid"):
            expectedValue = []
            actualValue = tasks.convertToBoolean("20", 5)
            self.assertListEqual(actualValue, expectedValue)

    def test_convertToInteger(self):

        # Pass in a list of boolean elements to the function
        with self.subTest(key="convertToInteger valid"):
            input_list = [True, False, False, False, True, True, True, True]
            expectedValue = 143
            actualValue = tasks.convertToInteger(input_list)
            self.assertEqual(actualValue, expectedValue, "Integers are different")

        # Pass in a string to the function
        with self.subTest(key="convertToInteger input string"):
            actualValue = tasks.convertToInteger("bad string")
            self.assertIsNone(actualValue)

        # Pass in a list containing non-boolean elements to the function
        with self.subTest(key="convertToInteger input a list containing non-boolean elements"):
            input_list = [True, False, False, "bad string", True]
            actualValue = tasks.convertToInteger(input_list)
            self.assertIsNone(actualValue)

        # Pass in an empty list to the function
        with self.subTest(key="convertToInteger input empty list"):
            input_list = []
            actualValue = tasks.convertToInteger(input_list)
            self.assertIsNone(actualValue)
