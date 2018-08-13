"""
在数学上，斐波纳契数列以如下被以递归的方法定义：
F(0)=0，F(1)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）

斐波那契数列：0, 1, 1， 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

"""


##################### 1. 暴力搜索 #########################
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)


##################### 2. 计划搜索 #########################
# -*- coding:utf-8 -*-
class Solution1:
    def Fibonacci(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if res[n] > 0:
            return res[n]
        res[n] = self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
        return res[n]


##################### 3. 递推 #########################
# -*- coding:utf-8 -*-
class Solution2:
    def Fibonacci(self, n):
        res = [0, 1]
        while len(res) <= n:
            res.append(res[-1] + res[-2])
        return res[n]


if __name__ == '__main__':
    n = 3
    res = [0] * (n + 1)
    print(Solution().Fibonacci(n))
    print(Solution1().Fibonacci(n))
    print(Solution2().Fibonacci(n))
