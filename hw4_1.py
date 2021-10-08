def divdigit(N):
    num = str(N)
    count = 0
    for i in num:
        if int(i)!=0 and N % int(i) == 0 :
            count += 1
    return count


eval(input())
