# -*- coding:utf-8 -*-
"""
题目描述
输入一棵二叉搜索树，
将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    pLastNodeInList = None

   # 将pLastNodeInList 作为参数传到ConvertNode中，由于递归操作的存在，最后返回的结果是有问题的
    def Convert(self, pRootOfTree):
        # write code here
        self.ConvertNode(pRootOfTree)

        # pLastNodeInList 指向双向链表的尾节点
        # 我们需要返回头结点
        pHeadOfList = self.pLastNodeInList
        while pHeadOfList and pHeadOfList.left:
            pHeadOfList = pHeadOfList.left

        return pHeadOfList

    def ConvertNode(self, pNode):
        if not pNode:
            return
        pCurrent = pNode
        if pCurrent.left:
            self.ConvertNode(pCurrent.left)

        pCurrent.left = self.pLastNodeInList
        if self.pLastNodeInList:
            self.pLastNodeInList.right = pCurrent

        self.pLastNodeInList = pCurrent

        if pCurrent.right:
            self.ConvertNode(pCurrent.right)


p = root = TreeNode(8)
p.left = TreeNode(6)
p.right = TreeNode(10)
p.left.left = TreeNode(5)
p.left.right = TreeNode(7)
p.right.left = TreeNode(9)
p.right.right = TreeNode(11)

print(Solution().Convert(root).val)
