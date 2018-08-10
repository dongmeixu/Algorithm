# # -*- coding:utf-8 -*-
# class Solution:
#     def Fibonacci(self, n):
#         # write code here
#         """方法1：递归不行，栈会溢出"""
#         # if n >= 2:
#         #     return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
#         # else:
#         #     return n
#         """方法2：用循环，最好不用递归"""
#         # recode = [1, 1]
#         # if n <= 1:
#         #     return n
#         # else:
#         #     for i in range(2, n):
#         #         recode.append(recode[-1] + recode[-2])
#         #     return recode[n - 1]
#         """
#         别人写的循环
#         链接：https: // www.nowcoder.com / questionTerminal / c6c7742f5ba7442aada113136ddea0c3
#         来源：牛客网
#         """
#         res = [0, 1, 1, 2]
#         while len(res) <= n:
#             res.append(res[-1] + res[-2])
#         return res[n]
#
# s = Solution().Fibonacci(5)
# print(s)

#
# # 尾递归示例
# def Fib(n, b1=1, b2=1, c=3):
#     if n < 3:
#         return 1
#     else:
#         if n == c:
#             return b1 + b2
#         else:
#             return Fib(n, b1=b2, b2=b1 + b2, c=c + 1)
#
#
# s = Fib(1001)
# print(s)
# # 当调用1002时就报错了
# # s = Fib(1002)
# # print(s)
#
# # 下面进行尾递归优化，使用这个方法以后Python的递归调用再也不用受到调用栈长度的制约
# import sys
#
#
# class TailRecurseException:
#     def __init__(self, args, kwargs):
#         self.args = args
#         self.kwargs = kwargs
#
#
# def tail_call_optimized(g):
#     """
#     This function decorates a function with tail call
#     optimization. It does this by throwing an exception
#     if it is it's own grandparent, and catching such
#     exceptions to fake the tail call optimization.
#
#     This function fails if the decorated
#     function recurses in a non-tail context.
#     """
#
#     def func(*args, **kwargs):
#         f = sys._getframe()
#         if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
#             raise TailRecurseException(args, kwargs)
#         else:
#             while 1:
#                 try:
#                     return g(*args, **kwargs)
#                 except TailRecurseException, e:
#                     args = e.args
#                     kwargs = e.kwargs
#
#     func.__doc__ = g.__doc__
#     return func
#
#
# @tail_call_optimized
# def Fib(n, b1=1, b2=1, c=3):
#     if n < 3:
#         return 1
#     else:
#         if n == c:
#             return b1 + b2
#         else:
#             return Fib(n, b1=b2, b2=b1 + b2, c=c + 1)
#
#
# s = Fib(2000)
# print(s)
#
#
# class Solution:
#     def Fibonacci(self, n):
#         # write code here
#         """方法1：递归不行，栈会溢出"""
#         # if n >= 2:
#         #     return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
#         # else:
#         #     return n
#         """方法2：用循环，最好不用递归"""
#         # recode = [1, 1]
#         # if n <= 1:
#         #     return n
#         # else:
#         #     for i in range(2, n):
#         #         recode.append(recode[-1] + recode[-2])
#         #     return recode[n - 1]
#         """
#         别人写的循环
#         链接：https: // www.nowcoder.com / questionTerminal / c6c7742f5ba7442aada113136ddea0c3
#         来源：牛客网
#         """
#         res = [0, 1, 1, 2]
#         while len(res) <= n:
#             res.append(res[-1] + res[-2])
#         return res[n]
#
# s = Solution().Fibonacci(5)
# print(s)
#



# 重新写
# -*- coding:utf-8 -*-
# 1.暴力递归
import time


def Fibonacci(n):
    # write code here
    if n <= 1:
        return n
    return Fibonacci(n - 1) + Fibonacci(n - 2)

# 2.记忆性搜索
def Fibonacci_1(n):
    # write code here
    if n <= 1:
        return n
    if result[n] > 0:
        return result[n]
    result[n] = Fibonacci_1(n - 1) + Fibonacci_1(n - 2)
    return result[n]

# 3.递推
def Fibonacci_2(n):
    # write code here
    if n <= 1:
        return n
    result = [1, 1]
    while len(result) < n:
        result.append(result[-1] + result[-2])
    return result[-1]


if __name__ == '__main__':
    n = int(input())
    result = [0] * (n + 1)
    begin = time.time()
    print(Fibonacci(n))
    end = time.time()
    print(end - begin)
    print("------------")
    begin = time.time()
    print(Fibonacci_1(n))
    end = time.time()
    print(end - begin)
    print("------------")
    begin = time.time()
    print(Fibonacci_2(n))
    end = time.time()
    print(end - begin)