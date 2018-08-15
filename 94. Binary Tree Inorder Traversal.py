# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        return self.dfs(root, res)

    def dfs(self, root, res):
        if not root:
            return res

        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)
        return res


p = root = TreeNode(1)
p.right = TreeNode(2)
p.right.left = TreeNode(3)
print(Solution().inorderTraversal(root))
