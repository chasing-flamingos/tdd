from math import floor

class RomanNumeral:

    def __init__(self, value = 0):
        self.value = value

    def __str__(self):
        if self.value in range(1, 4):
            return 'I' * self.value

        if self.value == 4:
            return str(RomanNumeral(1)) + str(RomanNumeral(5))

        if self.value in range(5, 9):
            return 'V' + str(RomanNumeral(self.value - 5))

        if self.value == 9:
            return str(RomanNumeral(1)) + str(RomanNumeral(10))

        if self.value in range(10, 40):
            return 'X' * floor(self.value / 10) + str(RomanNumeral(self.value % 10))

        if self.value in range(40, 50):
            return str(RomanNumeral(10)) + str(RomanNumeral(50)) + str(RomanNumeral(self.value % 10))

        if self.value in range(50, 90):
            return 'L' + str(RomanNumeral(self.value - 50))

        if self.value == 100:
            return 'C'

        if self.value == 500:
            return 'D'

        if self.value == 1000:
            return 'M'

        return ''
