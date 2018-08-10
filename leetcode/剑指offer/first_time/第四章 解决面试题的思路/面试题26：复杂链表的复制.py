"""
题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""

# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        self.CloneNodes(pHead)
        self.ConnectSiblingNodes(pHead)
        return self.ReconnectNodes(pHead)

    # 从旧链表中创建新链表，此时不处理新链表的兄弟节点
    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(0)
            pCloned.label = pNode.label
            pCloned.next = pNode.next
            pCloned.random = None

            pNode.next = pCloned
            pNode = pCloned.next

    # 根据旧链表的兄弟节点，初始化新链表的兄弟节点
    def ConnectSiblingNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random:
                pCloned.random = pNode.random.next
            pNode = pCloned.next

    # 从旧链表中拆分得到新链表
    def ReconnectNodes(self, pHead):
        pNode = pHead
        pCloneHead = None
        pCloneNode = None

        if pNode:
            pCloneHead = pCloneNode = pNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        while pNode:
            pCloneNode.next = pNode.next
            pCloneNode = pCloneNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        return pCloneHead


A = RandomListNode("A")
B = RandomListNode("B")
C = RandomListNode("C")
D = RandomListNode("D")
E = RandomListNode("E")
A.next = B
A.random = C
B.next = C

C.next = D
D.next = E
D.random = B

phead = A

s = Solution().Clone(phead)
print(s)
while s.next:
    print(s.label)
