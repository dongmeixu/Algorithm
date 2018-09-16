"""
区间统计

时间限制：C/C++语言 2000MS；其他语言 4000MS
内存限制：C/C++语言 131072KB；其他语言 655360KB
题目描述：
小明拿到了一个数列a1 , a2 , ... an ，小明想知道存在多少个区间[l,r]同时满足下列两个条件：
1、r-l+1=k;
2、在a l , a l+1,...ar中，存在一个数至少出现了 t 次。
输出满足条件的区间个数。
输入
输入第一行三个整数n,k,t(1≤n,k,t≤105。
第二行 n 个整数，a1 , a2 , ... an (1≤ai≤105)。
输出
输出一个数，问题的答案。

样例输入
5 3 2
3 1 1 1 2
样例输出
3


"""
n, k, t = list(map(int, input().split()))
a = list(map(int, input().split()))

res = 0

for l in range(n - t):
    r = l + k - 1

    if r == n or r - l < t:
        break

    sub_a = a[l:r+1]
    for num in set(sub_a):
        if sub_a.count(num) >= t:
            res += 1
            break
print(res)


def dfs(adj, start):
    visited = set()
    stack = [[start, 0]]
    while stack:
        (v, next_child_idx) = stack[-1]
        if (v not in adj) or (next_child_idx >= len(adj[v])):
            stack.pop()
            continue
        next_child = adj[v][next_child_idx]
        stack[-1][1] += 1
        if next_child in visited:
            continue
        print(next_child)
        visited.add(next_child)
        stack.append([next_child, 0])


graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
dfs(graph, 1)
