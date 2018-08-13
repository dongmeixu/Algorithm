"""
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：我们约定空树不是任意一个树的子结构）
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False

        result = False
        if pRoot1.val == pRoot2.val:
            result = self.IsSubtree(pRoot1, pRoot2)

        if not result:  # 在tree1的左子树查找是否包含tree2
            result = self.HasSubtree(pRoot1.left, pRoot2)

        if not result:  # 在tree1的右子树查找是否包含tree2
            result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def IsSubtree(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        else:
            return self.IsSubtree(pRoot1.left, pRoot2.left) and self.IsSubtree(pRoot1.right, pRoot2.right)


