from fractions import Fraction


class Sausage:
    def __init__(self, meat='pork!', vol=1.0):
        self.meat = meat
        self.vol = Fraction(vol)

    def __str__(self):
        v = int(self.vol * 12)
        row_count = 12 // len(self.meat) + 1
        full_pieces = v // 12
        rem = v % 12
        if v == 0:
            return '/|\n||\n||\n||\n\\|'
        envelop_up = '/' + '-' * 12 + '\\'
        row = '|' + (self.meat * row_count)[:12] + '|'
        envelop_down = '\\' + '-' * 12 + '/'

        long_row = full_pieces * row + ((row[:rem + 1] + '|') if rem > 0 else '')
        long_env_up = full_pieces * envelop_up + ((envelop_up[:rem + 1] + '|') if rem > 0 else '')
        long_env_down = full_pieces * envelop_down + ((envelop_down[:rem + 1] + '|') if rem > 0 else '')

        return long_env_up + '\n' + (long_row + '\n') * 3 + long_env_down

    def __abs__(self):
        return self.vol

    def __add__(self, other):
        return Sausage(self.meat, self.vol + abs(other))

    def __mul__(self, other):
        return Sausage(self.meat, self.vol * other)

    def __rmul__(self, other):
        return Sausage(self.meat, self.vol * other)

    def __truediv__(self, other):
        return Sausage(self.meat, self.vol / other)

    def __sub__(self, other):
        return Sausage(self.meat, 0.0 if abs(self) - abs(other) <= 0.0 else abs(self) - abs(other))

    def __bool__(self):
        return self.vol > 0.0

