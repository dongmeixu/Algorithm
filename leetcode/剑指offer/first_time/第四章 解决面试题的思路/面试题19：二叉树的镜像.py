# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


""" 
前序遍历这棵树的每个节点，如果遍历到的节点有子节点，
就交换它的两个子节点。
当交换完所有非叶子节点的左右子节点之后，就得到了树的镜像.

"""


# 1.根为空，返回
# 2.交换左右子树
# 4.递归交换
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # # 递归算法
        # if not root:
        #     return root
        # # 交换左右子树
        # tmp = root.left
        # root.left = root.right
        # root.right = tmp
        # # 递归交换
        # if root.left:
        #     self.Mirror(root.left)
        # if root.right:
        #     self.Mirror(root.right)

        # 非递归算法
        if not root:
            return root

        stack = [root]
        while len(stack) > 0:
            node = stack.pop(0)
            tmp = node.left
            node.left = node.right
            node.right = tmp
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)



