"""

题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

"""
# -*- coding:utf-8 -*-
class Solution:

    """
    思路：新建一个数组先把原数组中的奇数push进去再把偶数push进去，然后用新数组数据覆盖原数组即可
    复杂度O(n)

    """
    def reOrderArray(self, array):
        # write code here
        new_array = []
        for ele in array:
            if ele & 1 == 1:
                new_array.append(ele)

        for ele in array:
            if ele & 1 == 0:
                new_array.append(ele)
        return new_array.copy()

    
Solution().reOrderArray([2,4,1,5])