# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def isBalanced(self, pRoot):
        # write code here
        if not pRoot:
            return True
        if abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) > 1:
            return False
        return self.isBalanced(pRoot.left) and self.isBalanced(pRoot.right)

    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left, right) + 1

class Solution_1:

    def isBalanced(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.balanceHeight(pRoot) >= 0

    def balanceHeight(self, pRoot):
        if not pRoot:
            return 0

        left = self.balanceHeight(pRoot.left)
        right = self.balanceHeight(pRoot.right)
        if left < 0 or right < 0 or abs(left - right) > 1:  # 剪枝
            return -1
        return max(left, right) + 1
