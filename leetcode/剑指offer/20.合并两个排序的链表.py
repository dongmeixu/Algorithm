"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2
        if p1 is None:
            return p2
        if p2 is None:
            return p1
        if p1.val <= p2.val:
            p1.next = self.Merge(p1.next, p2)
            return p1
        else:
            p2.next = self.Merge(p1, p2.next)
            return p2
