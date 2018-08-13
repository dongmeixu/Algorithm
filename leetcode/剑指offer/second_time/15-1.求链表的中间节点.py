class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def midNodeOfList(self, head):
        if not head:
            return

        pfast = pslow = head
        while pfast.next:
            pfast = pfast.next
            if pfast.next:
                pfast = pfast.next
            pslow = pslow.next
        return pslow


N = list(map(int, input().split()))
p = head = ListNode(N[0])
for temp in N[1:]:
    p.next = ListNode(temp)
    p = p.next
print(Solution().midNodeOfList(head).val)
