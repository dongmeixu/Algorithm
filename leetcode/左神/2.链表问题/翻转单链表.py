class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ReverseSingleList:
    def reverse(self, head):
        pre = None

        while head:
            pnext = head.next
            head.next = pre
            pre = head
            head = pnext
        return pre


ll = list(map(int, input().split()))
head = p = ListNode(ll[0])
for x in ll[1:]:
    p.next = ListNode(x)
print(ReverseSingleList().reverse(head).val)