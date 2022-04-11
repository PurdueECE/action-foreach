import unittest
import sys
sys.path.insert(1, "../src/")
import programs as tasks

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


if __name__ == '__main__' :
	unittest.main()
