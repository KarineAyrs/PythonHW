def mark_square(_i: int, _j: int, _strings: list, _visited: list):
    for i in range(_i, len(_strings)):
        _row = _strings[i]
        for j in range(_j, len(_strings[0])):
            if _strings[i][_j] == '.':
                return
            if _strings[i][j] == '.':
                break
            _visited[i][j] = 1

strings = list()

input()
while True:
    string = input()
    if string[0] == '-':
        break
    strings.append(string)

x = len(strings)
y = len(strings[0])

count = int(0)

visited = [[0] * y for _ in range(x)]

for i in range(x):
    row = strings[i]
    for j in range(y):
        if row[j] == '.':
            visited[i][j] = 1
            continue
        if row[j] == '#' and not visited[i][j]:
            count += 1
            mark_square(i, j, strings, visited)

print(count)
