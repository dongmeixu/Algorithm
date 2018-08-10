"""
题目描述
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        res = []
        treepath = self.dfs(root)
        for i in treepath:
            if sum(map(int, i.split('->'))) == expectNumber:
                res.append(list(map(int, i.split('->'))))
        return res

    def dfs(self, root):
        if not root: return []
        if not root.left and not root.right:
            return [str(root.val)]
        treePath = [str(root.val) + "->" + path for path in self.dfs(root.left)]
        treePath += [str(root.val) + "->" + path for path in self.dfs(root.right)]
        return treePath


p = TreeNode(8)
p.left = TreeNode(6)
p.right = TreeNode(10)
p.left.left = TreeNode(5)
p.left.right = TreeNode(5)
p.right.left = TreeNode(9)
p.right.right = TreeNode(11)

s = Solution().FindPath(p, 19)
print(s)
