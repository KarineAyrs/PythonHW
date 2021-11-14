def chainslice(beg, end, *args):
    res = []
    i = 0
    for arg in args:
        for a in arg:
            if i >= end:
                break
            if i >= beg and i < end:
                res.append(a)
            i += 1

    return iter(res)
