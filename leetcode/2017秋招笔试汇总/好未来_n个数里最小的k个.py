"""

题目描述
找出n个数里最小的k个

输入描述:
每个测试输入包含空格分割的n+1个整数，最后一个整数为k值,n
不超过100。

输出描述:
输出n个整数里最小的k个数。升序输出

示例1
输入
3 9 6 8 -10 7 -11 19 30 12 23 5
输出
-11 -10 3 6 7
"""


# -*- coding:utf-8 -*-
class Solution3:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k <= 0:
            return []

        length = len(tinput)
        if k > length:
            return []
        tinput.sort()
        res = ""
        for tmp in tinput[:k]:
            res = res + str(tmp) + " "
        return res.strip()


input = list(input().strip().split(" "))
arr = [int(i) for i in input[:-1]]
k = int(input[-1])
print(Solution3().GetLeastNumbers_Solution(arr, k))