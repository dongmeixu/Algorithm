# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        root = None
        # 1.空链表
        if not pHead:
            return root
        # 2.只有一个节点
        if not pHead.next:
            return pHead

        # 3.遍历链表处理非尾节点的所有节点
        stack = [pHead.val]
        p = pHead.next

        while p.next:
            if p.val not in stack:
                stack.append(p.val)
            elif p.val in stack and p.next.val not in stack:
                stack.pop()
            p = p.next

        # 4.此时是尾节点
        if len(stack) != 0:
            if p.val == stack[-1]:
                stack.pop()
            else:
                stack.append(p.val)
        else:
            stack.append(p.val)

        # 操作完整个链表依旧为空，直接返回
        if not stack:
            return root
        else:
            p = root = ListNode(stack[0])
            for i in range(1, len(stack)):
                p.next = ListNode(stack[i])
                p = p.next
        return root


p = phead = ListNode(1)
p.next = ListNode(1)
p.next.next = ListNode(1)
p.next.next.next = ListNode(1)
p.next.next.next.next = ListNode(1)
p.next.next.next.next.next = ListNode(2)

p1 = phead
while p1:
    # print(p1.val)
    p1 = p1.next
pp = Solution().deleteDuplication(phead)

while pp:
    print(pp.val)
    pp = pp.next


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None

        if not pHead.next:
            return pHead

        pre = None
        pnode = pHead
        flag = False  # 表示是否经历了重复

        while pnode:
            pnext = pnode.next
            if not pnext:
                return pHead
            while pnode.val == pnext.val:
                flag = True  # 经历了重复
                pnext = pnext.next
                if not pnext and not pre:  # 全都是重复的
                    pHead = None
                    break
            if flag:  # 当经历了重复，直接将pre的next指向pnext
                if pre is None:
                    pHead = pnext
                else:
                    pre.next = pnext
            else:
                pre = pnode
            pnode = pnext
        return pHead


class Solution_1:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None

        stack = []
        p = pHead

        while p:
            if p.val not in stack:
                stack.append(p.val)
            else:
                stack.pop()
            p = p.next

        print(stack)
        if not stack:
            return []
        else:
            pnewHead = p1 = ListNode(stack[0])
            for i in range(1, len(stack)):
                p1.next = ListNode(stack[i])
                p1 = p1.next
            return pnewHead


p1 = pLong = ListNode(1)
p1.next = ListNode(1)
p1.next.next = ListNode(1)
ss = p1.next.next.next = ListNode(1)
tt = p1.next.next.next.next = ListNode(1)

head = Solution_1().deleteDuplication(pLong)
while head.next:
    print(head.val)
    head = head.next
