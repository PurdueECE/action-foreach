import unittest
import functions as tasks


class TestSuite(unittest.TestCase):

    def test_getStreakProduct(self):

        with self.subTest(key='Test 1: Valid sequence & streak'):
            expectedValue = ['547', '475']
            sequence = '547896543216879844475'
            actualValue = tasks.getStreakProduct(sequence, 6, 140)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key='Test 2: Valid sequence & streak'):
            expectedValue = ['826', '438', '6182', '446', '464', '644',
                             '4432', '44321']
            sequence = '82629438676182446443212345'
            actualValue = tasks.getStreakProduct(sequence, 6, 96)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key='Test 3: Valid sequence & no streak'):
            expectedValue = []
            sequence = '134235245234195234545478945645261'
            actualValue = tasks.getStreakProduct(sequence, 6, 419)
            self.assertEqual(expectedValue, actualValue)

    def test_convertToBoolean(self):

        with self.subTest(key='Test 1: Valid number & valid size'):
            expectedValue = ['True', 'True', 'False', 'True', 'False',
                             'True', 'True', 'False', 'False', 'False',
                             'True', 'True', 'True', 'False', 'False',
                             'False', 'False', 'False', 'False', 'False',
                             'False', 'False', 'False', 'False', 'False',
                             'False', 'True']
            actualValue = tasks.convertToBoolean(112312321, 40)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key='Test 2: Invalid Positive Decimal'):
            expectedValue = []
            actualValue = tasks.convertToBoolean(11.243, 40)
            self.assertEqual(expectedValue, actualValue)

    def test_convertToInteger(self):

        with self.subTest(key='Normal Input Test'):
            valid_list = ['True', 'True', 'False', 'True',
                          'False', 'True', 'True', 'False', 'False',
                          'False', 'True', 'True', 'True', 'False',
                          'False', 'False', 'False', 'False', 'False',
                          'False', 'False', 'False', 'False', 'False',
                          'False', 'False', 'True']
            expectedValue = 112312321
            actualValue = tasks.convertToInteger(valid_list)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key='Non-List Test'):
            expectedValue = None
            actualValue = tasks.convertToInteger("String")
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key='Invalid List Test'):
            invalid_list = ['True', 'False', 'Invalid', 'Words']
            expectedValue = None
            actualValue = tasks.convertToInteger(invalid_list)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key='Empty List Test'):
            empty_list = []
            expectedValue = None
            actualValue = tasks.convertToInteger(empty_list)
            self.assertEqual(expectedValue, actualValue)


if __name__ == '__main__':
    with open('testrun.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
