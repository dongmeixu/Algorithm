"""
1、第一个只出现一次的字符
在一个字符串中找到第一个只出现一次的字符。如输入abaccdeff，则输出b。
"""
import collections


class Solution:
    def OnlyOnce(self, s):
        # 为空
        if not s:
            return -1

        map = collections.OrderedDict()

        for tmp in s:
            map[tmp] = map.get(tmp, 0) + 1

        for key, value in map.items():
            if value == 1:
                return key
        return -1


print(Solution().OnlyOnce("abaccdeff"))
print(Solution().OnlyOnce("uujjhh"))