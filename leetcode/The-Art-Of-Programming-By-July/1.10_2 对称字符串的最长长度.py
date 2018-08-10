"""
2、对称子字符串的最大长度
输入一个字符串，输出该字符串中对称的子字符串的最大长度。比如输入字符串“google”，由于该字符串里最长的对称子字符串是“goog”，因此输出4。
提示：可能很多人都写过判断一个字符串是不是对称的函数，这个题目可以看成是该函数的加强版。
"""
class Solution:
    def longLength(self, s):
        if not s:
            return 0

        for i in range(len(s)):
            pass
