"""
给定一组区间，问最少删除多少个区间，可以让这些区间之间互相不重叠
（最多保留多少个区间）

-给定区间的起始点永远小于终止点
-诸如区间[1, 2]和[2, 3],不叫做重叠

如[[1, 2], [2, 3], [3, 4], [1, 3]],算法返回1
如[[1, 2], [1, 2], [1, 2]]，算法返回2
"""

"""
暴力解法：找出所有子区间的组合，之后判断它不重叠 O(2 ^ n * n)

先要排序，方便判断不重叠
"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # DP超时了。。。。
    # def eraseOverlapIntervals(self, intervals):
    #     """
    #     :type intervals: List[Interval]
    #     :rtype: int
    #     """
    #     if not intervals:
    #         return 0
    #
    #     inter = []
    #     for interval in intervals:
    #         inter.append([interval.start, interval.end])
    #
    #     inter.sort()
    #
    #     # memo[i]表示使用intervals[0...i]的区间能构成的最长不重叠区间序列
    #     memo = [1] * len(inter)  # dp:状态
    #     for i in range(1, len(inter)):
    #         # memo[i]
    #         for j in range(i):
    #             if inter[i][0] >= inter[j][1]:
    #                 memo[i] = max(memo[i], 1 + memo[j])
    #
    #     res = 0
    #     for i in range(len(memo)):
    #         res = max(res, memo[i])
    #     return len(intervals) - res

    # 贪心算法
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        # 按结尾最早的升序排序
        inter = []
        for interval in intervals:
            inter.append([interval.start, interval.end])

        inter.sort()

        res = 1
        pre = 0
        for i in range(1, len(inter)):
            if inter[i][0] >= inter[pre][1]:
                res += 1
                pre = i
        return len(inter) - res


# intervals = [Interval(1, 2), Interval(1, 3), Interval(1, 2)]
intervals = [Interval(1, 2), Interval(2, 3), Interval(3, 4), Interval(1, 3)]
print(Solution().eraseOverlapIntervals(intervals))
