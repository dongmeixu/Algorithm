# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s:
            return False

        sign = False
        decimal = False
        hasE = False

        # 遍历
        for i in range(len(s)):
            if s[i] == "e" or s[i] == "E":
                # 1.e的后面必须有数字
                if i == len(s) - 1:
                    return False
                # 2.e必须只出现一次
                if hasE:
                    return False
                hasE = True
            elif s[i] == "+" or s[i] == "-":
                # 3.如果是第二次出现符号位，则前面一位必须是e
                if sign and i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
                # 3.如果第一次出现符号位，如果不是在开头，则前面也必须是e
                if not sign and i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
                sign = True
            elif s[i] == ".":
                # e的后面不能出现.
                if hasE or decimal:
                    return False
                decimal = True
            else:
                if s[i] > "9" or s[i] < "0":
                    return False

        if len(s) == 1:
            if sign or decimal or hasE:
                return False
        return True


# s = "+100"
s = "+100"
print()
print(Solution().isNumeric(s))
