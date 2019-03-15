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

    def test_symbols_for_numbers_between_forty_and_fifty(self):
        self.assertEqual('XL', str(RomanNumeral(40)))
        self.assertEqual('XLI', str(RomanNumeral(41)))
        self.assertEqual('XLII', str(RomanNumeral(42)))
        self.assertEqual('XLIII', str(RomanNumeral(43)))
        self.assertEqual('XLIV', str(RomanNumeral(44)))
        self.assertEqual('XLV', str(RomanNumeral(45)))
        self.assertEqual('XLVI', str(RomanNumeral(46)))
        self.assertEqual('XLVII', str(RomanNumeral(47)))
        self.assertEqual('XLVIII', str(RomanNumeral(48)))
        self.assertEqual('XLIX', str(RomanNumeral(49)))

    def test_symbols_for_numbers_between_ninety_and_hundred(self):
        self.assertEqual('XC', str(RomanNumeral(90)))
        self.assertEqual('XCI', str(RomanNumeral(91)))
        self.assertEqual('XCII', str(RomanNumeral(92)))
        self.assertEqual('XCIII', str(RomanNumeral(93)))
        self.assertEqual('XCIV', str(RomanNumeral(94)))
        self.assertEqual('XCV', str(RomanNumeral(95)))
        self.assertEqual('XCVI', str(RomanNumeral(96)))
        self.assertEqual('XCVII', str(RomanNumeral(97)))
        self.assertEqual('XCVIII', str(RomanNumeral(98)))
        self.assertEqual('XCIX', str(RomanNumeral(99)))

    def test_symbols_for_numbers_between_hundred_and_four_hundred(self):
        self.assertEqual('CI', str(RomanNumeral(101)))
        self.assertEqual('CII', str(RomanNumeral(102)))
        self.assertEqual('CV', str(RomanNumeral(105)))
        self.assertEqual('CIX', str(RomanNumeral(109)))
        self.assertEqual('CL', str(RomanNumeral(150)))
        self.assertEqual('CC', str(RomanNumeral(200)))
        self.assertEqual('CCI', str(RomanNumeral(201)))
        self.assertEqual('CCXCIX', str(RomanNumeral(299)))
        self.assertEqual('CCC', str(RomanNumeral(300)))
        self.assertEqual('CCCI', str(RomanNumeral(301)))
        self.assertEqual('CCCXCIX', str(RomanNumeral(399)))

    def test_symbols_for_numbers_between_four_hundred_and_five_hundred(self):
        self.assertEqual('CD', str(RomanNumeral(400)))
        self.assertEqual('CDI', str(RomanNumeral(401)))
        self.assertEqual('CDV', str(RomanNumeral(405)))
        self.assertEqual('CDX', str(RomanNumeral(410)))
        self.assertEqual('CDL', str(RomanNumeral(450)))
        self.assertEqual('CDXCIX', str(RomanNumeral(499)))

if __name__ == '__main__':
    unittest.main()
