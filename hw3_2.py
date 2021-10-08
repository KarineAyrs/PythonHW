data = eval(input())
x = []
for elem in data:
  x.append([elem[0], False])
  x.append([elem[1], True])
x.sort()

result = 0
c = 0
for i in range(len(x)):
  if c != 0:
    result = result + x[i][0] - x[i-1][0]
  if x[i][1]:
    c = c + 1
  else:
    c = c - 1

print(result)
