class Dots:
    def __init__(self, beg, end):
        self.beg = beg
        self.end = end

    def __getitem__(self, item):

        if isinstance(item, slice):
            if item.step is None:
                h = (self.end - self.beg) / (item.stop - 1)
                return self.beg + item.start * h
            else:
                start = 0 if item.start is None else item.start
                stop = item.step if item.stop is None else item.stop

                h = (self.end - self.beg) / (item.step - 1)
                return (self.beg + i * h for i in range(start, stop))

        else:
            h = (self.end - self.beg) / (item - 1)
            b = self.beg + 0.0
            l = []
            while b <= self.end:
                l.append(b)
                b += h

            return l

