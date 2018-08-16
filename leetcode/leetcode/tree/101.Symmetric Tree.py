"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""

"""PASS"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.isSameTree(root.left, root.right)

    # def isSameTree(self, p, q): # 这部分代码跟100.Same Tree一样的
    #     if not p or not q:
    #         return p == q
    #
    #     if p.val != q.val:
    #         return False
    #
    #     # 注意题目的语义！！！！
    #     return self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)

    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if not n1 and not n2: continue
            if not n1 or not n2: return n1 == n2
            if n1.val != n2.val: return False
            stack.append((n1.right, n2.left))
            stack.append((n1.left, n2.right))
        return True


p = root1 = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = root2 = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
print(Solution().isSymmetric(root1))
