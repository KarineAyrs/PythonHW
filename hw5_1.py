from decimal import *
from decimal import Decimal as dec
from math import *

n_iter = 300
angle_grad = Decimal(input())
acc = int(input())

getcontext().prec = 1500

def factorial(n):
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def chudnovsky(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)))
        k += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi


pi = chudnovsky(100)

angle_rad = pi * Decimal(angle_grad) / Decimal(200)

def sin(x):
    res = 0

    for i in range(n_iter+1):
        sign = (-1) ** i
        power = x ** (2 * i + 1)
        divisor = factorial(2 * i + 1)
        res += sign * power / divisor

    return res


def cos(x):
    res = 0

    for i in range(n_iter+1):
        sign = (-1) ** i
        power = x ** (2 * i)
        divisor = factorial(2 * i)
        res += sign * power / divisor

    return res

def tan(x):
    return sin(x) / cos(x)

res = tan(dec(angle_rad))

with localcontext() as ctx:
    new_res = Context(prec=acc, Emax=999, clamp=1).create_decimal(res)
    print(new_res)