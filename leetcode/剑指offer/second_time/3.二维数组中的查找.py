"""

"""


# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:  # 列表为空
            return False

        # 从右上角或者左下角查找
        row = len(array) - 1
        col = len(array[0]) - 1

        i = 0
        j = col
        while i <= row and j >= 0:
            if target == array[i][j]:
                return True
            elif target > array[i][j]:
                i += 1
            else:
                j -= 1
        return False


array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
s = Solution().Find(0, array)
print(s)
