class Triangle:

    def __init__(self, a=None, b=None, c=None):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self._empty = not self._check()

    def _check(self):
        return (self.a + self.b > self.c) and \
               (self.b + self.c > self.a) and \
               (self.a + self.c > self.b) and \
               self.a > 0 and self.b > 0 and \
               self.c > 0

    def __abs__(self):
        p = (self.a + self.b + self.c) / 2

        return 0 if self._empty else (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1 / 2)

    def __bool__(self):
        return self._check()

    def __eq__(self, other):
        l = [other.a, other.b, other.c]
        return (self.a in l) and (self.b in l) and (self.c in l)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __str__(self):
        return '{}:{}:{}'.format(self.a, self.b, self.c)
