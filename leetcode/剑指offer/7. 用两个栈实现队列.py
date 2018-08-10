# coding=utf-8
"""
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。
队列中的元素为int类型。
"""
"""
思路：栈A用作入队列；
     栈B用作出队列，当栈B为空时，将栈A全部出栈，并入栈B,B再出栈
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
    # 3.如果栈B为空，将A中的元素全部出栈并入栈B
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
