"""
题目描述
输入一个链表，反转链表后，输出链表的所有元素。


思路：
    设置3个指针，一个指向当前节点，
    一个指向前一个节点，
    一个指向后一个节点
"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead:
            return

        pReverseHead = None
        pNode = pHead
        pPrev = None

        while pNode: # 遍历原来链表
            pNext = pNode.next # 原来链表后一个指针
            if not pNext: # 结束条件
                pReverseHead = pNode
            pNode.next = pPrev  # 将当前节点的next指针指向前一个元素（反转）
            pPrev = pNode  # 指针后移
            pNode = pNext  # 指针后移

        return pReverseHead


p = phead = ListNode(1)
p.next = ListNode(2)
p.next.next = ListNode(3)

pp = Solution().ReverseList(phead)

while pp:
    print(pp.val)
    pp = pp.next

