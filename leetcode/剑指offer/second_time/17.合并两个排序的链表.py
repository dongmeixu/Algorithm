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

        if pHead1.val <= pHead2.val:
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

p2 = phead2 = ListNode(2)
p2.next = ListNode(4)
p2.next.next = ListNode(5)
# p2 = None
pm = Solution().Merge(p1, p2)

while pm:
    print(pm.val)
    pm = pm.next
