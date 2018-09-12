# -*- coding:utf-8 -*-
class Solution:
    # 技巧 4个方向
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visited = []

    def hasPath(self, matrix, rows, cols, path):
        """
            :type board: List[List[str]]
            :type word: str
            :rtype: bool
            """
        m = rows
        n = cols

        board = [["" for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                board[i][j] = matrix[n * i + j]

        self.visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if self.search_word(board, path, 0, i, j):
                    return True
        return False

    def inArea(self, board, x, y):
        m = len(board)
        n = len(board[0])
        return 0 <= x < m and 0 <= y < n

    def search_word(self, board, word, index, startX, startY):
        # 递归截止条件
        if index == len(word) - 1:
            return board[startX][startY] == word[index]

        if board[startX][startY] == word[index]:
            self.visited[startX][startY] = True
            # 从startX, startY出发，向四个方向寻找
            for i in range(4):
                newx = startX + self.direction[i][0]
                newy = startY + self.direction[i][1]
                if self.inArea(board, newx, newy) and not self.visited[newx][newy]:
                    if self.search_word(board, word, index + 1, newx, newy):
                        return True

            self.visited[startX][startY] = False

        return False


# board = [
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E']
# ]
board = "ABCESFCSADEE"
word = "ABCB"
print(Solution().hasPath(board, 3, 4, word))

word = "ABCCED"
print(Solution().hasPath(board, 3, 4, word))

word = "SEE"
print(Solution().hasPath(board, 3, 4,  word))

word = "BCCED"
print(Solution().hasPath(board, 3, 4,  word))