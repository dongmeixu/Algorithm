"""
题目描述
在一个二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


# 思路：
# 1.选取数组中右上角元素
# 2.如果该数字等于要查找的数字，查找结束，返回true
# 3.如果该数字大于要查找的数字，剔除这个数字所在的行
# 4.如果该数字小于要查找的数字，剔除这个数字所在的列

# 或者从左下角元素开始
# 不能从左上角或者右下角：
# 假设数字1位于初始数组的左上角，由于1小于目标7，那么7应该位于1的右边或者下边。
# 此时我们既不能从查找范围内剔除1所在的行，也不能剔除1所在的列，这样我们就无法缩小查找的范围

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        # 总的行数与列数（数组下标从0开始，所以减一）
        # 方式1：从左下角元素开始查找
        # rows = len(array) - 1
        # cols = len(array[0]) - 1
        # i = rows
        # j = 0
        # while j <= cols and i >= 0:
        #     if target > array[i][j]:
        #         j += 1
        #     elif target < array[i][j]:
        #         i -= 1
        #     else:
        #         return True
        # return False

        # 方式2：从右上角元素开始
        rows = len(array) - 1
        cols = len(array[0]) - 1

        i = 0
        j = cols

        while i <= rows and j >= 0:
            if target > array[i][j]:
                i += 1
            elif target < array[i][j]:
                j -= 1
            else:
                return True
        return False


array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
s = Solution().Find(0, array)
print(s)
