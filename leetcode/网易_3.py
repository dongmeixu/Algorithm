"""

描述：牛牛准备参加学校组织的春游，出发前牛牛准备往背包里装入一些零食，牛牛的背包容量为w
牛牛家里一共有n带零食，第i带零食体积为v[i]
牛牛想知道在总体积不超过背包容量的情况下，他一种有多少种零食方法（总体积为0也算一种放法）

输入描述：
输入包含两行
第一行为两个正整数n和w(1 <= n <= 30, 1 <= w <= 2 * 10^9)，表示零食的数量和背包的容量
第二行n个正整数v[i] (0<=v[i]<=10^9)，表示每袋零食的体积

输出描述：输出一个正整数，表示牛牛一共有多少种零食放法

示例：
输入
3 10
1 2 4

输出
8

"""

import numpy as np


def solve(vlist, wlist, totalWeight, totalLength):
    resArr = np.zeros((totalLength + 1, totalWeight + 1), dtype=np.int32)
    for i in range(1, totalLength + 1):
        for j in range(1, totalWeight + 1):
            if wlist[i] <= j:
                resArr[i, j] = max(resArr[i - 1, j - wlist[i]] + vlist[i], resArr[i - 1, j])
            else:
                resArr[i, j] = resArr[i - 1, j]
    return resArr[-1, -1]


if __name__ == '__main__':
    v = [0, 60, 100, 120]
    w = [0, 10, 20, 30]
    weight = 50
    n = 3
    result = solve(v, w, weight, n)
    print(result)
