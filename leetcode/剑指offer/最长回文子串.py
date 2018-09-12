"""
对于一个字符串，请设计一个高效算法，计算其中最长回文子串的长度。

给定字符串A以及它的长度n，请返回最长回文子串的长度。

测试样例：
"abc1234321ab",12
返回：7
"""


# -*- coding:utf-8 -*-

class Palindrome:
    def getLongestPalindrome(self, A, n):
        # write code here
        if len(A) != n:
            return 0
        T = self.pre_process(A)

        pArr = [1 for _ in range(2 * n + 1)]
        pR = 0  # 回文右边界的下一个元素
        index = 0  # 回文中心

        long_len = 0
        current_index = 0

        for i in range(1, 2 * n):
            i_mirror = 2 * index - i
            if i < pR:
                if i_mirror >= 0:  # 说明i在以index为回文中心的回文范围内
                    pArr[i] = min(pArr[i_mirror], pR - i)
            else:
                pArr[i] = 1

            # 开始扩
            while i + pArr[i] < 2 * n + 1 and i - pArr[i] > -1 and T[i + pArr[i]] == T[i - pArr[i]]:
                pArr[i] += 1

            # 看是否需要更新pR
            if pArr[i] + i > pR:  # 新的回文半径长度大于之前的回文右边界
                pR = i + pArr[i]  # 回文右边界更新
                index = i  # 回文中心更新

            if pArr[i] > long_len:
                long_len = pArr[i]
                current_index = i

        orig_center = current_index >> 1
        orig_len = (long_len - 1) >> 1
        return long_len - 1, A[orig_center - orig_len: orig_center + orig_len + 1]

    def pre_process(self, s):
        if not s:
            return "#"

        res = "#"
        for tmp in s:
            res += tmp
            res += "#"

        return res


print(Palindrome().getLongestPalindrome("abbbbbaa", 8))
print(Palindrome().getLongestPalindrome("ab", 2))
print(Palindrome().getLongestPalindrome("bbabbaaabba", 11))
