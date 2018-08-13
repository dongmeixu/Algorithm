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

        reverseHead = None
        pre = None
        pNode = pHead

        while pNode:
            pNext = pNode.next
            if not pNext:
                reverseHead = pNode
            pNode.next = pre
            pre = pNode
            pNode = pNext

        return reverseHead


N = list(map(int, input().split()))
p = head = ListNode(N[0])
for temp in N[1:]:
    p.next = ListNode(temp)
    p = p.next
print(Solution().ReverseList(head).val)
