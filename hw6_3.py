from collections import defaultdict

d = defaultdict(set)

string = str()

lst = list()

entrance = str()
exit_ = str()

while True:
    string = input()

    if ' ' not in string:
        entrance = string
        exit_ = input()
        break

    s = string.split(' ')
    d[s[0]].add(s[1])
    d[s[1]].add(s[0])


def bfs(v):
    visited = set()
    q = list()

    q.append(v)
    while len(q) != 0:
        cur_v = q.pop(-1)
        visited.add(cur_v)

        if cur_v == exit_:
            break

        childs = d[cur_v]
        for child in childs:
            if child not in visited:
                q.append(child)

    return 'YES' if exit_ in visited else 'NO'


print(bfs(entrance))
