# -*- coding:utf-8 -*-
"""

题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        nodeStack = [pRoot]
        result = []
        while nodeStack:
            res = []
            nextStack = []
            for node in nodeStack:
                res.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            nodeStack = nextStack
            result.append(res)
        return result

    def Print_2(self, pRoot):
        # write code here
        if not pRoot:
            return []

        # last:表示正在打印的当前行的最右节点
        # nlast:表示下一行的最右节点
        last = nlast = pRoot
        queue = [pRoot]
        result = []
        layer_list = []
        while len(queue) > 0:
            node = queue.pop(0)
            layer_list.append(node.val)
            if node.left:
                queue.append(node.left)
                nlast = node.left
            if node.right:
                queue.append(node.right)
                nlast = node.right
            if last == node:
                result.append(layer_list)  # 此时一行已经遍历完，将这行数据加到result中，
                last = nlast               # 同时更新last与nlast,并重置layer_list
                layer_list = []
        return result


treeNode1 = TreeNode(1)
p = treeNode1
p.left = TreeNode(2)
p.right = TreeNode(3)
p.left.left = TreeNode(4)

s = Solution().Print(p)
print(s)
s = Solution().Print_2(p)
print(s)