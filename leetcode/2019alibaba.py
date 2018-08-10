
class Solution:
    res = [] # 保存结果
    map = []
    minStep = float('inf')

    def solution(self, N, M, map):
        dis = 0
        for i in range(N):
            for j in range(N):
                # 求i->j的最短路径
                self.dfs(i, j, N, M, dis, 0)
                map[i][j] = self.minStep
                self.minStep = float('inf')
        return map

    def dfs(self, start, end, N, M, dis, steps):
        if steps == M:
            # 刚刚好 M步 到达所需要的end 且路径较短，则更新数值
            if start == end and dis < self.minStep:
                # 更新
                self.minStep = dis
            return

        for next in range(N):
            if next == start:
                continue
            radis = dis + self.map[start][next]
            self.dfs(next, end, N, M, radis, steps + 1)


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    x = input()

    map = [[0] * n] * m  # 初始化
    dp = Solution().solution(n, m, map)
    print(dp)


    map = []
    for i in range(n):
        line = [int(x) for x in input().split()]
        map.append(list(line))
    dp = [list(x) for x in map]  # 一维列表浅拷贝用list(),二维列表浅拷贝用[list(x) for x in dp]  三维用[[list(i) for i in x] for x in dp]
    last_dp = [list(x) for x in map]
    for k in range(m - 1):  # 共循环m-1轮，每一次循环后的dp矩阵元素代表i和j之间的长度为m的最短路径
        for i in range(n):
            for j in range(n):
                tmp = [last_dp[i][x] + map[x][j] for x in range(n) if x != i and x != j]
                dp[i][j] = min(tmp)
        # copy
        last_dp = [list(x) for x in dp]

    print(dp)