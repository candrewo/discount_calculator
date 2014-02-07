import unittest
from disc_calc import DiscountCalculator

class DiscountCalculatorTests(unittest.TestCase):
  def test_ten_percent_discount(self):
    discount_calculator = DiscountCalculator()
    result = discount_calculator.calculate(100,10,'percent')
    self.assertEqual(10.0, result)