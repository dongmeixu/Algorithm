class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteRepeatNode(head):
    if not head:
        return head

    # 利用辅助数组
    tmp = []
    p = head
    while p:
        if p.val not in tmp:
            tmp.append(p.val)
        p = p.next

    newHead = p = ListNode(tmp[0])
    for i in range(1, len(tmp)):
        p.next = ListNode(tmp[i])
        p = p.next
    return newHead


ll = list(map(int, input().split()))
head = p = ListNode(ll[0])
for i in ll[1:]:
    p.next = ListNode(i)
    p = p.next
kk = deleteRepeatNode(head)
while kk:
    print(kk.val)
    kk = kk.next