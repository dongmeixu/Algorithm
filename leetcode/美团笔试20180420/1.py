import sys


def gcd(m, n):
    if not m:
        return n
    elif not n:
        return m
    elif m is n:
        return m
    while m % n:
        m, n = n, m % n
    return n


N, n, m, p = list(map(int, raw_input().split()))
gcd_list = []
for i in range(1, n + 1):
    for j in range(1, m + 1):
        gcd_list.append(gcd(i, j))
gcd_list.sort()
A = [p]
for i in range(gcd_list[-1] - 1):
    A.append((A[-1] + 153) % p)
res = 0
for index in gcd_list:
    res += A[index - 1]
sys.stdout.write(str(res) + "\n")
