class RomanNumeral:

    def __init__(self, value = 0):
        self.value = value

    def __str__(self):
        if self.value == 1:
            return 'I'
        if self.value == 5:
            return 'V'
        return ''
