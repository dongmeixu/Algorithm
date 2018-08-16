"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 思路：先先序遍历二叉树将结果保存到列表中，然后遍历链表，修改指针
class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res = self.preorderTraversal(root)
        for i in range(len(res) - 1):
            res[i].right = res[i + 1]
            res[i].left = None
        # return res

    def preorderTraversal(self, root):
        res = []
        return self.dfs(root, res)

    def dfs(self, root, res):
        if not root:
            return res
        res.append(root)
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        return res


head = TreeNode(0)
p = head
p.left = TreeNode(1)
p.right = TreeNode(2)
p.left.left = TreeNode(3)
rs = Solution().flatten(head)
for tmp in rs:
    print(tmp.val)
