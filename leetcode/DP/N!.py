"""
N!
F(0) = F(1) = 1
F(n) = n * F(n - 1) 当且仅当 n>=2
"""

# 1.递归
def f_1(n):
    if n <= 1:
        return 1
    return n * f_1(n - 1)

# 2.计划搜索
def f_2(n):
    if n <= 1:
        return 1
    if result[n] > 0:
        return result[n]
    result[n] = n * f_2(n - 1)
    return result[n]

# 3.递推
def f_3(n):
    result = [1, 1]
    for i in range(2, n + 1):
        result.append(i * result[i - 1])
    return result[n]


if __name__ == '__main__':
    n = int(input())
    result = [0] * (n + 1)
    print(f_1(n))
    print(f_2(n))
    print(f_3(n))