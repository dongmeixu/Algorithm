"""
判断一棵二叉树是否为平衡二叉树

平衡二叉树：每一个节点的左右子树的高度差不超过1
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBBT(self, root):
        if not root:
            return True

        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
