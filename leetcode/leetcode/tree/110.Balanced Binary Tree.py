"""
判断一棵二叉树是否为平衡二叉树

平衡二叉树：每一个节点的左右子树的高度差不超过1
"""

"""已通过leetcode"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1


p = root = TreeNode(0)
p.left = TreeNode(2)
p.left.left = TreeNode(2)
p.left.left.left = TreeNode(2)
p.right = TreeNode(2)
p.right.left = TreeNode(2)
p.right.left.right = TreeNode(2)
print(Solution().isBalanced(root))
