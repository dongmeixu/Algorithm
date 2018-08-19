# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
> 类型：DFS遍历
> Time Complexity O(n)
> Space Complexity O(1)


暴力解法：
利用数组储存inorder过的数，如果出现重复，或者数组不等于sorted(arr)，证明不是Valid Tree.这个解法比较易读，如果对Space Complexity要求不严格，可以通过比对数组里面的数而不是sorted(arr)来达到O(N)时间复杂。
"""


# class Solution:
#     res = []
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if not root:
#             return True
#
#         self.dfs_inorder(root)
#
#         return self.res == sorted(self.res) and len(self.res) == len(set(self.res))
#
#     def dfs_inorder(self, root):
#         # 树为空
#         if not root:
#             return
#
#         self.dfs_inorder(root.left)
#         self.res.append(root.val)
#         self.dfs_inorder(root.right)


"""
O(1) Space解法：
在上面的算法里进行了优化，每次只需要将当前root.val和上次储存的self.last比对即可知道是否满足条件。然后设立self.flag用于返回。
"""
import sys
class Solution:
    last = -sys.maxsize - 1
    flag = True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.inorder(root)
        return self.flag

    def inorder(self, root):
        # 树为空
        if not root:
            return

        self.inorder(root.left)
        if self.last >= root.val:
            self.flag = False
        self.last = root.val
        self.inorder(root.right)