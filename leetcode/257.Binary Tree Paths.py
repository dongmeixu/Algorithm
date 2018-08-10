"""
给定一棵二叉树，返回所有表示从根节点到叶子节点路径的字符串
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        res = []
        if not root:
            return res
        # 已经到达了叶子节点
        if not root.left and not root.right:
            res.append(str(root.val))

        leftS = self.binaryTreePaths(root.left)
        for s in leftS:
            res.append(str(root.val) + "->" + s)
        rightS = self.binaryTreePaths(root.right)
        for s in rightS:
            res.append(str(root.val) + "->" + s)

        print(res)
        return res


h = root = TreeNode(1)
left1 = h.left = TreeNode(2)
right1 = h.right = TreeNode(3)
left1.left = TreeNode(4)
left1.right = TreeNode(5)
right1.left = TreeNode(6)
right1.right = TreeNode(7)

Solution().binaryTreePaths(root)