"""

题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    # 将元素直接入栈A
    def push(self, node):
        # write code here
        self.stackA.append(node)

    # 1. B不为空，直接出栈
    # 2. 栈A为空，返回None
    # 3. 如果栈B为空，将A中的元素全部出栈并入栈B
    def pop(self):
        # return xx
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:  # B为空，将A的所有元素均进栈
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()


def sortAges(arr):
    if not arr:
        return []
    oldestAge = 99
    length = len(arr)

    # 初始化为0
    timesOfAge = [0] * length

    for i in range(length):
        if 0 < arr[i] < length:
            timesOfAge[arr[i]] += 1

    print(timesOfAge)

    index = 0
    for i in range(oldestAge):
        for j in range(timesOfAge[i]):
            arr[index] = i
            index += 1
    print(arr)


sortAges([1, 2, 2, 3, 2])
