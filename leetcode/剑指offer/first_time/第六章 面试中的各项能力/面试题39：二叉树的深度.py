"""
输入一棵二叉树的根节点，求该树的深度。
从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, root):
        # 如果为空，则返回0
        if not root:
            return 0
        # 递归的求其左子树与右子树的深度
        return max(self.TreeDepth(root.left),
                   self.TreeDepth(root.right)) + 1