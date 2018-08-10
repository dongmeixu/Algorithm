import numpy as np


class Solution:
    # 技巧 4个方向
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visited = []

    def exist(self, board, word):
        """
            :type board: List[List[str]]
            :type word: str
            :rtype: bool
            """
        m = len(board)
        n = len(board[0])
        self.visited = list(np.array([[False] * n] * m))

        for i in range(m):
            for j in range(n):
                if self.search_word(board, word, 0, i, j):
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
                newx = self.direction[i][0]
                newy = self.direction[i][1]
                if self.inArea(board, newx, newy) and not self.visited[newx][newy]:
                    if self.search_word(board, word, index + 1, newx, newy):
                        return True

                self.visited[startX][startY] = False

        return False


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

word = "ABCB"
print(Solution().exist(board, word))

word = "ABCCED"
print(Solution().exist(board, word))

word = "SEE"
print(Solution().exist(board, word))
