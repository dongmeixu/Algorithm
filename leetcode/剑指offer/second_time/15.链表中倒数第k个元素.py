# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 考虑：链表为空；k小于0或者大于链表的总长度
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k <= 0:
            return

        pfast = pslow = head  # 循环不变量 [第一个元素......最后一个元素]的闭区间范围内

        while k - 1:  # 边界容易出错
            # for i in range(1, k):  # 第一个指针先自己走 k - 1 步
            if pfast.next:
                pfast = pfast.next
                k -= 1
            else:  # k比链表的长度都大
                return

        while pfast.next:  # 当走到最后一个节点的时候截止
            pfast = pfast.next
            pslow = pslow.next
        return pslow.val


N = list(map(int, input().split()))
p = head = ListNode(N[0])
for temp in N[1:]:
    p.next = ListNode(temp)
    p = p.next
print(Solution().FindKthToTail(head, 3))
