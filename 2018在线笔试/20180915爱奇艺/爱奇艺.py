def chooseNoodles(noodles):
    if not noodles:
        return
    noodles.sort(key=lambda x: x[1])  # 将面条的右端点升序排序

    res = [False] * len(noodles)

    idx = []
    res[0] = True
    pre = 0
    idx.append(0)
    for i in range(1, len(noodles)):
        if noodles[i][0] >= noodles[pre][1]:
            res[i] = True
            pre = i
            idx.append(i)
    # print(idx)
    c = 0
    for i in range(len(res)):
        if res[i]:
            c += 1
    # return c, res
    return c


noodles = []
N = int(input())
for _ in range(N):
    start, end = list(map(str, input().split()))
    if int(start) < int(end):
        noodles.append([int(start), int(end)])
    else:
        noodles.append([int(end), int(start)])
print(chooseNoodles(noodles))
