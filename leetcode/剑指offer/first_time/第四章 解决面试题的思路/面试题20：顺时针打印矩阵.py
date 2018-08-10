# -*- coding:utf-8 -*-
"""
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
     则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

"""
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        rows = len(matrix)  # 行数
        cols = len(matrix[0])  # 列数

        top = 0  # 代表第一行
        left = 0  # 代表第一列
        bottom = rows - 1  # 代表最后一行
        right = cols - 1  # 代表最后一列

        print(rows, cols)
        res = []

        while len(res) < rows * cols:
            if bottom < top:
                break
            if right < left:
                break

            res.extend(matrix[top][left: right + 1])  # 遍历1
            top += 1  # 代表下一行
            if top > bottom:  # 比如只有1行的情况
                break
            for i in range(top, bottom + 1):  # 遍历2
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            for i in range(right, left - 1, -1):  # 遍历3
                res.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom, top - 1, -1):  # 遍历3
                res.append(matrix[i][left])
            left += 1
        print(res)
        return res


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Solution().printMatrix(matrix)
