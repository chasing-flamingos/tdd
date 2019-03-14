import unittest
from roman_numeral import RomanNumeral

class TestRomanNumeral(unittest.TestCase):

    def test_default_value_is_null(self):
        self.assertEqual('', str(RomanNumeral()))

    def test_one_symbol_is_I(self):
        self.assertEqual('I', str(RomanNumeral(1)))

    def test_five_symbol_is_V(self):
        self.assertEqual('V', str(RomanNumeral(5)))

    def test_ten_symbol_is_X(self):
        self.assertEqual('X', str(RomanNumeral(10)))

    def test_fifty_symbol_is_L(self):
        self.assertEqual('L', str(RomanNumeral(50)))

    def test_hundred_symbol_is_C(self):
        self.assertEqual('C', str(RomanNumeral(100)))

    def test_five_hundred_symbol_is_D(self):
        self.assertEqual('D', str(RomanNumeral(500)))

    def test_thousand_sybol_is_M(self):
        self.assertEqual('M', str(RomanNumeral(1000)))

if __name__ == '__main__':
    unittest.main()
