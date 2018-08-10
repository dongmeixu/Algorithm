"""
N * M的棋盘上，小兵要从左下角走到右下角，
只能向上或者向右走，
问有多少种走法？
"""
# -*- coding:utf-8 -*-
import datetime
import numpy as np

##################### 1. 暴力搜索 #########################
def f1(n, m):
    # write code here
    if n == 0 or m == 0:
        return 0
    if n == 1 or m == 1:
        return 1
    return f1(n - 1, m) + f1(n, m - 1)

##################### 2. 记忆性搜索 #########################
def f2(n, m):
    # write code here
    if n == 0 or m == 0:
        return 0
    if n == 1 or m == 1:
        return 1
    if res[n][m] > 0:
        return res[n][m]
    res[n][m] = f2(n - 1, m) + f2(n, m - 1)
    return res[n][m]

##################### 3. 递推 #########################
def f3(n, m):
    # write code here
    if n == 0 or m == 0:
        return 0
    if n == 1 or m == 1:
        return 1

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            res[i][j] = res[i - 1][j] + res[i][j - 1]
    # print(res)
    return res[n][m]


"""
N * M的棋盘上，小兵要从左下角走到右下角，
只能向上或者向右走，
问有多少种走法？
附加条件：小兵向前冲，往上、右可以走1步或两步
"""

def f4(n, m):
    if n == 0 or m == 0:
        return 0
    if n == 1 or m == 1:
        return 1
    return f4(n - 1, m) + f4(n - 2, m) + f4(n, m - 1) + f4(n, m - 2)


def f5(n, m):
    if n == 0 or m == 0:
        return 0
    if n == 1 or m == 1:
        return 1
    if res_1[n][m] > 0:
        return res_1[n][m]
    res_1[n][m] = f5(n - 1, m) + f5(n - 2, m) + f5(n, m - 1) + f5(n, m - 2)

    return res_1[n][m]


def f6(n, m):
    if n == 0 or m == 0:
        return 0
    if n == 1 or m == 1:
        return 1
    res_1[1][1] = res_1[0][1] + res_1[1][0]
    # 不要忘了走到（2, 1）点会有走1步或者走2步的情况
    for i in range(2, n + 1):
        res_1[i][1] = res_1[i - 1][1] + res_1[i][0] + res_1[i - 2][1]
    for j in range(2, m + 1):
        res_1[1][j] = res_1[1][j - 1] + res_1[0][j] + res_1[1][j - 2];

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            res_1[i][j] = res_1[i - 1][j] + res_1[i - 2][j] + res_1[i][j - 1] + res_1[i][j - 2]
    # print(res_1)
    return res_1[n - 1][m - 1]  # 改成n-1和m-1就正确了


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    res = np.zeros((n + 1, m + 1))
    begin = datetime.datetime.now()
    fib = f1(n, m)
    print(fib)
    end = datetime.datetime.now()
    print(end - begin)

    begin = datetime.datetime.now()
    fib = f2(n, m)
    print(fib)
    end = datetime.datetime.now()
    print(end - begin)

    begin = datetime.datetime.now()
    res = np.ones((n + 1, m + 1))
    fib = f3(n, m)
    print(fib)
    end = datetime.datetime.now()
    print(end - begin)
    print("-----------------")

    begin = datetime.datetime.now()
    fib = f4(n, m)
    print(fib)
    end = datetime.datetime.now()
    print(end - begin)

    begin = datetime.datetime.now()
    res_1 = np.zeros((n + 1, m + 1))
    fib = f5(n, m)
    print(fib)
    end = datetime.datetime.now()
    print(end - begin)

    begin = datetime.datetime.now()
    res_1 = np.ones((n + 1, m + 1))
    fib = f6(n, m)
    print(fib)
    end = datetime.datetime.now()
    print(end - begin)