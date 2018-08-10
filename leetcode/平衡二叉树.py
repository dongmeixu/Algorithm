# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.is_balanced = True

    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.TreeDepth(pRoot)
        return self.is_balanced

    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        if abs(left - right) > 1:
            self.is_balanced = False
        return max(left, right) + 1