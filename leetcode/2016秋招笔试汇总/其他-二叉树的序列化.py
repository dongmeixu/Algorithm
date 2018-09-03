# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeToSequence:
    def toSequence(self, root):
        # write code here
        if not root:
            return ""
        return "(" + self.toSequence(root.left) + self.toSequence(root.right) + ")"


root = p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.left.left = TreeNode(4)
p.left.right = TreeNode(5)
print(TreeToSequence().toSequence(root))