# -*- coding:utf-8 -*-
# class Solution:
#     # 返回对应char
#     s = "google"
#
#     def FirstAppearingOnce(self):
#         # write code here
#         if not self.s:
#             return "#"
#
#         char_list = list(self.s)
#
#         hash_table = {}
#         for c in char_list:
#             hash_table[c] = hash_table.get(c, 0) + 1
#         for key, value in hash_table.items():
#             if value == 1:
#                 return key
#                 print(key)
#         return "#"
#
#     def Insert(self, char):
#         # write code here
#         self.s += char

class Solution:
    def __init__(self):
        self.s = "google"

    def FirstAppearingOnce(self):
        res = list(filter(lambda c: self.s.count(c) == 1, self.s))
        print(res)
        return res[0] if res else "#"


    def Insert(self, char):
        self.s += char


print(Solution().FirstAppearingOnce())
