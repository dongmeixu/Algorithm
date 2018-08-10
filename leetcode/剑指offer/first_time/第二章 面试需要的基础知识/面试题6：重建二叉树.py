"""
题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None

        startPreorder = 0
        endPreorder = len(pre) - 1
        startInorder = 0
        endInorder = len(tin) - 1

        return self.reConstructBinaryTreeMain(pre, startPreorder, endPreorder, tin, startInorder, endInorder)

    # 根据前序遍历序列的第一个数字创建根节点，接下来在中序遍历序列中找到根节点的位置，
    # 这样就能确定左右子树节点的数量。
    # 在前序遍历和中序遍历的序列中划分了左右子树节点的值之后，就可以递归的调用函数，分别构建它的左右子树
    def reConstructBinaryTreeMain(self, pre, startPreorder, endPreorder, tin, startInorder, endInorder):
        # 前序遍历的第一个数字是根节点的值
        rootValue = pre[startPreorder]
        root = TreeNode(rootValue)
        root.left = root.right = None

        # 在中序遍历中找到根节点的值
        rootInorder = startInorder
        while rootInorder < endInorder and tin[rootInorder] != rootValue:
            rootInorder += 1

        # 中序遍历中没有这个根节点
        if rootInorder == endInorder and tin[rootInorder] != rootValue:
            print("非法输入")

        # 左子树的长度
        leftLength = rootInorder - startInorder

        leftPreorderEnd = startPreorder + leftLength

        if leftLength > 0:
            root.left = self.reConstructBinaryTreeMain(pre, startPreorder + 1, leftPreorderEnd, tin, startInorder,
                                                       rootInorder - 1)

        if leftLength < endPreorder - startPreorder:
            root.right = self.reConstructBinaryTreeMain(pre, leftPreorderEnd + 1, endPreorder, tin, rootInorder + 1,
                                                        endInorder)

        # print(root.val)
        return root


pre = [1, 2, 4, 7, 3, 5, 6, 8]
tin = [4, 7, 2, 1, 5, 3, 8, 6]
Solution().reConstructBinaryTree(pre, tin)
