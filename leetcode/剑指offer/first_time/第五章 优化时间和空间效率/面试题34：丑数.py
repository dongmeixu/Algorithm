"""
题目描述

    把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。例如 6、8
    都是丑数，但 14 不是，因为它包含因子 7。 习惯上我们把 1
    当做是第一个丑数。求按从小到大的顺序的第 N 个丑数。
"""

"""
思路1：逐个判断每个整数是不是丑数的解法，直观但不够高效
    所谓一个数m是另一个n的因子，是指n能被m整除，也就是n % m==0.
    根据丑数的定义，丑数只能被2,3,5整除，也就是说如果一个数能被2整除，我们把它连续除以2；
    如果能被3整除，就连续除以3；如果能被5整除，就连续除以5.如果最后我们得到的是1，那么
    这个数就是丑数，否则不是。
"""


# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        # 依次判断每个整数是不是丑数
        if not index:
            return 0

        number = 0
        uglyFound = 0
        while uglyFound < index:
            number += 1

            if self.IsUgly(number):
                uglyFound += 1
        return number

    def IsUgly(self, number):
        while number % 2 == 0:
            number //= 2
        while number % 3 == 0:
            number //= 3
        while number % 5 == 0:
            number //= 5

        return True if number == 1 else False


"""

思路2：
"""


# -*- coding:utf-8 -*-
class Solution2:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if not index:
            return 0
        if index <= 6:
            return index

        pUglyNumbers = [0] * index  # 保存丑数的数组
        pUglyNumbers[0] = 1  # 初始时只有1

        pMultiply2 = 0  # 下标
        pMultiply3 = 0
        pMultiply5 = 0

        for nextUglyIndex in range(1, index):
            p2 = pUglyNumbers[pMultiply2] * 2
            p3 = pUglyNumbers[pMultiply3] * 3
            p5 = pUglyNumbers[pMultiply5] * 5

            # 下一个丑数应该是p2,p3,p5中最小的那个值
            pUglyNumbers[nextUglyIndex] = min(p2, p3, p5)

            # 找出下一次的p2,p3,p5的位置
            if pUglyNumbers[nextUglyIndex] >= p2:
                pMultiply2 += 1
            if pUglyNumbers[nextUglyIndex] >= p3:
                pMultiply3 += 1
            if pUglyNumbers[nextUglyIndex] >= p5:
                pMultiply5 += 1

        return pUglyNumbers[index - 1]


index = 1500
# print(Solution().GetUglyNumber_Solution(index))
print(Solution2().GetUglyNumber_Solution(index))
