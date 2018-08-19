"""
给出一棵二叉树以及一个数字sum，
判断在这棵二叉树上是否存在一条从根到叶子的路径，
其路径上的所有节点和为sum
"""

"""
注意递归终止条件！！！！！！！！
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        # 递归终止条件：当这棵树只有右子树，且根节点的值等于5=====》这个时候其实是错的
        if not root:
            return False
        if not root.left and not root.right: # 忽略了当前节点的上层节点是叶子节点的情况
            return root.val == sum

        # 递归结构
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)