def SpiralDigit(m, n):
  arr = [[-1]*m for j in range(n)]
  row, col = 0, 0
  col_step, row_step = 1, 0
  for i in range(n * m):
    arr[row][col] = i % 10
    new_row, new_col = row + row_step, col + col_step
    if 0 <= new_row < n and 0 <= new_col < m and arr[new_row][new_col] == -1:
      row, col = new_row, new_col
    else:
      col_step, row_step = -row_step, col_step
      row, col = row + row_step, col + col_step
  
  for i in range(len(arr)):
    print(*arr[i])

m,n=eval(input())
SpiralDigit(m,n)
