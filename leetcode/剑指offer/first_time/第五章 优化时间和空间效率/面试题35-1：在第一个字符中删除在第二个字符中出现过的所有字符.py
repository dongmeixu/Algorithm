"""

题目描述：
    定义一个函数，输入两个字符串，从第一个字符串中删除在第二个字符串
    中出现过的所有字符。
    例如从第一个字符串"we are students." 中删除在第二个字符串
    “aeiou”中出现过的字符得到的结果是”w r stdnts.“

"""

"""
思路：
    为了解决这个问题，我们可以创建一个用数组实现的简单哈希表来存储
    第二个字符串。这样我们从头到尾扫描第一个字符串的每一个字符时，用
    O(1)时间就能判断出该字符是不是在第二个字符中。如果第一个字符串
    的长度是n,那么总的时间复杂度是O(n)
"""
import collections
class Solution:
    def sovle(self, string1, string2):
        hashTable = dict(collections.Counter(string2))
        # print(hashTable)
        string1 = list(string1)

        if not string1:
            return ""
        for s in string1:
            if s in hashTable.keys():
                string1.remove(s)

        # print(string1)
        return ''.join(string1)


string1 = "we are students."
# string2 = "aeiou"
# string1 = ""
string2 = ""
print(Solution().sovle(string1, string2))