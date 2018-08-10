"""

题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。

"""

# 思路：树的层次遍历，队列

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        res = []
        if not root:
            return []
        currentStack = [root]  # 用list模拟队列
        while currentStack:
            nextStack = []
            for i in currentStack:
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
                res.append(i.val)
                currentStack = nextStack
        return res

    def PrintFromTopToBottom_1(self, root):
        # write code here
        # BFS广度优先搜索
        if not root:
            return []
        queue = [] # 节点入队列
        res = []
        queue.append(root)
        while len(queue) > 0:  # 如果队列中有元素，则将该元素出队，再将其子节点入队列
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

treeNode1 = TreeNode(1)
p = treeNode1
p.left = TreeNode(2)
p.right = TreeNode(3)
p.left.left = TreeNode(4)


s = Solution().PrintFromTopToBottom_1(p)
print(s)