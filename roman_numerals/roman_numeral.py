class RomanNumeral:

    def __init__(self, value = 0):
        self.value = value

    def __str__(self):
        if self.value in range(1, 4):
            return 'I' * self.value
        if self.value == 4:
            return str(RomanNumeral(1)) + str(RomanNumeral(5))
        if self.value == 5:
            return 'V'
        if self.value in range(6, 9):
            return str(RomanNumeral(5)) + str(RomanNumeral(self.value - 5))
        if self.value == 9:
            return str(RomanNumeral(1)) + str(RomanNumeral(10))
        if self.value == 10:
            return 'X'
        if self.value == 20:
            return 'XX'
        if self.value == 30:
            return 'XXX'
        if self.value == 50:
            return 'L'
        if self.value == 100:
            return 'C'
        if self.value == 500:
            return 'D'
        if self.value == 1000:
            return 'M'
        return ''
