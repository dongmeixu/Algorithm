"""
Given a binary tree, return the preorder traversal of its nodes’ values.
For example: Given binary tree {1,#,2,3},
1
\
2
/
3
return [1,2,3].
Note: Recursive solution is trivial, could you do it iteratively?
"""

"""已通过leetcode"""
# 递归方式:
# 二叉树遍历的递归实现，每个结点只需遍历一次，故时间复杂度为O(n)。
# 而使用了递归，最差情况下递归调用的深度为O(n)，所以空间复杂度为O(n)。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""底边的代码在leetcode上无法运行通过"""
"""好像是不能用递归，按照leetcode的处理模式，所有树的根节点都可以认为是前一个树最后一个节点的右子节点"""


# class Solution:
#     res = []
#
#     def preorderTraversal(self, root):
#         if not root:
#             return self.res
#         self.res.append(root.val)
#         self.preorderTraversal(root.left)
#         self.preorderTraversal(root.right)
#         return self.res

class Solution:

    def preorderTraversal(self, root):
        res = []
        return self.dfs(root, res)

    def dfs(self, root, res):
        if not root:
            return res
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        return res


# 非递归方式：stack  时间复杂度O(n),空间复杂度O(n)
"""
1.根节点入栈

2.每次从栈顶弹出一个元素，访问该节点
3.把该节点的右孩子入栈
4.把该节点的左孩子入栈

5.重复执行2-4，直到栈为空
"""


class Solution_1:
    res = []

    def preorderTraversal(self, root):
        # 用于保存遍历结果的辅助空间
        res = []

        if not root:
            return res

        stack = [root]

        while len(stack) > 0:
            top = stack[-1]
            stack.pop()
            res.append(top.val)

            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)

        return res


head = TreeNode(0)
p = head
p.left = TreeNode(1)
p.right = TreeNode(2)
p.left.left = TreeNode(3)
print(Solution().preorderTraversal(head))

print(Solution_1().preorderTraversal(head))
