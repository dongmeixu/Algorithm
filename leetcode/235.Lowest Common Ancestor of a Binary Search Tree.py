"""
给定一棵二分搜索树和两个节点，寻找这两个节点的最近公共祖先

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def loewstCommonAncestor(self, root, p, q):
        assert p is not None and q != None

        if not root:
            return

        if p.val < root.val and q.val < root.val:
            return self.loewstCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.loewstCommonAncestor(root.right, p, q)
        else:
            return root


p = root = TreeNode(4)
p.left = TreeNode(2)
p.right = TreeNode(6)
p.left.left = TreeNode(1)
p.left.right = TreeNode(3)
p.right.left = TreeNode(5)
p.right.right = TreeNode(7)
print(Solution().loewstCommonAncestor(root, TreeNode(2), TreeNode(3)).val)
