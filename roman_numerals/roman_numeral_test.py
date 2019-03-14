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

    def test_symbol_combinations_for_I(self):
        self.assertEqual('II', str(RomanNumeral(2)))
        self.assertEqual('III', str(RomanNumeral(3)))

    def test_symbol_combinations_for_V(self):
        self.assertEqual('IV', str(RomanNumeral(4)))
        self.assertEqual('VI', str(RomanNumeral(6)))
        self.assertEqual('VII', str(RomanNumeral(7)))
        self.assertEqual('VIII', str(RomanNumeral(8)))

    def test_symbol_combinations_for_X(self):
        self.assertEqual('IX', str(RomanNumeral(9)))
        self.assertEqual('XX', str(RomanNumeral(20)))
        self.assertEqual('XXX', str(RomanNumeral(30)))

    def test_symbols_for_double_digits(self):
        self.assertEqual('XI', str(RomanNumeral(11)))
        self.assertEqual('XII', str(RomanNumeral(12)))
        self.assertEqual('XIII', str(RomanNumeral(13)))
        self.assertEqual('XIV', str(RomanNumeral(14)))
        self.assertEqual('XV', str(RomanNumeral(15)))
        self.assertEqual('XVI', str(RomanNumeral(16)))
        self.assertEqual('XVII', str(RomanNumeral(17)))
        self.assertEqual('XVIII', str(RomanNumeral(18)))
        self.assertEqual('XIX', str(RomanNumeral(19)))
        self.assertEqual('XXI', str(RomanNumeral(21)))
        self.assertEqual('XXXIV', str(RomanNumeral(34)))

    def test_symbol_combinations_for_L(self):
        self.assertEqual('LI', str(RomanNumeral(51)))
        self.assertEqual('LII', str(RomanNumeral(52)))
        self.assertEqual('LIII', str(RomanNumeral(53)))
        self.assertEqual('LIV', str(RomanNumeral(54)))
        self.assertEqual('LV', str(RomanNumeral(55)))
        self.assertEqual('LVI', str(RomanNumeral(56)))
        self.assertEqual('LVII', str(RomanNumeral(57)))
        self.assertEqual('LVIII', str(RomanNumeral(58)))
        self.assertEqual('LIX', str(RomanNumeral(59)))
        self.assertEqual('LX', str(RomanNumeral(60)))
        self.assertEqual('LXII', str(RomanNumeral(62)))
        self.assertEqual('LXXVI', str(RomanNumeral(76)))
        self.assertEqual('LXXXIX', str(RomanNumeral(89)))

if __name__ == '__main__':
    unittest.main()
