"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

"""

"""


思路：首先我们选择从左下角开始搜寻，
(为什么不从左上角开始搜寻，左上角向右和向下都是递增，那么对于一个点，对于向右和向下会产生一个岔路；
如果我们选择从左下脚开始搜寻的话，如果大于就向右，如果小于就向下)。

"""
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        # 总的行数与列数（数组下标从0开始，所以减一）
        rows = len(array) -1
        cols = len(array[0]) - 1
        i = rows
        j = 0
        while j <= cols and i >= 0:
            if target > array[i][j]:
                j += 1
            elif target < array[i][j]:
                i -= 1
            else:
                return True
        return False

s = Solution().Find(2, [[1, 2, 3], [4, 5, 6]])
print(s)