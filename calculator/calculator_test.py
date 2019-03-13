import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(3, calculator.add(1, 2))

    def test_negative(self):
        self.assertEqual(-3, calculator.negative(3))
        self.assertEqual(3, calculator.negative(-3))
        self.assertEqual(0, calculator.negative(0))

if __name__ == '__main__':
    unittest.main()
