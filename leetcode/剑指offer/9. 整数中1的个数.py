# -*- coding:utf-8 -*-
"""
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

思路： 将10进制转化为2进制，将ob 以及0用空代替，最后直接统计字符串的长度即可
"""
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n < 0:
            bin_n = bin(2 ** 32 + n)
        else:
            bin_n = bin(n)
        bin_n = bin_n.split("b")[1]
        return len(str(bin_n).replace("0", ""))


count = Solution().NumberOf1(10)
print(count)
count = Solution().NumberOf1(-2)
print(count)