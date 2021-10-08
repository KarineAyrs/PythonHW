import math

x,y,r=eval(input())
a,b = eval(input())
f=False

while a!=0 or b!=0:
    if math.sqrt((x-a)**2+(y-b)**2)>r:
        f=True
    a,b=eval(input())

print('NO') if f else print('YES')

