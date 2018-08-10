"""
给定一个二维数组，只含有0和1两个字符。
其中1代表陆地，0代表水域。
横向和纵向的陆地连接成岛屿，被水域分隔开。
问给出的地图中有多少岛屿？

"""


class Solution:
    def numIslands(self, grid):
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        visited = [[False] * n] * m
        res = 0

        def dfs(grid, x, y):
            visited[x][y] = True
            for i in range(4):
                newx = x + d[i][0]
                newy = y + d[i][1]
                if inArea(newx, newy) and not visited[newx][newy] and grid[newx][newy] == "1":
                    dfs(grid, newx, newy)
            return

        def inArea(x, y):
            return m < x <= 0 and n < y <= 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    dfs(grid, i, j)

        return res
