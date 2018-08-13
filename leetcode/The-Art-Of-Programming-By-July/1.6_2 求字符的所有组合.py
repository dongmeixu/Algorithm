"""
2、如果不是求字符的所有排列，而是求字符的所有组合，应该怎么办呢？
当输入的字符串中含有相同的字符串时，相同的字符交换位置是不同的排列，但是同一个组合。
举个例子，如果输入abc，它的组合有a、b、c、ab、ac、bc、abc。
"""

"""
求组合的问题，跟求排列的问题类似，很容易的想到递归的实现方式。

在求一个字符串中所有字符的组合的时候，针对一个字符，有两种情况，假设在长度为n的字符串中选择长度为m的组合字符串，

第一是选择长度为n的字符串中的第一个字符，那么要在其余的长度n-1的字符串中选择m-1个字符

第二是不选择长度为n的字符串中的第一个字符，那么要在其余的长度n-1的字符串中选择m个字符

递归结束的条件就是，当m为0，即从字符串中不再选出字符的时候，这个时候已经找到了m个字符的组合，输出即可。还有一个条件是，当输入的

字符串是串，自然是不能从中选出任何字符的。

"""


class Solution:
    result = []

    def Combination(self, s):
        if not s:
            return
        # s = list(s)
        res = []
        for i in range(1, len(s) + 1):
            self.Combination_main(s, i, res)
        return max(self.result)

    # 从字符串s中选择m个字符
    def Combination_main(self, s, m, res):
        # m=0,递归结束，输出当前结果
        if m == 0:
            # print("".join(res))
            # print(res)
            chengji = int(min(res)) * int(sum(res))

            print(chengji)
            self.result.append(chengji)
            return
        if len(s) != 0:
            # 选择当前元素
            res.append(s[0])
            self.Combination_main(s[1:], m - 1, res)
            # 不选择当前元素
            res.pop()
            self.Combination_main(s[1:], m, res)


print(Solution().Combination([6, 2, 1]))
