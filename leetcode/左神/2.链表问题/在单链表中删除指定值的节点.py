class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeValue(head, num):
    if not head or not num:
        return head

    stack = []
    p = head
    while p:
        if p.val != num:
            stack.append(p)
        p = p.next

    for i in range(1, len(stack)):
        stack[i - 1].next = stack[i]
    return stack[0]


ll = list(map(int, input().split()))
head = p = ListNode(ll[0])
for i in ll[1:]:
    p.next = ListNode(i)
    p = p.next

kk = removeValue(head, 3)
while kk:
    print(kk.val)
    kk = kk.next
