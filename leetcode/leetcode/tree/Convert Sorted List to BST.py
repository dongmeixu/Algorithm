"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

与上一个题类似，但是单链表不能随机访问，
而自顶向下的二分法必须需要RandomAccessIterator，因此前面的方法不使用本题
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 时间复杂度O(n^2) 空间复杂度O(logn)
class Solution:
    def sortedListToBST(self, head):

        len = self.get_length(head)
        return self.sortedListToBST_main(head, len)

    def sortedListToBST_main(self, head, len):
        if len == 0:
            return None
        if len == 1:
            return TreeNode(head.val)

        mid = len // 2

        root = TreeNode(self.nth_node(head, mid).val)
        root.left = self.sortedListToBST_main(head, mid - 1)
        root.right = self.sortedListToBST_main(head, mid + 1)
        return root

    def get_length(self, head):
        n = 0
        while head:
            head = head.next
            n += 1
        return n

    def nth_node(self, node, n):
        while n >= 0:
            node = node.next
            n -= 1
        return node


class Solution:
    def sortedListToBST(self, head):
        # 类似2分法一样
        # 获取链表长度
        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        return self.sortedListToBST_main(head, 0, n - 1)

    def sortedListToBST_main(self, head, start, end):
        if start > end:
            return None
        mid = start + (end - start) // 2
        leftTrees = self.sortedListToBST_main(head, start, mid - 1)
        root = TreeNode(head.val)
        root.left = leftTrees

        head = head.next
        rightTrees = self.sortedListToBST_main(head, mid + 1, end)
        root.right = rightTrees
        return root


nums = [1, 2, 3, 4, 5]
print(Solution().sortedListToBST(nums))
