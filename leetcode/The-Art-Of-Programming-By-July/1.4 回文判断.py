"""
回文判断

题目描述

回文，英文palindrome，指一个顺着读和反过来读都一样的字符串，比如madam、我爱我，这样的短句在智力性、趣味性和艺术性上都颇有特色，中国历史上还有很多有趣的回文诗。
那么，我们的第一个问题就是：判断一个字串是否是回文？
"""


# 解法1：设置2个指针（头指针、尾指针），从两端向中间扫描字符串，如果所有字符都一样，则是回文
# 时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def IsPalindrome(self, s):
        s = list(s)
        if not s:
            return False

        start = 0
        end = len(s) - 1

        while start <= end:
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True


print(Solution().IsPalindrome("we"))
