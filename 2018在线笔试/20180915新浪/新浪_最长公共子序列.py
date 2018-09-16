def lcs(x, y):
    lenx = len(x)
    leny = len(y)
    c = [[0 for _ in range(leny + 1)] for j in range(lenx + 1)]
    res = 0
    for i in range(lenx):
        for j in range(leny):
            if x[i] == y[j]:
                c[i + 1][j + 1] = c[i][j] + 1
            elif c[i + 1][j] > c[i][j + 1]:
                c[i + 1][j + 1] = c[i + 1][j]
            else:
                c[i + 1][j + 1] = c[i][j + 1]
            res = max(res, c[i + 1][j + 1])
    return res


x = input()
y = input()
print(lcs(x, y))

# 时间复杂度T(n) = O(len(x) * len(y))
