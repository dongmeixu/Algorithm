# TODO:没有考虑字符串如果含有非数字元素怎么办
class Solution:
    def StrToInt(self, s):
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
            res = res * 10 + int(s[i])
            i += 1

        return sign * res


print(Solution().StrToInt("-123n"))
