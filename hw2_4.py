k=int(input())

for i in range(1000):
    
    cond = (k * 10 ** i - k**2) % (10*k-1) == 0
    ans = int(((k * 10 ** i - k**2)//(10*k-1))*10+k)
    if cond:        
        print("{:d}".format(ans)) 
        break
