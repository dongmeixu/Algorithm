"""
Longest Palindromic Substring Part II
– LeetCode https://articles.leetcode.com/longest-palindromic-substring-part-ii/


"""


# class Solution:
#     def longestPalindrome(self, s):
#         if not s:
#             return None
#
#         # 对这个字符串做特殊处理
#         T = self.preProcess(s)
#         print(T)
#
#         n = len(T)
#         p = [0] * (2 * n - 1)
#
#         C = 0
#         R = 0
#         for i in range(n - 1):
#             i_mirror = 2 * C - 1
#             p[i] = min(R - i, p[i_mirror]) if R > i else 0
#
#             # attempt to expand palindrome centered at i
#             while T[i + 1 + p[i]] == T[i - 1 - p[i]]:
#                 p[i] += 1
#
#             if i + p[i] > R:
#                 C = i
#                 R = i + p[i]
#
#         # find the max element in p
#         maxLen = 0
#         centerIndex = 0
#         for i in range(1, n - 1):
#             if p[i] > maxLen:
#                 maxLen = p[i]
#                 centerIndex = i
#         del p
#
#         return s[(centerIndex - 1 - maxLen) >> 2: maxLen]
#
#     def preProcess(self, s):
#         n = len(s)
#
#         if n == 0:
#             return "^$"
#
#         ret = "^"
#         for tmp in s:
#             ret += "#" + tmp
#
#         ret += "#$"
#         return ret
#

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
        orig_index = current_index >> 1
        orig_len = long_len >> 1

        ss = orig_index + orig_len - 1
        print(ss)
        # print(orig_index, orig_len)
        # print(A[orig_index - orig_len + 1: orig_index + orig_len])
        if ss == 0:
            A_res = list(A[:ss + 1])
        elif ss == n - 1 and orig_index - orig_len + 1 != 0:
            A_res = list(A[:orig_index - orig_len + 1])
        else:
            j = ss
            # 判断该回文子串下一个元素是否跟该回文的最后一个元素相等
            for i in range(j, -1, -1):
                if j < n:
                    if A[i] != A[j]:
                        j = i
                        break
                    else:
                        j += 1

            A_res = list(A[:j + 1])
        A_res.reverse()
        return long_len - 1, A[orig_index - orig_len:], "".join(A_res)

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

# 问题分解
# 1、找到最长的回文子串
# 2、剩余部分就是需要添加的子串


nums = list(map(int, input().split()))
nums_len = len(nums)
max_val = [nums[-1]] * nums_len
min_val = [nums[0]] * nums_len
for i in range(nums_len - 2, -1, -1):
    max_val[i] = max(max_val[i + 1], nums[i])
for j in range(1, nums_len):
    min_val[j] = min(min_val[j - 1], nums[j])
max_differ = max_val[1] - min_val[0]
for i in range(2, nums_len):
    max_differ = max(max_val[i] - min_val[i], max_differ)
print(max_differ)



