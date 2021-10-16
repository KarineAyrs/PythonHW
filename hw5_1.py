from decimal import *

def fact(n):
  if n==0:
    return 1
  res=1
  for i in range(1,n+1):
    res*=i
  
  return res

def pi(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k)*(Decimal(fact(6*k))/((fact(k)**3)*(fact(3*k)))* (13591409+545140134*k)/(640320**(3*k)))
        k += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi


def cos(x):
  sum = 0

  for n in range(40):
    sum+=(x**(2*n)*(-1)**n)/fact(2*n)
    
  return sum


def tan(x):  
  cs = cos(x)
  sin=(1-cs**Decimal(2))**Decimal(0.5) 
  return sin/cs

A = input()
E=input()
getcontext().prec = int(E)
X = Decimal(A)*pi(100)/Decimal(200)
getcontext().rounding = ROUND_DOWN
print(tan(X))
