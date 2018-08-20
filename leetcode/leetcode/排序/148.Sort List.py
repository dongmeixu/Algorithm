"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 归并排序，时间复杂度O(nlogn) 空间复杂度O(1)
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # 快慢指针找到中间元素
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # 断开，分成2个部分
        fast = slow
        slow = slow.next
        fast.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            head = ListNode(l1.val)
            head.next = self.mergeTwoLists(l1.next, l2)
        elif l1.val > l2.val:
            head = ListNode(l2.val)
            head.next = self.mergeTwoLists(l1, l2.next)
        else:
            head = ListNode(l1.val)
            head.next = ListNode(l2.val)
            head.next.next = self.mergeTwoLists(l1.next, l2.next)
        return head
