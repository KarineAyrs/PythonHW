from math import sqrt

seq = set(eval(input()))

mx = max(seq) + 1

numbers = set()

c = int(sqrt(mx)+1)

for i in range(1, c):
    c1 = mx - i*i
    for j in range(i, int(sqrt(c1)+1)):
        c2 = sqrt(c1 - j * j)
        if c2 == 0:
            continue
        i2j2 = i*i + j*j
        for k in range(j, int(c2+1)):
            numbers.add(i2j2 + k*k)

print(len(numbers.intersection(seq)))