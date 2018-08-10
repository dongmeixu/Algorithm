"""
奇偶调序

题目描述

输入一个整数数组，调整数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
要求时间复杂度为O(n)。
"""


# 基于快排
class Solution:
    def OddEvenSort(self, arr):
        if not arr:
            return

        left = 0
        right = len(arr) - 1

        while left <= right:
            if arr[left] & 1 != 0:  # 是奇数，则继续往后扫描
                left += 1
            elif arr[right] & 1 == 0:  # 是偶数，则继续往前扫描
                right -= 1
            else:  # 交换
                tmp = arr[left]
                arr[left] = arr[right]
                arr[right] = tmp
        return arr


print(Solution().OddEvenSort([1, 2, 3, 4]))
