"""
对于一个字符串，我们想通过添加字符的方式使得新的字符串整体变成回文串，但是只能在原串的结尾添加字符，请返回在结尾添加的最短字符串。

给定原字符串A及它的长度n，请返回添加的字符串。保证原串不是回文串。

测试样例：
"ab",2
返回："a"
"""


# -*- coding:utf-8 -*-

class Palindrome:
    def pre_process(self, s):
        if not s:
            return "#"

        res = "#"
        for tmp in s:
            res += tmp
            res += "#"

        return res

    def addToPalindrome(self, A, n):
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
        return "".join(A_res)