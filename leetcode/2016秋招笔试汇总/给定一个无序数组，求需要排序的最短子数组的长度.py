"""
给定一个无序数组，求需要排序的最短子数组的长度
"""


class Solution:
    def shortestLen(self, arr, n):
        if not arr or not n:
            return 0

        max = arr[0]
        index_right = 0
        for i in range(1, n):
            if max > arr[i]:
                index_right = i
            else:
                max = arr[i]

        min = arr[-1]
        index_left = 0
        for i in range(n - 2, -1, -1):
            if min > arr[i]:
                min = arr[i]
            else:
                index_left = i

        return index_right - index_left + 1


arr = [1, 5, 3, 4, 2, 6, 7]
print(Solution().shortestLen(arr, len(arr)))
