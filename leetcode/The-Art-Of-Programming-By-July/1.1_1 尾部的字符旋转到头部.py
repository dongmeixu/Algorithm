"""
2、编写程序，在原字符串中把字符串尾部的m个字符移动到字符串的头部，要求：长度为n的字符串操作时间复杂度为O(n)，空间复杂度为O(1)。 例如，原字符串为”Ilovebaofeng”，m=7，输出结果为：”baofengIlove”。
"""


class Solution:
    def RightRotateString(self, s, m):
        if not s:
            return ""

        s = list(s)

        len_s = len(s)
        m %= len_s

        self.Reverse(s, 0, len_s - m - 1)  # s[0......len_s-m-1]
        self.Reverse(s, len_s - m, len_s - 1)
        self.Reverse(s, 0, len_s - 1)

        return "".join(s)

    def Reverse(self, s, left, right):
        while left <= right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -= 1
        return s


print(Solution().RightRotateString("ILovebaofeng", -1))
