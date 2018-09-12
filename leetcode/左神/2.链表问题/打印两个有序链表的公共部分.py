class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
2个有序链表，打印公共部分
"""

"""
因为是有序链表，所以从两个链表的表头开始扫描
1.head1.val == head2.val,打印这个结点，head1,head2同时指针后移
2.head1.val > head2.val, head2指针后移
3.head1.val < head2.val, head1指针后移
直到head1，head2有任何一个为空时就截止
"""
class CommonPart:
    def getCommon(self, head1, head2):
        res = []
        if not head1 or not head2:
            return res

        p1 = head1
        p2 = head2
        while p1 and p2:
            if p1.val == p2.val:
                res.append(p1.val)
                p1 = p1.next
                p2 = p2.next
            elif p1.val > p2.val:
                p2 = p2.next
            else:
                p1 = p1.next
        return res


list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

phead1 = ListNode(list1[0])
p = phead1
for x in list1[1:]:
    temp = ListNode(x)
    p.next = temp
    p = p.next

phead2 = ListNode(list2[0])
p = phead2
for x in list2[1:]:
    temp = ListNode(x)
    p.next = temp
    p = p.next

print(CommonPart().getCommon(phead1, phead2))
