class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class DoubleList:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.pre = None


"""
删除单链表与双链表中倒数第k个节点
"""


class CommonPart:
    def delInSingleList(self, head, k):
        if not head or k < 1:
            return head

        p1 = p2 = head
        for i in range(k):
            if p1.next:
                p1 = p1.next
            else:
                return

        while p1.next:
            p1 = p1.next
            p2 = p2.next

        node = p2.next
        print(node.val)
        p2.next = node.next
        del node
        return head

    def delInDoubleList(self, head, k):
        if not head or k < 1:
            return head

        p1 = p2 = head
        for i in range(k):
            if p1.next:
                p1 = p1.next
            else:
                return

        while p1.next:
            p1 = p1.next
            p2 = p2.next

        node = p2.next
        p2.next = node.next
        node.next.pre = p2
        del node
        return head


# list = list(map(int, input().split()))
#
# phead1 = ListNode(list[0])
# p = phead1
# for x in list[1:]:
#     temp = ListNode(x)
#     p.next = temp
#     p = p.next

# print(CommonPart().delInSingleList(phead1, 3))


p = phead2 = DoubleList(0)

p.next = DoubleList(1)
p.next.pre = p
p.next.next = DoubleList(2)
p.next.next.pre = p.next
print(CommonPart().delInDoubleList(phead2, 2))
pp = CommonPart().delInDoubleList(phead2, 2)
while pp:
    print(pp.val)
    pp = pp.next

