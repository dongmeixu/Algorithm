"""
Write an efficient algorithm that searches for a value in an m×n matrix. This matrix has the following
properties:
• Integers in each row are sorted from left to right.
• The first integer of each row is greater than the last integer of the previous row.
"""


class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        # 从右上角查找
        rows = len(matrix)
        cols = len(matrix[0])
        i, j = 0, cols - 1

        while i < rows and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
print(Solution().searchMatrix(matrix, 3))
