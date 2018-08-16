"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

"""
"""已通过leetcode"""
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        ret = []
        if not root:
            return ret
        queue = collections.deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if len(ret) == level:
                ret.append([])
            ret[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        for i, tmp in enumerate(ret):
            if i & 1 != 0:
                tmp.reverse()
        return ret


class Solution_1:
    def __init__(self):
        self.alist = []

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.aux_leve(root, 0)

        for i, tmp in enumerate(self.alist):
            if i & 1 != 0:
                tmp.reverse()
        return self.alist

    def aux_leve(self, current, level):
        if not current:
            return 0
        else:
            if len(self.alist) <= level:
                self.alist.append([])
            self.alist[level].append(current.val)
            self.aux_leve(current.left, level + 1)
            self.aux_leve(current.right, level + 1)


head = TreeNode(0)
p = head
p.left = TreeNode(1)
p.right = TreeNode(2)
p.left.left = TreeNode(3)
p.left.right = TreeNode(4)
print(Solution().zigzagLevelOrder(head))
print(Solution_1().zigzagLevelOrder(head))

