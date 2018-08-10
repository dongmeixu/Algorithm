"""

题目描述
输入一个链表，输出该链表中倒数第k个结点。

"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k < 0:  # 1. 链表为空
            return             # 2. 输入的 K=0

        p1 = p2 = head

        for i in range(1, k):# 第一个指针先自己走 k -1 步
            if p1.next:  # 3. 链表的节点总数少于K
                p1 = p1.next
            else:
                return

        while p1.next:
            p1 = p1.next
            p2 = p2.next

        print(p2.val)
        return p2


N = list(map(int, input().split()))
p = head = ListNode(N[0])
for temp in N[1:]:
    p.next = ListNode(temp)
    p = p.next
Solution().FindKthToTail(head, k=0)
