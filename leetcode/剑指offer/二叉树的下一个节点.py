# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    stack = []
    target = TreeLinkNode(0)

    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return -1
        inorder = self.GetInorder(pNode)
        print(self.stack)
        index = inorder.index(self.target.val)
        return inorder[index + 1]

    def GetInorder(self, pNode):
        if not pNode:
            return -1

        if not pNode.left and not pNode.right:
            return pNode.val
        self.stack.append(self.GetNext(pNode.left))
        self.stack.append(pNode.val)
        self.stack.append(self.GetNext(pNode.right))

        # 此时已经得到了中序遍历的结果
        target = TreeLinkNode(1)
        # index = self.stack.index(target.val)
        # print(self.stack[index + 1])
        return self.stack


root = p = TreeLinkNode(0)
p.left = TreeLinkNode(1)
p.right = TreeLinkNode(2)
print(Solution().GetNext(root))
