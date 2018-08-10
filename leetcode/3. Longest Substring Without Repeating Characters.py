class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        start = 0
        max_length = 0
        # 判断list中是否包含重复值
        # if len(set(s)) == length:
        #     return length
        for i, sub in enumerate(s):
            print(i, sub)
            if sub in used and start <= used[sub]:
                start = used[sub] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[sub] = i
        return max_length


ss = Solution().lengthOfLongestSubstring("abcabcbb")
print(ss)


""""

python 中判断一个列表里面是否有重复值
参考网址：
    1. http://blog.csdn.net/together_cz/article/details/77493952
    2. http://www.pythoner.com/205.html
    
"""

from collections import Counter


def fun_1(num_list):
    if len(set(num_list)) == len(num_list):
        print("无重复值")
    else:
        print("有重复值")


def fun_2(num_list):
    c = Counter(num_list)
    top_1 = c.most_common(1)
    print(top_1)
    if top_1[0][1] != 1:
        print("有重复值")
    else:
        print("无重复值")


lists = [['a', 'b', 'c'], [2, 2, 3]]
for list in lists:
    fun_1(list)
    print("*" * 30)
    fun_2(list)