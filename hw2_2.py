num=int(input())
q = 0
n=num

while num>0:
    mod=int(num%10)
    q=q*10+mod
    num=num//10

print('YES') if n==q else print('NO')
