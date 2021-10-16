def fill_square(field, X,Y, s,c):
  for j in range(X, X+s):
    for i in range(Y, Y+s):
      field[i][j]=c


def squares(w,h, *args): 
    
  field = [['.']*w for i in range(h)]
  for ar in args:
    fill_square(field, ar[0], ar[1],ar[2],ar[3])
  for l in field:
    print(''.join(l))


exec(input())
