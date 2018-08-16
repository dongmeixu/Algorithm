"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""PASS"""

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res = self.inorderTraversal(root)
        first = 0
        sec = len(res) - 1

        for i in range(1, len(res)):
            if res[first].val < res[i].val:
                first += 1
            else:
                break

        for i in range(len(res) - 2, first, -1):
            if res[sec].val > res[i].val:
                sec -= 1
            else:
                break
        # 交换
        tmp = res[first].val
        res[first].val = res[sec].val
        res[sec].val = tmp

    def inorderTraversal(self, root):
        res = []
        return self.dfs(root, res)

    def dfs(self, root, res):
        if not root:
            return res
        self.dfs(root.left, res)
        res.append(root)
        self.dfs(root.right, res)
        return res
