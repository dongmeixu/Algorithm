# -*- coding:utf-8 -*-

"""

思路：可以用一个循环打印矩阵，每次打印一圈


"""
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        m = len(matrix)  # 行数
        n = len(matrix[0])  # 列数
        left = 0
        top = 0
        right = n - 1
        bottom = m - 1
        print(m, n)
        result = []  # 用于保存数据
        while len(result) < m * n:
            if bottom < top:
                break
            if right < left:
                break

            # if m == 1:  # 只有1行
            #     return matrix[0]
            # if n == 1:  # 只有一列
            #     for i in range(m):
            #         result.extend(matrix[i])
            #     return result

            result.extend(matrix[top][left: right + 1])
            top += 1
            if bottom < top:  # 比如只有1行
                break

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            if right < left:  # 只有1列
                break

            # print(result)
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

            for j in range(bottom, top - 1, -1):
                # print(j)
                result.append(matrix[j][left])
            left += 1

        return result


s = Solution().printMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
s1 = Solution().printMatrix([[1], [2], [3]])
s2 = Solution().printMatrix(
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
print(s, s1)
print(s2)
