import math

num = int(input())
i = 2

while i<num:
    pw = math.log(num)/math.log(i)
    if pw-int(pw)==0:
        print('YES')
        break

    i+=1
else:
    print('NO')
    
        
    
