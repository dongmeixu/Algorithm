"""

题目描述
输入一个链表，输出该链表中倒数第k个结点。

思路：循环遍历链表把链表的内容放到一个数组（列表）中，最后直接取出倒数第k个就可以了
"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        res = []
        while head:
            res.append(head)
            head = head.next
        if k > len(res) or k < 1:
            return
        return res[-k]