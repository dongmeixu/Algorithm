"""
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。

"""


# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array:
            return []

        pEven = 0  # 指向偶数的指针
        pOdd = len(array) - 1  # 指向奇数的指针

        while pEven < pOdd:
            # 向后移动pEven,直至指向偶数
            while array[pEven] & 1 != 0:
                pEven += 1
            # 向前移动pOdd,直至指向奇数
            while array[pOdd] & 1 == 0:
                pOdd -= 1

            if pEven < pOdd:
                tmp = array[pOdd]
                array[pOdd] = array[pEven]
                array[pEven] = tmp

        return array

    def reOrderArray_1(self, array):
        # write code here
        newArray = []
        if not array:
            return newArray
        for item in array:
            if item & 1 == 1:
                newArray.append(item)
        for item in array:
            if item & 1 == 0:
                newArray.append(item)
        return newArray


array = [1, 2, 3, 4, 5]
print(Solution().reOrderArray(array))
array = [1, 2, 3, 4, 5]
print(Solution().reOrderArray_1(array))
