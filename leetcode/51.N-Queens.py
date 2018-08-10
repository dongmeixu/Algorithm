"""
求n皇后问题的所有解

n个皇后摆放在n*n的棋盘格中，使得横竖和两个对角线方向均不会同时出现两个皇后
"""

"""
快速判断不合法的情况
竖向：col[i]表示第i列被占用
对角线1：dia1[i]表示第i对角线1被占用   i + j
对角线2：dia2[i]表示第i对角线2被占用   i - j + n - 1
"""


class Solution:
    res = []
    col, dia1, dia2 = [], [], []

    def solveNQueens(self, n):
        self.res.clear()
        self.col.clear()
        self.dia1.clear()
        self.dia2.clear()
        # 初始化
        self.col = [False] * n
        self.dia1 = [False] * (2 * n - 1)
        self.dia2 = [False] * (2 * n - 1)

        self.putQueend(n, 0, [])
        return self.res

    # 尝试在一个n皇后问题中，摆放第index 行的皇后位置
    def putQueend(self, n, index, row):
        if index == n:
            self.res.append(self.generateBoard(n, row))
            # print(self.res)

        for i in range(n):
            # 尝试将第index行的皇后摆放在第一列
            if not self.col[i] and not self.dia1[index + i] and not self.dia2[index - i + n - 1]:
                row.append(i)
                self.col[i] = True
                self.dia1[index + i] = True
                self.dia2[index - i + n - 1] = True
                self.putQueend(n, index + 1, row)
                self.col[i] = False
                self.dia1[index + i] = False
                self.dia2[index - i + n - 1] = False
                row.pop()
        return

    def generateBoard(self, n, row):
        board = [["."] * n] * n
        for i in range(n):
            board[i][row[i]] = 'Q'
        return board


n = 4
res = Solution().solveNQueens(n)
for i in range(len(res)):
    for j in range(n):
        print(res[i][j])
    print("\n")




