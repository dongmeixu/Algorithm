"""
最大连续乘积子串

题目描述

给一个浮点数序列，取最大乘积连续子串的值，例如 -2.5，4，0，3，0.5，8，-1，则取出的最大乘积连续子串为3，0.5，8。也就是说，上述数组中，3 0.5 8这3个数的乘积30.58=12是最大的，而且是连续的。
"""


# 解法一: 最简单粗暴的方式：两个for循环直接轮询。时间复杂度O(n^2)
class Solution:
    def sovle(self, arr):
        if not arr:
            return 0

        max_sum = arr[0]
        index_begin = index_end = 0

        for i in range(len(arr)):
            tmp_sum = 1
            for j in range(i, len(arr)):
                tmp_sum *= arr[j]
                if tmp_sum > max_sum:
                    max_sum = tmp_sum
                    index_begin = i
                    index_end = j

        return max_sum, arr[index_begin: index_end + 1]

    """
    解法2: 动态规划求解的方法一个for循环搞定，所以时间复杂度为O(n)。
    假设数组为a[]，直接利用动态规划来求解，考虑到可能存在负数的情况，我们用maxend来表示以a[i]结尾的最大连续子串的乘积值，用minend表示以a[i]结尾的最小的子串的乘积值，那么状态转移方程为：
        maxend = max(max(maxend * a[i], minend * a[i]), a[i]);
        minend = min(min(maxend * a[i], minend * a[i]), a[i]);
    """

    def sovle_1(self, arr):
        if not arr:
            return 0

        # 初始化
        maxEnd = arr[0]
        minEnd = arr[0]
        maxResult = arr[0]

        for i in range(1, len(arr)):
            maxEnd = max(max(maxEnd * arr[i], minEnd * arr[i]), arr[i])
            minEnd = min(min(maxEnd * arr[i], minEnd * arr[i]), arr[i])
            maxResult = max(maxResult, maxEnd)
        return maxResult

    def FindGreatestSumOfSubArray(self, array):
        # write code here
        ret = -1  # 最大值
        sum = 1  # 乘积
        for item in array:
            if sum <= 0:
                sum = item
            else:
                sum *= item
            ret = ret if ret > sum else sum  # 更新最大值

        return ret


print(Solution().sovle([-2.5, 4, 0, 3, 0.5, 8, -1]))
print(Solution().sovle_1([-2.5, 4, 0, 3, 0.5, 8, -1]))
print(Solution().FindGreatestSumOfSubArray([-2.5, 4, 0, 3, 0.5, 8, -1]))
