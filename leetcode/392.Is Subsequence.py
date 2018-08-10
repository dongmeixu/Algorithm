"""
给定两个字符串s和t,问s是不是t的子序列
-如 s="abc", t="ahbgdc"，则s是t的子序列，算法返回true
-如 s="axc"，t="ahbgdc"，则s不是t的子序列，算法返回false
"""

# 贪心算法
class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = list(s)
        t_list = list(t)

        si = 0
        ti = 0
        res = 0
        while si < len(s_list) and ti < len(t_list):
            if s_list[si] == t_list[ti]:
                si += 1
                ti += 1
                res += 1
            else:
                ti += 1
        if res == len(s_list):
            return True
        else:
            return False


s = "abc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))
