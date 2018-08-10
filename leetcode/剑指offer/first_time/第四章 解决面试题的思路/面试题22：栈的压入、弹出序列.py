# -*- coding:utf-8 -*-
"""
题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，
请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        len_push = len(pushV)
        len_pop = len(popV)

        if not pushV or not popV or len_push != len_pop:
            return False

        stack = []

        # 记录弹出序列的元素位置
        j = 0

        for i in range(len_push):
            stack.append(pushV[i])
            # 一个元素入栈以后，如果当前栈顶元素跟pop序列相应位置的值相等，则出栈（可以连续出栈！！！）
            while j < len_pop and stack[-1] == popV[j]:
                stack.pop()
                j += 1

        if len(stack) > 0:
            return False
        else:
            return True


push = [1, 2, 3, 4, 5]
# pop = [4, 5, 3, 2, 1]
pop = [4, 3, 5, 1, 2]
print(Solution().IsPopOrder(push, pop))
#
# ss = "12345"
# res = 0
# length = len(ss)
# for i, s in enumerate(ss):
#     # print(i, s)
#     res += 10 ** (length - 1 - i) * int(s)
#     # print(res)
#
# print(res)
