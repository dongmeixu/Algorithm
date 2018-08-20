import sys


class Solution:
    def StrToInt(self, s):
        INT_MAX = sys.maxsize
        INT_MIN = -INT_MAX - 1

        # 字符串为空
        # s = list(s)
        if not s:
            return 0

        # 用于保存最后的结果
        res = 0
        # 符号位,默认是正数
        sign = 1

        i = 0  # i用来代表第一个数字所在的位置
        # 判断字符串的最高位是否是符号位，是的话看下是正数还是负数
        if s[i] == "-":
            sign = -1
            i += 1  # 第一个数字位
        elif s[i] == "+":
            i += 1

        if not s[i:].isdigit():
            return 0

        while i < len(s):
            # 5.溢出
            if res > INT_MAX / 10 or (res == INT_MAX / 10 and (int(str[i])) > INT_MAX % 10):
                if sign == -1:
                    return INT_MIN
                else:
                    return INT_MAX
            res = res * 10 + int(s[i])
            i += 1

        return sign * res


print(Solution().StrToInt("+1235555555555555550989"))
