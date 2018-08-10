"""
假设你想给小朋友饼干。
每个小朋友最多能够给一块饼干。
每个小朋友都有一个“贪心指数”，称为g(i),
g(i)

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.

"""
# 贪心算法
class Solution:
    def findContentChildren(self, g, s):
        # 首先对g, s排序-降序排序
        g.sort(reverse=True)
        s.sort(reverse=True)

        gi = 0
        si = 0
        res = 0

        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]: # 最大的那块饼干能分给最贪心的那个人
                res += 1
                si += 1
                gi += 1
            else:
                gi += 1
        return res




