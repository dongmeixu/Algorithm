"""
用递归的思想解决

"""
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        else:
            return max(1 + self.TreeDepth(pRoot.left), 1 + self.TreeDepth(pRoot.right))
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
print(Solution().TreeDepth(tree))