class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 判断单链表是否有环,有的话则返回环的入口节点
def getLoopNode(head):
    if not head or not head.next or not head.next.next:
        return None

    slow = head.next
    fast = head.next.next
    while slow != fast:
        if not fast.next or not fast.next.next:
            return None
        slow = slow.next
        fast = fast.next.next

    # 此时如果有环，循环结束后指示的是相遇点
    cur = head
    while cur != slow:
        cur = cur.next
        slow = slow.next
    return cur


# 判断两个单链表是否相交，若相交则返回第一个公共节点
def noLoop(head1, head2):
    if not head1 or not head2:
        return None

    nDiffer = 0
    cur1 = head1
    cur2 = head2
    # 统计长度的同时判断下最后的节点是否相等
    while cur1.next:
        nDiffer += 1
        cur1 = cur1.next

    while cur2.next:
        nDiffer -= 1
        cur2 = cur2.next

    if cur1 != cur2:
        return None

    # cur1指示长的链表，cur2指示短的链表
    cur1 = head1 if nDiffer > 0 else head2
    cur2 = head2 if cur1 == head1 else head1
    nDiffer = abs(nDiffer)

    while nDiffer:
        cur1 = cur1.next
        nDiffer -= 1

    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next

    return cur1


# 如何判断两个有环链表是否相交，相交则返回第一个相交节点，不想交则返回null
def bothLoop(head1, loop1, head2, loop2):
    if loop1 == loop2:
        cur1 = noLoop(head1, head2)
        return cur1
    else:
        cur1 = loop1.next
        while cur1 != loop1:
            if cur1 == loop2:
                return loop1
            cur1 = cur1.next
        return None


def getIntersectNode(head1, head2):
    if not head1 or not head2:
        return None
    loop1 = getLoopNode(head1)
    loop2 = getLoopNode(head2)
    if loop1 and loop2:
        return bothLoop(loop1, loop2)
    if not loop1 and not loop2:
        return noLoop(loop1, loop2)
    return None
