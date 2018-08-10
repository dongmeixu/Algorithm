"""
题目：在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
    输入一个数组，求出这个数组中的逆序对的总数

思路：
    归并算法

"""


# -*- coding:utf-8 -*-
# class Solution:
#     def InversePairs(self, data):
#         # write code here
#         if not data:
#             return 0
#
#         length = len(data)
#
#         copy = data.copy()
#
#         count = self.InversePairs_Main(data, copy, 0, length - 1)
#
#         del copy
#         return count
#
#     def InversePairs_Main(self, data, copy, start, end):
#         if start == end:
#             return 0
#         mid = end + (end - start) // 2
#
#         left = self.InversePairs_Main(copy, data, start, start + mid)
#         right = self.InversePairs_Main(copy, data, start + mid + 1, end)
#
#         # i初始化为前半段最后一个数字的下标
#         i = start + mid
#
#         # j初始化为后半段最后一个数字的下标
#         j = end
#         indexCopy = end
#         count = 0
#
#         while i >= start and j >= start + mid + 1:
#             if data[i] > data[j]:
#                 copy[indexCopy] = data[i]
#                 indexCopy -= 1
#                 i -= 1
#                 count += j - start - mid
#
#             else:
#                 copy[indexCopy] = data[j]
#                 indexCopy -= 1
#                 j -= 1
#
#         for i in range(start + 1, -1):
#             copy[indexCopy] = data[i]
#             indexCopy -= 1
#
#         for j in range(start + mid + 1, -1):
#             copy[indexCopy] = data[j]
#             indexCopy -= 1
#
#         return left + right + count

class Solution:
    cnt = 0
    tmp = []

    def InversePairs(self, data):
        # write code here
        if not data:
            return 0

        length = len(data)

        self.tmp = data.copy()

        self.mergeSortUp2Down(data, 0, length - 1)

        return int(self.cnt % 1000000007)

    def mergeSortUp2Down(self, nums, first, last):
        if last - first < 1:
            return

        mid = first + (last - first) // 2
        self.mergeSortUp2Down(nums, first, mid)
        self.mergeSortUp2Down(nums, mid + 1, last)
        self.merge(nums, first, mid, last)

    def merge(self, nums, first, mid, last):
        i = first
        j = mid + 1
        k = first
        while i <= mid or j <= last:
            if i > mid:
                self.tmp[k] = nums[j]
                j += 1
            elif j > last:
                self.tmp[k] = nums[i]
                i += 1
            else:
                self.tmp[k] = nums[j]
                j += 1
                self.cnt += mid - i + 1  # nums[i] > nums[j],说明nums[i...mid] 都大于nums[j]
            k += 1

        for k in range(first, last + 1):
            nums[k] = self.tmp[k]


arr = [1, 2, 3, 4, 5, 6, 7, 0]
print(Solution().InversePairs(arr))
