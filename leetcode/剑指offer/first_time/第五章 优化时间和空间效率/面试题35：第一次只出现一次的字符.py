"""
题目描述：在字符串中找出第一个只出现一次的字符。如输入"abaccdeff"，则输出‘b’

"""

"""
思路：
    如果需要判断多个字符是不是在某个字符串里出现过或者统计多个字符在某个字符串中出现的次数，我们可以考虑基于数组创建一个简单的哈希表。这样可以用很小的空间消耗换来时间效率的提升。
"""
import collections


# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:  # 字符串为空
            return -1

        hashTable = dict(collections.Counter(s).items())

        for id, item in enumerate(s):
            if hashTable[item] == 1:
                return item
            """底下这2句话出错是因为位置写错了。。。。
            应该写在循环外面，
            当遍历完整个数组都没有找到，则返回-1"""
            # else:    # 加上这2句话，牛客AC不了
            #     return -1
        return -1

    def FirstNotRepeatingChar_map(self, s):
        # write code here
        if not s:  # 字符串为空
            return -1

        # 有个问题：如果是普通的字典，它是无序的，如果输入中包含多个只出现一次的元素就会出错的
        map = collections.OrderedDict()
        for tmp in s:
            map[tmp] = map.get(tmp, 0) + 1

        for key, value in map.items():
            if map[key] == 1:
                return key
        return -1
        # hashTable = dict(collections.Counter(s).items())
        #
        # for id, item in enumerate(s):
        #     if hashTable[item] == 1:
        #         return id
        #     # else:    # 加上这2句话，牛客AC不了
        #     #     return -1


s = 'abccbooseexdad'
print(Solution().FirstNotRepeatingChar(s))
