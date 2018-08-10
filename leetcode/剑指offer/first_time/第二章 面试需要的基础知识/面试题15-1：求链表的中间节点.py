"""
题目描述：
    如果链表中节点总数为奇数，返回中间节点。
    如果节点总数是偶数，返回中间两个节点的任意一个。


思路：
    也可以定义两个指针，同时从链表的头结点出发，
    一个指针一次走一步，另一个指针一次走两步。
    当走得快的指针走到链表的末尾时，走得慢的指针正好在链表的中间。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def midNodeOfList(self, head):
        if not head:
            return

        p1 = p2 = head
        while p2.next:
            p1 = p1.next
            if p2.next.next:
                p2 = p2.next.next
            else:
                return p1 or p2
        return p1


N = list(map(int, input().split()))
p = head = ListNode(N[0])
for temp in N[1:]:
    p.next = ListNode(temp)
    p = p.next
print(Solution().midNodeOfList(head).val)


