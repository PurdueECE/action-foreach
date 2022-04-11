import unittest
import sys
from src import programs as tasks

class TestSuite(unittest.TestCase):
	
	def test_getStreakProduct(self):
		with self.subTest(key="666666666666666666661222"):
			expectedValue = ['122', '22', '22']
			actualValue = tasks.getStreakProduct("666666666666666666661222", 8, 4)
			self.assertEqual(expectedValue, actualValue, "Lists do not match")

		with self.subTest(key="999999999999999999999999999999914822"):
			expectedValue = ['148', '48', '822']
			actualValue = tasks.getStreakProduct("999999999999999999999999999999914822", 6, 32)
			self.assertEqual(expectedValue, actualValue, "Lists do not match")

		with self.subTest(key="34567890987654323456789"):
			expectedValue = []
			actualValue = tasks.getStreakProduct("34567890987654323456789", 12, 1)
			self.assertEqual(expectedValue, actualValue, "Lists do not match")
			
	def test_convertToBoolean(self):
		with self.subTest(key="Normal Input Test"):
			expectedValue = [False, False, False, False, True, False, True, False]
			actualValue = tasks.convertToBoolean(10, 8)
			self.assertEqual(expectedValue, actualValue, "Lists do not match")

		with self.subTest(key="Non-Integer Input Test"):
			expectedValue = []
			actualValue = tasks.convertToBoolean("6", 5)
			self.assertEqual(expectedValue, actualValue, "Lists do not match")

	def test_convertToInteger(self):
		with self.subTest(key="Normal Input Test"):
			expectedValue = 10
			actualValue = tasks.convertToInteger([True, False, True, False])
			self.assertEqual(expectedValue, actualValue, "Integer values do not match.")
		with self.subTest(key="Non-List Test"):
			expectedValue = None
			actualValue = tasks.convertToInteger("This is a string.")
			self.assertEqual(expectedValue, actualValue, "Values do not match.")
		with self.subTest(key="Invalid List Test"):
			expectedValue = None
			actualValue = tasks.convertToInteger([1, 2, 3, 4, 5])
			self.assertEqual(expectedValue, actualValue, "Values do not match.")
		with self.subTest(key="Empty List Test"):
			expectedValue = None
			actualValue = tasks.convertToInteger([])
			self.assertEqual(expectedValue, actualValue, "Values do not match.")


if __name__ == '__main__' :
	with open('log.txt', "w") as f:
		runner = unittest.TextTestRunner(f)
		unittest.main(testRunner=runner)
