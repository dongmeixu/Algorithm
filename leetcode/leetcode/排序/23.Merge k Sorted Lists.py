# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 时间复杂度O(n1+n2+n3....)，空间复杂度O(1)======>超时了
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        p = lists[0]
        for i in range(1, len(lists)):
            p = self.mergeTwoLists(p, lists[i])
        return p

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

    # 方法2
    def mergeKLists_2(self, lists):
        if not lists:
            return

        tmp = []
        for node in lists:
            while node:
                tmp.append(node.val)
                node = node.next
        tmp.sort()

        p, head = None, None
        for i in range(len(tmp)):
            if i == 0:
                head = a = ListNode(tmp[i])
            else:
                a.next = ListNode(tmp[i])
                a = a.next
        return head