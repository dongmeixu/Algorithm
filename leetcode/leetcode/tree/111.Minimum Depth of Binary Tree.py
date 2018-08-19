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


# 递归版本
# 时间复杂度O(n)，空间复杂度O(n)
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

    def minDepth_ditui(self, root):
        if not root:
            return 0
        import sys
        max = sys.maxsize

        stack = [(root, 1)]
        while len(stack) != 0:
            node, depth = stack[-1]
            stack.pop()
            if not root.left and not root.right:
                max = min(max, depth)
            if root.left and depth < max:  # 深度控制，剪枝
                stack.append((root.left, depth + 1))
                root = root.left
            if root.right and depth < max:    # 深度控制，剪枝
                stack.append((root.right, depth + 1))
                root = root.right
        return max


p = root = TreeNode(0)
p.left = TreeNode(2)
print(Solution().minDepth(root))
print(Solution().minDepth_ditui(root))
