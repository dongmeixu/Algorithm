"""方法1：基于哈希表"""
# # -*- coding:utf-8 -*-
# class Solution:
#     # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
#     # 函数返回True/False
#     def duplicate(self, numbers, duplication):
#         # write code here
#         if not numbers:
#             return False
#
#         # 利用hashmap
#         hash_table = {}
#         for num in numbers:
#             hash_table[num] = hash_table.get(num, 0) + 1
#
#         for key, value in hash_table.items():
#             if value >= 2:
#                 duplication[0] = key
#                 return True
#         return False


"""方法2：改进的地方，在构建哈希表的时候就直接判断元素出现次数是否大于1"""
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False

        # 利用hashmap 时间复杂度O(n),空间复杂度O(n)
        hash_table = {}
        for num in numbers:
            if hash_table.get(num) != 0:
                hash_table[num] = 0
            else:
                duplication[0] = num
                return True
        return False