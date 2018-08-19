import sys


class Solution:
    def strToInt(self, s):
        INT_MAX = sys.maxsize
        INT_MIN = - INT_MAX - 1

        num = 0
        # 1. 字符串为空，默认为0
        if not s:
            return 0

        # 2.符号位
        sign = 1

        # 3.去除空格
        i = 0
        while s[i] == " " and i < len(s):
            i += 1

        if s[i] == "+":
            i += 1
        else:
            assert s[i] == "-"
            sign = -1
            i += 1

        while i < len(s):
            # 4.非数字
            if s[i] < "0" or s[i] > "9":
                break
            # 5.溢出
            if num > INT_MAX / 10 or (num == INT_MAX / 10 and (int(str[i])) > INT_MAX % 10):
                if sign == -1:
                    return INT_MIN
                else:
                    return INT_MAX

            num = num * 10 + int(str[i])

        return num * sign


print("+13672242400000000000000000000000000")
