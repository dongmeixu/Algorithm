"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 节点被重复遍历了。。。。
    def isBalanced(self, root):
        if not root:
            return True
        left = self.TreeDepth(root.left)
        right = self.TreeDepth(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def TreeDepth(self, root):
        # 如果为空，则返回0
        if not root:
            return 0
        # 递归的求其左子树与右子树的深度
        return max(self.TreeDepth(root.left),
                   self.TreeDepth(root.right)) + 1