"""
2、对称子字符串的最大长度
输入一个字符串，输出该字符串中对称的子字符串的最大长度。比如输入字符串“google”，由于该字符串里最长的对称子字符串是“goog”，因此输出4。
提示：可能很多人都写过判断一个字符串是不是对称的函数，这个题目可以看成是该函数的加强版。
"""


class Solution:
    def longestPalindrome(self, s):
        if not s:
            return None

        # 对这个字符串做特殊处理
        T = self.preProcess(s)

        n = len(T)
        p = [0] * (2 * n - 1)

        C = 0
        R = 0
        for i in range(n - 1):
            i_mirror = 2 * C - 1
            p[i] = min(R - i, p[i_mirror]) if R > i else 0

            # attempt to expand palindrome centered at i
            while T[i + 1 + p[i]] == T[i - 1 - p[i]]:
                p[i] += 1

            if i + p[i] > R:
                C = i
                R = i + p[i]

        # find the max element in p
        maxLen = 0
        centerIndex = 0
        for i in range(1, n - 1):
            if p[i] > maxLen:
                maxLen = p[i]
                centerIndex = i
        del p

        # return s[(centerIndex - 1 - maxLen) >> 2: maxLen]
        return maxLen - (centerIndex - 1 - maxLen) // 2

    def preProcess(self, s):
        n = len(s)

        if n == 0:
            return "^$"

        ret = "^"
        for tmp in s:
            ret += "#" + tmp

        ret += "#$"
        return ret


print(Solution().longestPalindrome("googleef"))
