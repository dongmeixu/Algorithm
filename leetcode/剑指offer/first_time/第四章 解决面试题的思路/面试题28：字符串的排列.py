"""
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""


# -*- coding:utf-8 -*-
class Solution:
    res = []
    used = []

    def Permutation(self, ss):
        # write code here
        if not ss:
            return self.res
        ss = list(ss)
        self.used = [False] * len(ss)
        self.main(ss, 0, [])
        return self.res

    # 如果有重复元素就不对了。。。
    def main(self, s, index, p):
        if index == len(s):
            self.res.append("".join(p[:]))
        for i in range(len(s)):
            if not self.used[i]:
                p.append(s[i])
                self.used[i] = True
                self.main(s, index + 1, p)
                p.pop()
                self.used[i] = False


#         ss = list(ss)
#         res = []
#         if not ss:
#             return res
#         self.PermutationMain(ss, res, 0)
#         #print(res)
#         return res
#
#     def PermutationMain(self, ss, res, begin):
#         for i in range(begin, len(ss)):
#             if i != begin and ss[i] == ss[begin]:  # 遇到重复元素的情况
#                 continue
#             # 交换元素
#             a = ss[begin]
#             ss[begin] = ss[i]
#             ss[i] = a
#             # tmp用于记录当前交换后的字符串
#             tmp = ''.join(ss)
#             if tmp not in res and i == len(ss) - 1:
#                 res.append(tmp)
#             self.PermutationMain(ss[:], res, begin + 1)
#
#
# ss = "aa"
# print(len(ss))
# Solution().Permutation(ss)
print(Solution().Permutation("aba"))

import queue


class Solution:
    def Permutation(self, s):
        s_list = list(s)
        s_len = len(s_list)
        q1 = queue.Queue()
        q2 = queue.Queue()
        q1.put(s_list)

        for i in range(s_len - 1):
            if q1.empty():
                while not q2.empty():
                    s_list = q2.get()
                    q1.put(s_list)
                    c1 = s_list[i]
                    for j in range(i + 1, s_len):
                        c2 = s_list[j]
                        if c2 != c1:
                            temp = s_list[:]
                            temp[i] = c2
                            temp[j] = c1
                            q1.put(temp)
            else:
                while not q1.empty():
                    s_list = q1.get()
                    q2.put(s_list)
                    c1 = s_list[i]
                    for j in range(i + 1, s_len):
                        c2 = s_list[j]
                        if c2 != c1:
                            temp = s_list[:]
                            temp[i] = c2
                            temp[j] = c1
                            q2.put(temp)
        res = []
        if q1.empty():
            while not q2.empty():
                res.append(q2.get())
        else:
            while not q1.empty():
                res.append(q1.get())
        return res


print(Solution().Permutation("aba"))
