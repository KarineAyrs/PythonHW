def LookSay():
    s = [1]
    while True:
        s2 = []
        cnt = 0
        prev = 0
        for el in s:
            yield el
            if not prev:
                prev = el
                cnt = 1
            elif prev == el:
                cnt += 1
            else:
                s2.append(cnt)
                s2.append(prev)
                prev = el
                cnt = 1
        s2.append(cnt)
        s2.append(prev)
        s = s2
    # las = '1'
    # while True:
    #     new_las = ''
    #     count = 0
    #     prev = ''
    #     for i in range(len(las)):
    #         yield las[i]
    #         if prev == '':
    #             prev = las[i]
    #             count = 1
    #         elif prev == las[i]:
    #             count += 1
    #         else:
    #             new_las += str(count) + prev
    #             prev = las[i]
    #             count = 1
    #
    #     new_las += str(count) + prev
    #     las = new_las
    #


for i, l in enumerate(LookSay()):
    print(f"{i}: {l}")
    if i > 50:
        break
