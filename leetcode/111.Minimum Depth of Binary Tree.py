"""
求一棵二叉树的最低深度
从根节点到叶子节点的最短路径长度

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minimumDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 0 # 判断当前节点是否为叶子节点（找到以叶子节点为结束的路径）

        return min(self.minimumDepth(root.left), self.minimumDepth(root.right)) + 1


p = root = TreeNode(0)
# p.left = TreeNode(2)
print(Solution().minimumDepth(root))
