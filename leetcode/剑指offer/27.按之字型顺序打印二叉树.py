# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        current = [pRoot]
        layer = 1
        result = []
        while len(current) > 0:
            next = []
            for node in current:
                # print(layer & 1 == 1)
                result.append(node.val)
                print(result)
                layer += 1
            if layer & 1 == 1:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            else:
                if node.left:
                    next.append(node.right)
                if node.right:
                    next.append(node.left)
            # layer += 1
            current = next
        return result


treeNode1 = TreeNode(1)
p = treeNode1
p.left = TreeNode(2)
p.right = TreeNode(3)
p.left.left = TreeNode(4)
s = Solution().Print(p)
print(s)