class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def listPartition(head, pivot):
    if not head or not pivot:
        return head

    # 将所有节点入栈
    stack = []
    pnode = head
    while pnode:
        stack.append(pnode)
        pnode = pnode.next

    # 对栈数组中的元素排序，基于partition操作
    arrPartition(stack, pivot, 0, len(stack) - 1)

    # 将排序后的所有节点链接成单链表
    for i in range(1, len(stack)):
        stack[i - 1].next = stack[i]
    stack[-1].next = None
    # testing
    for tmp in stack:
        print(tmp.val)
    return stack[0]


# 三路快排
def arrPartition(arr, pivot, start, end):
    index = 0
    while index != end:
        if arr[index].val < pivot:
            # tmp = arr[index]
            # arr[index] = arr[start]
            # arr[start] = tmp
            swap(arr, index, start)
            start += 1
            index += 1
        elif arr[index].val > pivot:
            swap(arr, index, end)
            # tmp = arr[index]
            # arr[index] = arr[end]
            # arr[end] = tmp
            end -= 1
        else:
            index += 1


def swap(arr, index1, index2):
    tmp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = tmp


head = p1 = ListNode(0)
p1.next = ListNode(4)
p1.next.next = ListNode(2)
listPartition(head, 3)
