# -*- coding:utf-8 -*-
class Solution:
    # 4个方向
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visited = []

    def movingCount(self, threshold, rows, cols):
        # write code here
        self.visited = [[False for _ in range(cols)] for _ in range(rows)]

        return self.moving_dfs(threshold, 0, 0, rows, cols)

    def inArea(self, rows, cols, x, y):
        return 0 <= x < rows and 0 <= y < cols

    def checkSum(self, threshold, startX, startY):
        sum = 0
        while startX != 0:
            sum += startX % 10
            startX = startX / 10
        while startY != 0:
            sum += startY % 10
            startY = startY / 10

        if sum > threshold:
            return False
        else:
            return True

    def moving_dfs(self, threshold, startX, startY, rows, cols):
        if not self.inArea(rows, cols, startX, startY):
            return 0

        if self.visited[startX][startY] or not self.checkSum(threshold, startX, startY):
            return 0

        self.visited[startX][startY] = True
        for i in range(4):
            newx = startX + self.direction[i][0]
            newy = startY + self.direction[i][1]
        return 1 + self.moving_dfs(threshold, startX - 1, startY, rows, cols) + self.moving_dfs(threshold, startX,
                                                                                                startY + 1, rows,
                                                                                                cols) + self.moving_dfs(
            threshold, startX + 1, startY, rows, cols) + self.moving_dfs(threshold, startX, startY - 1, rows, cols)


print(Solution().movingCount(5, 10, 10))
