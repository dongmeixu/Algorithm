"""
求一棵二叉树的最低深度
从根节点到叶子节点的最短路径长度

"""

"""已通过leetcode"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left == 0 or right == 0: # 根节点只有一棵子树
            return left + right + 1
        else:
            return min(left, right) + 1


p = root = TreeNode(0)
p.left = TreeNode(2)
print(Solution().minDepth(root))
