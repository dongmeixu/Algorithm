"""
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。
求base的exponent次方。

"""


# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):  # O(n)
        # write code here
        result = 1.0

        if base == 0.0:
            return 0
        if exponent == 0:
            return 1
        for i in range(abs(exponent)):
            result *= base

        if exponent < 0:
            return 1 / result
        else:
            return result

    def Power_1(self, base, exponent):  # O(logn)
        # write code here
        if abs(base - 0.0) < 1e-6:
            return 0
        if exponent == 0:
            return 1
        # result = self.Power_1(base, exponent // 2)  # 栈溢出
        # result = pow(base, exponent >> 1)  # 用右移运算符代替了除以2
        result = base ** (exponent >> 1)
        result *= result
        if exponent & 1: # 用位与运算符代替了求余运算符（%）来判断一个数是奇数还是偶数。
            result *= base
        return result


print(Solution().Power_1(2, -3))
