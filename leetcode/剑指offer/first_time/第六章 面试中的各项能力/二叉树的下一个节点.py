# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# 思路：中序遍历，然后再找当前节点的下一个节点，
# 但得先通过getNext方法找到二叉树的根节点
class Solution:
    res = []

    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None

        # 找到根节点
        p = pNode
        while p.next:
            p = p.next

        self.inOrder(p)
        if self.res.index(pNode) != len(self.res) - 1:
            return self.res[self.res.index(pNode) + 1]
        else:
            return None

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.res.append(root)
        self.inOrder(root.right)
