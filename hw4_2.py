def BinPow(a, n, f):
    res = a
    m = n - 1
    while m > 0:
        if m & 1:
            res = f(res, a)
            m -= 1

        else:
            a = f(a, a)
            m //= 2

    return res


exec(input())
