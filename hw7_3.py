import random


def randomes(seq):
    beg_ends = []
    for par in seq:
        par_els = [v for v in par]
        beg_ends.append(par_els)
        yield random.randint(par_els[0], par_els[1])

    while True:
        for el in beg_ends:
            yield random.randint(el[0], el[1])
