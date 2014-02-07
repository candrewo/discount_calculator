import unittest
from disc_calc import DiscountCalculator

class DiscountCalculatorTests(unittest.TestCase):
	def five_dollar_discount_test(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(250, 5, 'dollar')
		self.assertEqual (5, result)
	def test_ten_percent_discount(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(100, 10, 'percent')
		self.assertEqual(10, result)
	def fifteen_percent_discount_test(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(100, 15, 'percent')
		self.assertEqual (15, result)
	def invalid_discount_types_test(self):
		discount_calculator = DiscountCalculator()
		self.assertRaises (ValueError, discount_calculator.calculate,
		 150, 5, 'string')
	def floating_point_percentage_discount_test(self):
	    discount_calculator = DiscountCalculator()
	    result = discount_calculator.calculate(100.0,10.0,'percent')
	    self.assertEqual(10.0, result)
	def floating_point_absolute_discount_test(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(250.0,5.0,'dollar')
		self.assertEqual(5.0, result)
	def percent_discount_more_than_100_test(self):
		discount_calculator = DiscountCalculator()
		self.assertRaises (ValueError, discount_calculator.calculate, 
			150, 110, 'percent')
	def dollar_amount_greater_than_total_test(self):
		discount_calculator = DiscountCalculator()
		self.assertRaises (ValueError, discount_calculator.calculate,
			150, 160, 'dollar')