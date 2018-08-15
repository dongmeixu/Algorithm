"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [−2,1,−3,4,−1,2,1,−5,4], the contiguous subarray [4,−1,2,1] has
the largest sum = 6.
"""
import sys
# 动态规划 对于数组中的元素而言，有2种状态

class Solution:
    def maxSubArray(self, arr):
        if not arr:
            return

        res = -(sys.maxsize + 1)
        f = 0
        for i in range(len(arr)):
            f = max(f + arr[i], arr[i])
            res = max(res, f)
        return res


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
