"""
求一棵二叉树的最高深度，从根节点到叶子节点的最长路径长度
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        # 递归终止条件
        if not root:
            return 0
        # 递归结构
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


head = TreeNode(0)
p = head
p.left = TreeNode(1)
p.right = TreeNode(2)
p.left.left = TreeNode(3)

print(Solution().maxDepth(head))