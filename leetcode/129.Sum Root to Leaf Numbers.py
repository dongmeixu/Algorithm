"""
给定一棵二叉树，每个节点只包含数字0-9，
从根节点到叶子节点的每条路径可以表示成一个数，
求这些数的和。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = []
    num = []

    def s(self, root):
        if not root:
            return 0
        self.num += str(root.val)
        # print(self.num)

        # res用于保存每个从根节点到叶子节点的路径代表的一个数字
        if not root.left and not root.right:
            tmp = ""
            for s in self.num[:]:
                tmp += s
            self.res.append(int(tmp))
        else:
            if root.left:
                self.s(root.left)
            if root.right:
                self.s(root.right)
        self.num.pop()

        # 后处理，将所有数字求和
        final = 0
        for i in self.res:
            final += i
        return final


p = root = TreeNode(1)
p.left = TreeNode(3)
p.right = TreeNode(3)
print(Solution().s(root))
