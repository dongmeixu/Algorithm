# coding=utf-8


def minCostClimbStairs(cost):
    n = len(cost)
    f = [0 for _ in range(n)]

    f[0] = cost[0]
    f[1] = cost[1]
    for i in range(2, n):
        f[i] = cost[i] + min(f[i - 1], f[i - 2])
    if f[n - 1] < f[n - 2]:  # 走这个台阶 or 不走这个台阶
        return f[n - 1]
    else:
        return f[n - 2]


cost = list(map(int, input().split(",")))
print(minCostClimbStairs(cost))
