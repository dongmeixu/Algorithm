"""

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""
# -*- coding:utf-8 -*-
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 不符合输出要求
# class Solution:
# def levelOrder(self, root):
#     res = []
#     if not root:
#         return res
#     queue = [root]
#     while len(queue) != 0:
#         root = queue.pop()
#         res.append(root.val)
#         if root.left:
#             queue.append(root.left)
#         if root.right:
#             queue.append(root.right)
#     return res

"""这个是别人代码改写的。。。"""
class Solution(object):
    def levelOrder(self, root):
        ret = []
        if not root:
            return ret
        # queue = collections.deque([(root, 0)])
        queue = [(root, 0)]
        while queue:
            node, level = queue[0]
            queue.pop(0)
            if len(ret) == level:
                ret.append([])
            ret[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return ret


class Solution_1:
    def __init__(self):
        self.alist = []

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.aux_leve(root, 0)
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
print(Solution().levelOrder(head))
print(Solution_1().levelOrder(head))
