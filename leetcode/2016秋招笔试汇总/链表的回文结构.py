# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class PalindromeList:
    def chkPalindrome(self, A):
        # write code here
        if not A:
            return True
        # 翻转链表
        reverseHead = self.reverseList(A)
        # 依次遍历原链表与翻转后的链表，逐元素判断是否相等
        p_orig = A
        p_reverse = reverseHead
        while p_orig and p_reverse:
            if p_orig.val != p_reverse.val:
                return False
            p_orig = p_orig.next
            p_reverse = p_reverse.next
        return True

    def reverseList(self, ListHead):
        reverseHead = None
        pre = None
        pNode = ListHead

        while pNode:
            if not pNode.next:  # 此时代表原链表的最后一个元素，上翻转链表头结点指向它
                reverseHead = pNode
            pNext = pNode.next
            pNode.next = pre
            pre = pNode
            pNode = pNext
        return reverseHead

head = p = ListNode(1)
p.next = ListNode(2)
p.next.next = ListNode(2)
p.next.next.next = ListNode(3)
print(PalindromeList().chkPalindrome([]))