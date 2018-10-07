class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addList(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    s1 = []
    s2 = []
    p1 = head1
    p2 = head2

    while p1:
        s1.append(p1.val)
        p1 = p1.next
    while p2:
        s2.append(p2.val)
        p2 = p2.next

    pre = None
    pnode = None
    ca = 0
    while s1 or s2:
        n1 = s1.pop() if s1 else 0
        n2 = s2.pop() if s2 else 0
        n = n1 + n2 + ca
        pre = pnode
        pnode = ListNode(n % 10)
        pnode.next = pre
        ca = int(n / 10)
    if ca == 1:
        pre = pnode
        pnode = ListNode(1)
        pnode.next = pre
    return pnode


head1 = p1 = ListNode(9)
p1.next = ListNode(3)
p1.next.next = ListNode(7)
head2 = p2 = ListNode(6)
p2.next = ListNode(3)
head = addList(head1, head2)
while head:
    print(head.val)
    head = head.next



