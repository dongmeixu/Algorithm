"""
在数学上，斐波纳契数列以如下被以递归的方法定义：
F(0)=0，F(1)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）

斐波那契数列：0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

"""
##################### 1. 暴力搜索 #########################
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n
        return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)


##################### 2. 计划搜索 #########################
# -*- coding:utf-8 -*-
class Solution1:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n
        if result[n] > 0:
            return result[n]
        result[n] = self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
        return result[n]


##################### 3. 递推 #########################
# -*- coding:utf-8 -*-
class Solution2:
    def Fibonacci(self, n):
        # write code here
        # if n <= 1:
        #     return n
        # result = [1, 1]
        # for i in range(2, n):
        #     result.append(result[-1] + result[-2])
        # return result[-1]
        res = [0, 1, 1, 2]
        while len(res) < n:
            res.append(res[-1] + res[-2])
        return res[n]


if __name__ == '__main__':
    n = int(input())
    result = [0] * (n + 1)
    fib = Solution1().Fibonacci(n)
    print(fib)