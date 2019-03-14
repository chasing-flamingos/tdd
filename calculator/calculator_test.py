import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_negative(self):
        self.assertEqual(-3, calculator.negative(3))
        self.assertEqual(3, calculator.negative(-3))
        self.assertEqual(0, calculator.negative(0))

    def test_add(self):
        self.assertEqual(3, calculator.add(1, 2))

    def test_add_many_numbers(self):
        self.assertEqual(10, calculator.add(2, 2, 2, 2, 2))
        self.assertEqual(10, calculator.add(3, 4, 1, 2))
        self.assertEqual(0, calculator.add(0, 0, 0))
        self.assertEqual(1, calculator.add(1))

    def test_add_no_arguments(self):
        with self.assertRaises(RuntimeError) as cm:
            calculator.add()

        self.assertEqual(
            "add() needs at least one argument. None was given.",
            str(cm.exception)
        )

    def test_substract(self):
        self.assertEqual(2, calculator.substract(6, 4))
        self.assertEqual(6, calculator.substract(2, -4))
        self.assertEqual(-4, calculator.substract(-2, 2))
        self.assertEqual(0, calculator.substract(-2, -2))

    def test_substract_many_numbers(self):
        self.assertEqual(1, calculator.substract(10, 2, 3, 4))
        self.assertEqual(14, calculator.substract(5, -3, -4, -2))
        self.assertEqual(3, calculator.substract(2, 3, -4))
        self.assertEqual(0, calculator.substract(2, 2))
        self.assertEqual(1, calculator.substract(1))


if __name__ == '__main__':
    unittest.main()
