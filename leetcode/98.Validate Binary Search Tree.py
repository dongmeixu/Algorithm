"""
给定一棵二叉树，验证其是否是二分搜索树
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def validateBST(self, root):
        if not root:
            return True

        if root.left is not None and root.right is not None:
            if root.left.val < root.val < root.right.val:
                self.validateBST(root.left)
                self.validateBST(root.right)
            else:
                return False
        else:
            if root.left:
                if root.left.val < root.val:
                    self.validateBST(root.left)
                else:
                    return False

            if root.right:
                if root.right.val < root.val:
                    self.validateBST(root.right)
                else:
                    return False
