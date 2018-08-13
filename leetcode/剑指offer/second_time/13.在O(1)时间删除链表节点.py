class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, listNode, deleteNode):
        if not listNode or not deleteNode:
            return

        # 只有一个节点
        p = listNode
        if p == deleteNode:
            del deleteNode

        elif deleteNode.next:  # 属于中间的节点
            nextNode = deleteNode.next
            deleteNode.val = nextNode.val
            deleteNode.next = nextNode.next
            del nextNode

        else:  # 属于尾指针
            while p:
                if p.next == deleteNode:
                    del p.next
                    p.next = None
                p = p.next
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
