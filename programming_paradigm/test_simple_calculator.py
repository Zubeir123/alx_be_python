import unittest
from simple_calculator import SimpleCalculator

calc = SimpleCalculator()

class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(13, 7), 20)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
    def test_subtract(self):
        self.assertEqual(calc.subtract(13, 7), 6)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
    def test_multiply(self):
        self.assertEqual(calc.multiply(0, 1), 0)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
    def test_divide(self):
        self.assertEqual(calc.divide(21, 3), 7)
        self.assertEqual(calc.divide(0, 1), 0)
        self.assertEqual(calc.divide(8, 0), None)