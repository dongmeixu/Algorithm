"""
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。

"""

"""
分析：
    p1 指向第一个链表 p2指向第二个链表 pmerge指向合并后的链表
    1. 当p1头结点的值小于p2头结点的值，则将p1的头结点赋给pmerge
    反之， pmerge = p2
    
    2.递归调用
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        if pHead1.val < pHead2.val:
            pMerge = pHead1
            pMerge.next = self.Merge(pHead1.next, pHead2)

        else:
            pMerge = pHead2
            pMerge.next = self.Merge(pHead1, pHead2.next)
        return pMerge


# p1 = phead1 = ListNode(1)
# p1.next = ListNode(3)
# p1.next.next = ListNode(4)
p1 = None

# p2 = phead2 = ListNode(2)
# p2.next = ListNode(4)
# p2.next.next = ListNode(5)
p2 = None
pm = Solution().Merge(p1, p2)

while pm:
    print(pm.val)
    pm = pm.next