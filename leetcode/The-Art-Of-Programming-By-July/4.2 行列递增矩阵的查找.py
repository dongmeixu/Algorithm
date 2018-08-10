"""

题目描述

在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

"""

"""
有序。。。。找到初始比较查找的位置，然后用二分法继续查找，每次查找都会将查找范围缩小
"""


class Solution:
    def matrixSearch(self, matrix, target):
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])

        # 右上角的数字
        row, col = 0, n - 1
        while row < m and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1
        return False


#test
# matrix = [[1, 2, 3], [4, 5, 6]]
matrix = []
print(Solution().matrixSearch(matrix, 0))
