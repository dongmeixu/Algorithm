# 1. 设计暴力搜索算法，找到冗余------->超时

def search(idx, M):
    if idx < 0 or M == 0: # idx的下标是从0开始的！！！！！
        return 0
    if weights[idx] > M:  # 某个物体的重量大于能承受的总重量，弃了
        return search(idx - 1, M)
    if idx >= 0 and M >= weights[idx]:
        return max(values[idx] + search(idx - 1, M - weights[idx]), search(idx - 1, M))


def search1(idx, M):
    if idx < 0 or M == 0:
        return 0
    if weights[idx] > M:
        return search(idx - 1, M)
    if result[idx] > 0:
        return result[idx]
    if idx >= 0 and M >= weights[idx]:
        result[idx] = max(values[idx] + search(idx - 1, M - weights[idx]), search(idx - 1, M))
    return result[-1]

def search2(idx, M):
    if idx < 0 or M == 0:
        return 0
    for i in range(1, N):
        for j in range(1, M):
            result[i][j] = max(values[i - 1] + result[i - 1][j - weights[i - 1]], result[i - 1][j])
    return result[N - 1][M - 1]


import numpy as np
N, M = list(map(int, input().split()))
weights = []
values = []
# result = [0] * N
result = np.zeros((N + 1, M + 1))
for i in range(N):
    w, p = list(map(int, input().split()))
    weights.append(w)
    values.append(p)
print(weights, values)
s = search2(N - 1, M)
print(s)






