N = int(input())

point = []

while N:
    x, y = input().strip().split()
    point.append([int(x), int(y)])
    N -= 1

# 所有点按照y轴按降序排序
point.sort(key=lambda x: x[1], reverse=True)

res = [point[0]]
for i in range(1, len(point)):
    # 如果当前点的x值大于res最大点的x值，则加入res
    if point[i][0] > res[-1][0]:
        res.append(point[i])

res.sort(key=lambda x: x[0])
for i in range(len(res)):
    print('{} {}'.format(res[i][0], res[i][1]))
