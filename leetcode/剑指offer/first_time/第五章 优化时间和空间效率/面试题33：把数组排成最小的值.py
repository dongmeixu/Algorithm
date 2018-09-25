"""
题目描述

    输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一
    个。例如输入数组 {3，32，321}，则打印出这三个数字能排成的最小数字为 321323。
"""
from filecmp import cmp

"""
解题思路：
可以看成是一个排序问题，在比较两个字符串 S1 和 S2 的大小时，
应该比较的是 S1+S2 和 S2+S1 的大小，
如果 S1+S2 < S2+S1，那么应该把 S1 排在前面，否则应该把 S2 排在前面。
"""

"""python3没通过"""
# -*- coding:utf-8 -*-
class Solution:
    # 方法1：排序，指定比较方式
    # def PrintMinNumber(self, numbers):
    #     # write code here
    #     if not numbers: return ""
    #     numbers = list(map(str, numbers))
    #     numbers.sort(cmp=lambda x, y: cmp(x + y, y + x))
    #     return "".join(numbers).lstrip('0') or '0'

    # 方法2：全排列
    def PrintMinNumber_1(self, numbers):
        if not numbers:
            return ""
        used = [False] * len(numbers)
        res = self.dfs(numbers, 0, [], [], used)
        return min(res)

    def dfs(self, numbers, index, tmp, res, used):
        if len(tmp) == len(numbers):
            res.append("".join(list(map(str, tmp[:]))))
            return

        for i in range(len(numbers)):
            if not used[i]:
                tmp.append(numbers[i])
                used[i] = True
                self.dfs(numbers, index + 1, tmp, res, used)
                tmp.pop()
                used[i] = False
        return res


numbers = [3, 32, 321]
# print(Solution().PrintMinNumber(numbers))
print(Solution().PrintMinNumber_1(numbers))
