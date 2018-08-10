class Solution:
    def ReverseSeqence(self, s, bit):
        if not s:
            return ""

        if bit <= 0:
            return ""

        s = list(s)
        # 旋转整体
        self.Reverse(s, 0, len(s) - 1)

        # 左旋
        self.Reverse(s, 0, len(s) - 1 - bit)

        self.Reverse(s, len(s) - bit, len(s) - 1)
        return "".join(s)

    def Reverse(self, s, start, end):
        while start <= end:
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            start += 1
            end -= 1


print(Solution().ReverseSeqence("123456", 4))
