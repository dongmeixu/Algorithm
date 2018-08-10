"""
题目描述
给定一个字符串，要求把字符串前面的若干个字符移动到字符串的尾部，如把字符串“abcdef”前面的2个字符'a'和'b'移动到字符串的尾部，使得原字符串变成字符串“cdefab”。请写一个函数完成此功能，要求对长度为n的字符串操作的时间复杂度为 O(n)，空间复杂度为 O(1)。
"""


class Solution:
    # 解法一：暴力移位法  一位一位的移动到末尾 时间复杂度O(mn), 空间复杂度O(1)
    def LeftShiftOne(self, s):
        if not s:
            return ""
        s = list(s)
        first = s[0]
        for i in range(1, len(s)):
            s[i - 1] = s[i]
        s[len(s) - 1] = first

    def LeftRotateString(self, s, m):
        while m:
            self.LeftShiftOne(s)
            m -= 1
        return "".join(s)

    # 解法二：三步反转法
    def LeftRotateString_1(self, s, bit):
        s_copy = list(s)
        if not s:
            return ""
        len_s = len(s)
        bit %= len_s
        if bit == 0:
            return s

        # self.Reverse(s_copy, 0, len_s - 1)
        # self.Reverse(s_copy, 0, len_s - bit - 1)
        # self.Reverse(s_copy, len_s - bit, len_s - 1)

        self.Reverse(s_copy, 0, bit - 1)
        self.Reverse(s_copy, bit, len_s - 1)
        self.Reverse(s_copy, 0, len_s - 1)

        return "".join(s_copy)

    def Reverse(self, s, left, right):
        while left <= right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -= 1
        return s


# s = "Ilovebaofeng"
s = "abcdef"
print(Solution().LeftRotateString_1(s, 7))
