import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(13, 7), 20)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(13, 7), 6)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(0, 1), 0)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
    def test_divide(self):
        self.assertEqual(self.calc.divide(21, 3), 7)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(8, 0), None)