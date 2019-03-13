import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(3, calculator.add(1, 2))

    def test_negative(self):
        self.assertEqual(-3, calculator.negative(3))
        self.assertEqual(3, calculator.negative(-3))
        self.assertEqual(0, calculator.negative(0))

    def test_substract(self):
        self.assertEqual(2, calculator.substract(6, 4))
        self.assertEqual(6, calculator.substract(2, -4))
        self.assertEqual(-4, calculator.substract(-2, 2))
        self.assertEqual(0, calculator.substract(-2, -2))

if __name__ == '__main__':
    unittest.main()
