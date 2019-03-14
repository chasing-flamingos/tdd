class RomanNumeral:

    def __init__(self, value = 0):
        self.value = value

    def __str__(self):
        if self.value == 1:
            return 'I'
        if self.value == 5:
            return 'V'
        if self.value == 10:
            return 'X'
        if self.value == 50:
            return 'L'
        if self.value == 100:
            return 'C'
        if self.value == 500:
            return 'D'
        if self.value == 1000:
            return 'M'
        return ''
