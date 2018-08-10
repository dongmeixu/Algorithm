# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
最开始的思路：
递归：
    判断左右子树是否全为空，为空则return
    定义临时变量，交换左右子树
    递归当前树的左右子树
"""

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return root

        # 交换左右子树
        tmp = root.left
        root.left = root.right
        root.right = tmp

        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)


