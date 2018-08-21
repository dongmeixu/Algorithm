"""
Given a binary tree, return the inorder traversal of its nodes’ values.
For example: Given binary tree {1,#,2,3},
1
\
2
/
3
return [1,3,2].
Note: Recursive solution is trivial, could you do it iteratively?

"""
"""已通过leetcode"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 下面的无法通过leetcode
# class Solution:
#     res = []
#
#     def inorderTraversal(self, root):
#         if not root:
#             return self.res
#         self.inorderTraversal(root.left)
#         self.res.append(root.val)
#         self.inorderTraversal(root.right)
#         return self.res

class Solution:

    def inorderTraversal(self, root):
        res = []
        return self.dfs(root, res)

    def dfs(self, root, res):
        if not root:
            return res
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)
        return res


# 非递归方式：stack  时间复杂度O(n),空间复杂度O(n)
"""
1.初始化一个二叉树节点pNode指向根节点
2.若pNode非空，将pNode入栈，然后把pNode指向其左孩子（直到最左边的节点）
3.若pNode空，弹出栈顶的结点，并访问该结点，将pNode指向其右孩子（访问最左边的结点，并遍历其右子树）
"""
class Solution_1:

    def inorderTraversal(self, root):
        # 用于保存遍历结果的辅助空间
        res = []
        stack = []

        if not root:
            return res

        pNode = root

        while pNode or len(stack) > 0:
            if pNode:
                stack.append(pNode)
                pNode = pNode.left
            else:
                top = stack[-1]
                stack.pop()
                res.append(top.val)
                pNode = top.right

        return res


head = TreeNode(0)
p = head
p.left = TreeNode(1)
p.right = TreeNode(2)
p.left.left = TreeNode(3)
print(Solution().inorderTraversal(head))
print(Solution_1().inorderTraversal(head))
