"""
5、在O(1)时间内删除单链表结点
给定单链表的一个结点的指针，同时该结点不是尾结点，此外没有指向其它任何结点的指针，请在O(1)时间内删除该结点。

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, pHead, target):
        if not pHead or not target:
            return

        p = pHead
        # 要删除的节点刚好是头结点指向的元素
        if pHead == target:
            del target
            pHead = None

        elif target.next:
            # 删除的元素在链表中间
            tmp = target.next
            target.val = tmp.val
            target.next = tmp.next
            del tmp
        else:
            # 此时待删除元素在链尾，只能顺序遍历删除了
            while p:
                if p.next == target:
                    del target
                    p.next = None
                else:
                    p = p.next
        return pHead


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