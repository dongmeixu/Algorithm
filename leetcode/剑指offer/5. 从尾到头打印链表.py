# coding=utf-8
"""
输入一个链表，从尾到头打印链表每个节点的值。

"""
"""
思路：递归遍历，每次把值加入列表，最后再把列表reverse
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        result = []
        if listNode is None:
            return result
        while listNode.next is not None:
            result.append(listNode.val)
            listNode = listNode.next
        result.append(listNode.val)
        result.reverse()
        return result
