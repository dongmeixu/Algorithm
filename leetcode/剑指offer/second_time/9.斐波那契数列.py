# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n < 0:
            return
        res = [0, 1, 1]
        for i in range(3, n + 1):
            res.append(res[-1] + res[-2])
        return res[n]


print(Solution().Fibonacci(-1))
