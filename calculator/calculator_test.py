import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(3, calculator.add(1, 2))

if __name__ == '__main__':
    unittest.main()
