"""
题目描述
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
但是对于后面问题他就没辙了。剑指offer/第五章 优化时间和空间效率/面试题32：从1到n整数中1出现的次数.py
ACMer希望你们帮帮他,
并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数。
"""

"""
思路1：
    对n以内的所有数 判断每位上是不是为1；之后再将所有值累加
    如果输入数字n，n有O(logn)位，我们需要判断每一位是不是1，
    那么它的时间复杂度是O(n * logn).
    当输入n非常大的时候，需要大量的计算，运算效率不高。
    
思路2：
从1到n整数中1出现的次数：O(logn)算法 - CSDN博客 https://blog.csdn.net/yi_afly/article/details/52012593
"""
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if not n:
            return 0

        res = 0
        for i in range(1, n + 1):
            res += self.NumberOf1(i)
            # print(res)
        return res

    def NumberOf1(self, number):
        count = 0
        while number:
            if number % 10 == 1:
                count += 1
            number //= 10
        return count

    def count(self, n):
        if n < 1:
            return 0

        count = 0
        base = 1
        round = n
        while round > 0:
            weight = round % 10
            round //= 10
            count += round * base

            if weight == 1:
                count += n % base + 1
            elif weight > 1:
                count += base
            base *= 10

        return count


n = -1 # (1,2,3,4,5,6,7,8,9,10,11,12)
# print(Solution().NumberOf1Between1AndN_Solution(n))
print(Solution().NumberOf1Between1AndN_Solution(11))
print(Solution().count(11))







