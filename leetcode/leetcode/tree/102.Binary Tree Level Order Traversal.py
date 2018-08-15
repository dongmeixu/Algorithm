# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderTraversal(self, root):
        res = []
        if not root:
            return res
        queue = [root]
        while len(queue) != 0:
            root = queue.pop()
            res.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return res
