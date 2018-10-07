# 思路1：将元素入栈，然后逆序，最后再连接起来

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseKNodes(head, k):
    if not head or not k:
        return head

    stack = []
    p = head
    while p:
        stack.append(p)
        p = p.next

    length = len(stack)
    if k >= length:
        return head

    index = 0
    for i in range(length // k):
        reverse(stack, index, index + k - 1)
        # stack[index: index + k].reverse()
        index += k

    for i in range(1, len(stack)):
        stack[i - 1].next = stack[i]
    return stack[0].val


def reverse(arr, left, right):
    while left <= right:
        tmp = arr[left]
        arr[left] = arr[right]
        arr[right] = tmp
        left += 1
        right -= 1
    return arr


ll = list(map(int, input().split()))
head = p = ListNode(ll[0])
for i in ll[1:]:
    p.next = ListNode(i)
    p = p.next

reverseKNodes(head, 3)
