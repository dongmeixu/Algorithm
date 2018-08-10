# -*- coding:utf-8 -*-
"""

题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方

"""
class Solution:
    def Power(self, base, exponent):
        # write code here
        return base ** exponent
    """
    1-原始做法：时间复杂度O(exponent)
    """
    def Power_1(self, base, exponent):
        # write code here
        result = 1.0
        if base == 0.0:
            result = 0.0
        if exponent < 0:
            e = -exponent
        else:
            e = exponent
        for i in range(e):
            result *= base
        if exponent < 0:
            return 1 / result
        else:
            return result

    """
    2-二分改进
    
    举例：求3^5
    3^5 = 3^2 * 3^2 * 3 （当指数为奇数的时候）
    3^4 = 3^2 * 3^2（当指数为偶数的时候）
    这样就根据奇数幂和偶数幂来分成了2半，故得到了2个公式：
    
    x^n = x^(n/2) * x^(n/2). (n为偶数) 
    x^n = x^(n/2) * x^(n/2) * x. (n为奇数) 
    
    判断一个数是不是奇数：
    b & 1表示了b的奇偶性，奇数返回1，偶数返回0；相当于b % 2 == 1
    """

    def Power_2(self, base, exponent):
        # write code here
        if exponent == 1:
            return base
        if base == 0.0:
            return 0.0
        if exponent & 1:
            return pow(base, exponent / 2) * pow(base, exponent / 2) * base
        else:
            return pow(base, exponent / 2) * pow(base, exponent / 2)



# S = Solution().Power(0, -2)
# print(S)

S_1 = Solution().Power_1(-1, 1)
print(S_1)

S_1 = Solution().Power_2(-1.0, 1)
print(S_1)