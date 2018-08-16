"""
Given a binary tree, return the postorder traversal of its nodes’ values.
For example: Given binary tree {1,#,2,3},
1
\
2
/
3
return [3,2,1].
Note: Recursive solution is trivial, could you do it iteratively?
"""

"""已通过leetcode"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root):
        res = []
        return self.dfs(root, res)

    def dfs(self, root, res):
        if not root:
            return res
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)
        return res


"""
非递归：
1.设置2个栈：stack1 and stack2
2.将根节点压入stack1

3.弹出stack1的栈顶元素，并将其压入到stack2
4.将刚才的栈顶元素的左右孩子依次入栈stack1
执行3-4直到stack1为空======> 此时stack2中的元素从栈顶到栈低的顺序依次为左右根

5.当所有元素都已经入栈stack2后，依次从stack2中弹出元素并访问
"""


class Solution_1:
    def postorderTraversal(self, root):
        res = []
        if not root:
            return res

        stack1 = [root]
        stack2 = []

        while stack1:
            top = stack1[-1]
            stack1.pop()
            stack2.append(top)
            if top.left:
                stack1.append(top.left)
            if top.right:
                stack1.append(top.right)

        while stack2:
            top = stack2[-1]
            res.append(top.val)
            stack2.pop()

        return res


"""
一个栈实现的。。。。。。
"""


class Solution_2:
    def postorderTraversal(self, root):
        pass


head = TreeNode(0)
p = head
p.left = TreeNode(1)
p.right = TreeNode(2)
p.left.left = TreeNode(3)
print(Solution().postorderTraversal(head))
print(Solution_1().postorderTraversal(head))
