import unittest
from roman_numeral import RomanNumeral

class TestRomanNumeral(unittest.TestCase):

    def test_default_value_is_null(self):
        self.assertEqual('', str(RomanNumeral()))

if __name__ == '__main__':
    unittest.main()
