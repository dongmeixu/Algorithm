"""
facebook
404:求出一棵二叉树所有左叶子的和

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    sumOfLeft = 0

    def sum(self, root):
        # 递归终止条件
        if not root:
            return 0
        if not root.left and not root.right: # 是叶子节点
            return 0
        # 递归过程
        if root.left: # 递归的主要操作
            self.sumOfLeft += root.left.val
        self.sum(root.left)  # 递归调用该节点的左子树
        self.sum(root.right)  # 递归调用该节点的右子树
        return self.sumOfLeft


p = root = TreeNode(3)
p.left = TreeNode(9)
p.right = TreeNode(20)
p.left.left = TreeNode(1)
p.right.left = TreeNode(15)
p.right.right = TreeNode(7)
print(Solution().sum(root))