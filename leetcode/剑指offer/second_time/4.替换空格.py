# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if not s:
            return ""

        s = list(s)

        # 找出空格的个数
        numOfBlank = 0
        for tmp in s:
            if tmp == " ":
                numOfBlank += 1
        newLength = len(s) + numOfBlank * 2

        newStringList = [" "] * newLength

        pNew = newLength - 1
        pOld = len(s) - 1

        while pOld != pNew:
            if s[pOld] != " ":
                newStringList[pNew] = s[pOld]
                pNew -= 1
                pOld -= 1
            else:
                newStringList[pNew] = "0"
                newStringList[pNew - 1] = "2"
                newStringList[pNew - 2] = "%"
                pNew -= 3
                pOld -= 1
        while pOld > -1:
            newStringList[pNew] = s[pOld]
            pNew -= 1
            pOld -= 1

        return "".join(newStringList)


s = "I am a goog student"
print(Solution().replaceSpace(s))
