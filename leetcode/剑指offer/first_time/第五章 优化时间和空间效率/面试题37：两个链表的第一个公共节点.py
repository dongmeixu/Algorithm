"""
题目：输入两个链表，找出它们的第一个公共节点
"""
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def FindFirstCommonNode(self, pHead1, pHead2):
    #     # write code here
    #     if not pHead1 or not pHead2:
    #         return None
    #     p1 = pHead1
    #     p2 = pHead2
    #     while p1 != p2:
    #         p1 = p1.next if p1.next else pHead2
    #         p2 = p2.next if p2.next else pHead1
    #
    #     return p1

    # 时间复杂度O(m+n)
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None

        # 得到两个链表的长度
        nLength1 = self.GetListLength(pHead1)
        nLength2 = self.GetListLength(pHead2)

        if nLength1 > nLength2:
            pListHeadLong = pHead1
            pListHeadShort = pHead2
            nLengthDif = nLength1 - nLength2

        else:

            pListHeadLong = pHead2
            pListHeadShort = pHead1
            nLengthDif = nLength2 - nLength1

        # 让长的链表先走
        for i in range(nLengthDif):
            pListHeadLong = pListHeadLong.next
        # print(pListHeadLong.val)
        # print(pListHeadShort.val)
        # 此时长的跟短的应该到链尾的距离都是一样的，这时候同时在两个链表上遍历
        while pListHeadLong and pListHeadShort and pListHeadLong != pListHeadShort:
            pListHeadLong = pListHeadLong.next
            pListHeadShort = pListHeadShort.next

        return pListHeadLong

    def GetListLength(self, pHead):
        length = 0
        p = pHead
        if not p:
            return length
        while p:
            p = p.next
            length += 1

        # print(length)
        return length

# p1 = pLong = ListNode(1)
# p1.next = ListNode(2)
# p1.next.next = ListNode(3)
# ss = p1.next.next.next = ListNode(6)
# tt = p1.next.next.next.next = ListNode(7)
#
#
# p2 = pShort = ListNode(4)
# p2.next = ListNode(5)
# p2.next.next = ss
# p2.next.next.next = tt


p1 = pLong = ListNode(1)
p1.next = ListNode(2)
p1.next.next = ListNode(3)


p2 = pShort = ListNode(4)
p2.next = ListNode(5)

print(Solution().FindFirstCommonNode(pLong, pShort))

