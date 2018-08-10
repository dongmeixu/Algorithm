class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isCycle(self, head):
        if not head:
            return

        pfast = pslow = head
        isCycle = False

        while True:
            pfast = pfast.next if pfast.next else None;
            if not pfast:
                break
            pfast = pfast.next if pfast.next else None;
            if not pfast:
                break

            pslow = pslow.next if pslow.next else None;
            if not pslow:
                break

            if pfast == pslow:
                isCycle = True
                break

        return head, pslow, isCycle

    def entrn(self, head, pslow, isCycle):
        if not isCycle:
            return
        cur = head
        inter = pslow

        while cur != inter:
            cur = cur.next
            inter = inter.next

        return cur



#
# N = list(map(int, input().split()))
# p = head = ListNode(N[0])
# for temp in N[1:]:
#     p.next = ListNode(temp)
#     p = p.next
# print(Solution().isCycle(head))

p = phead = ListNode(1)
# p.next = ListNode(2)
# p.next.next = ListNode(3)
# p.next.next.next = ListNode(4)
# p.next.next.next = p.next

s = Solution()
head, pslow, isCycle = s.isCycle(phead)
ss = s.entrn(head, pslow, isCycle)
print(ss)