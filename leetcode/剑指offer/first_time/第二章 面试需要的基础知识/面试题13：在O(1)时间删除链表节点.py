# -*- coding:utf-8 -*-
"""题目：给定单链表的头指针和一个节点的指针，定义一个函数在O(1)的时间删除链表节点"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, listNode, deleteNode):
        if not listNode or not deleteNode:
            return

        # 要删除的节点不是尾节点
        # 有n-1个非尾节点，可以在O(1)下把下一个节点的内存复制覆盖要删除的节点，并删除下一个节点
        if deleteNode.next:
            pNext = deleteNode.next
            deleteNode.val = pNext.val
            deleteNode.next = pNext.next

            del pNext
            pNext = None

        # 链表只有一个节点，删除头结点（也是尾节点）
        elif listNode == deleteNode:
            del deleteNode
            deleteNode = None
            listNode = None

        # 链表中有多个节点，删除尾节点
        # 对于尾节点而言，仍需顺序查找，时间复杂度为O(n)
        else:
            phead = listNode
            while phead.next != deleteNode:
                phead = phead.next

            phead.next = None
            del deleteNode
            deleteNode = None
        # 故总体的平均时间复杂度为  [(n - 1) * O(1) + O(n)] / n
        return listNode


# N = list(map(int, input().split()))
# print(N)
N = [1, 2, 3, 4, 5]
p = phead = ListNode(N[0])  # 头结点
for nodeVal in N[1:]:
    p.next = ListNode(nodeVal)
    p = p.next

# while phead:
#     print(phead.val)
#     phead = phead.next
phead = Solution().deleteNode(phead, phead.next.next)

while phead:
    print(phead.val)
    phead = phead.next
