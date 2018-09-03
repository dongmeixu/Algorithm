# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    res = []

    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k <= 0:
            return None
        self.inOrder(pRoot)

        if k > len(self.res):
            return None
        else:
            return self.res[k - 1].val

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.res.append(root)
        self.inOrder(root.right)


p = root = TreeNode(8)
p.left = TreeNode(6)
p.right = TreeNode(10)
p.left.left = TreeNode(5)
p.left.right = TreeNode(7)
p.right.left = TreeNode(9)
p.right.right = TreeNode(11)
print(Solution().KthNode(root, 8))