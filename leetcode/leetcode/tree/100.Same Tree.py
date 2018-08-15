# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""递归DFS"""
# class Solution:
#     def isSameTree(self, p, q):
#         """
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: bool
#         """
#         if not p or not q:
#             return p == q
#
#         if p.val != q.val:
#             return False
#
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

"""stack"""
# class Solution(object):
#     def isSameTree(self, p, q):
#         stack = [(p, q)]
#         while stack:
#             n1, n2 = stack.pop()
#             if not n1 and not n2: continue
#             if not n1 or not n2: return n1 == n2
#             if n1.val != n2.val: return False
#             stack.append((n1.right, n2.right))
#             stack.append((n1.left, n2.left))
#         return True

"""queue"""
import collections


class Solution(object):
    def isSameTree(self, p, q):
        queue = collections.deque([(p, q)])
        while queue:
            n1, n2 = queue.popleft()
            if not n1 and not n2: continue
            if not n1 or not n2: return n1 == n2
            if n1.val != n2.val: return False
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))
        return True


p = root1 = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = root2 = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
print(Solution().isSameTree(root1, root2))
