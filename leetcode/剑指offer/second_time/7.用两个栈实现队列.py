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
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()


