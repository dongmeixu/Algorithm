"""
1、判断一条单向链表是不是“回文”
分析：对于单链表结构，可以用两个指针从两端或者中间遍历并判断对应字符是否相等。
但这里的关键就是如何朝两个方向遍历。
由于单链表是单向的，所以要向两个方向遍历的话，
可以采取经典的快慢指针的方法，
即先位到链表的中间位置，再将链表的后半逆置，最后用两个指针同时从链表头部和中间开始同时遍历并比较即可。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 没通过
class Solution:
    def IsPalindrome(self, listNode):
        if not listNode:
            return None

        # 1. 统计下链表的长度
        p = listNode
        lengthOfList = 0
        while p:
            lengthOfList += 1
            p = p.next
        # 2. 设置快慢指针，让快的指针先走到链表中间
        slow = fast = listNode
        time = lengthOfList >> 1
        while time:
            fast = fast.next
            time -= 1
        fast = fast if time & 1 == 0 else fast.next
        while fast:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True

        # if time & 1 == 0:  # 偶数
        #     while fast:
        #         if slow.val != fast.val:
        #             return False
        #         slow = slow.next
        #         fast = fast.next
        # else:  # 奇数
        #     fast = fast.next
        #     while fast:
        #         if slow.val != fast.val:
        #             return False
        #         slow = slow.next
        #         fast = fast.next


# 利用栈
class Solution_1:
    def IsPalindrome(self, listNode):
        if not listNode:  # 当链表为空的时候，返回false
            return True

        if not listNode.next:  # 当链表只含有一个元素，返回True
            return True

        stack = [listNode]
        p = listNode.next
        while p:  # 从链表第二个元素开始比较，如果它与栈顶元素值相等，则栈顶元素出栈，否则，该节点入栈
            top = stack[-1]
            if top.val == p.val:
                stack.pop()
            else:
                stack.append(p)
            p = p.next

        if len(stack) == 0:  # 遍历完整个链表以后，如果栈为空，则返回true
            return True
        else:
            return False


p = phead = ListNode(1)
p.next = ListNode(2)
p.next.next = ListNode(2)
p.next.next.next = ListNode(1)
print(Solution_1().IsPalindrome(phead))
