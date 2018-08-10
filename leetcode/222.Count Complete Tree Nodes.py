"""
给定一棵完全二叉树，求完全二叉树的节点个数

完全二叉树：除了最后一层，所有层的节点数达到最大，与此同时，最后一层的所有节点都在最左侧（堆使用完全二叉树）

满二叉树：所有层的节点数达到最大

"""


"""
解题思路：先求出二叉树的深度 level。
根据完全二叉树的结构特点，可以求头结点右子树的深度，
如果右子树的深度与完全二叉树的深度一致，那么左子树即为层数为level的满的完全二叉树，可用公式求出左子树的节点数；
若右子树深度比二叉树深度小，那么右子树为深度为level-1的满二叉树，可用公式求出右子树节点数；剩下的部分同样的道理既可以递归得出。

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = 0

    def main(self, root):
        if not root:
            return 0
        depth_root = self.depth(root)
        depth_right = self.depth(root.right) + 1
        if depth_root == depth_right:  # 左子树一定是满二叉树
            self.res += 2 ** (depth_right - 1) + self.main(root.right)
        elif depth_right == depth_root - 1:
            self.res += 2 ** (depth_right - 1) + self.main(root.left)
        return self.res

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1


p = root = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.left.left = TreeNode(4)
p.left.right = TreeNode(5)
print(Solution().main(root))