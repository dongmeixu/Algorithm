# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):  # O(logn)
        # write code here
        # 特殊情况
        if abs(base - 0.0) > 1e6 or exponent == 0:
            return 1

        abs_exponent = abs(exponent)
        res = base * (abs_exponent >> 1)
        res *= res
        if abs_exponent & 1 == 1:  # 奇数
            res *= base
        if exponent < 0:
            return 1 / res
        else:
            return res


print(Solution().Power(2, -3))
