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
    def Convert(self, pRootOfTree):
        # write code here
        pLastNodeInList = TreeNode(0)
        self.ConvertNode(pRootOfTree, pLastNodeInList)

        # pLastNodeInList 指向双向链表的尾节点
        # 我们需要返回头结点
        pHeadOfList = pLastNodeInList
        while pHeadOfList and pHeadOfList.left and pHeadOfList.right:
            pHeadOfList = pHeadOfList.left

        return pHeadOfList

    def ConvertNode(self, pNode, pLastNodeInList):
        if not pNode:
            return
        pCurrent = pNode
        if pCurrent.left:
            self.ConvertNode(pCurrent.left, pLastNodeInList)

        pCurrent.left = pLastNodeInList
        if pLastNodeInList:
            pLastNodeInList.right = pCurrent

        pLastNodeInList = pCurrent

        if pCurrent.right:
            self.ConvertNode(pCurrent.right, pLastNodeInList)