"""
Longest Palindromic Substring Part II
– LeetCode https://articles.leetcode.com/longest-palindromic-substring-part-ii/


"""


class Solution:
    def longestPalindrome(self, s):
        if not s:
            return None

        # 对这个字符串做特殊处理
        T = self.preProcess(s)
        print(T)

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

        return s[(centerIndex - 1 - maxLen) >> 2: maxLen]

    def preProcess(self, s):
        n = len(s)

        if n == 0:
            return "^$"

        ret = "^"
        for tmp in s:
            ret += "#" + tmp

        ret += "#$"
        return ret


print(Solution().longestPalindrome("abaaba"))
