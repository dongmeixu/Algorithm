"""
一、先序遍历对二叉树进行序列化
    1.假设序列化结果为str，初始时str为空字符串
    2.先序遍历二叉树时如果遇到空节点，在str末尾加上“#！”
    3.如果遇到不为空的节点，假设节点值为3，就在str末尾加上“3！”



三、按层遍历的方式进行二叉树进行序列化
    1.用队列来进行二叉树的按层遍历，即宽度优先便利。
    2.除了访问节点的顺序是按层遍历之外，对结果字符串的处理，与之间介绍的处理方式一样
    3.反序列化过程一样
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    result = ""

    def preSerialize(self, root):
        # write code here
        if root is None:
            self.result += "#!"
        if root:
            self.result += str(root.val) + "!"
            self.preSerialize(root.left)
            self.preSerialize(root.right)

        return self.result

    def preSerialize_ditui(self, root):
        res = ""
        currentStack = [root]
        while len(currentStack) > 0:
            node = currentStack.pop(-1)
            if node is None:
                res += "#!"
            else:
                res += str(node.val) + "!"
                currentStack.append(node.right)
                currentStack.append(node.left)
        return res

    def midSerialize(self, root):
        # write code here
        if root is None:
            self.result += "#!"
        if root:
            self.midSerialize(root.left)
            self.result += str(root.val) + "!"
            self.midSerialize(root.right)

        return self.result

    def midSerialize_ditui(self, root):
        res = ""
        currentStack = [root]
        p = root
        while p:
            currentStack.append(p.left)
            p = p.left
        # currentStack.append(None)
        print(len(currentStack))
        while len(currentStack) > 0:
            # print(len(currentStack))
            node = currentStack.pop(-1)
            if node is None:
                res += "#!"
            else:
                res += str(node.val) + "!"
                if node == root:
                    currentStack.append(node.right)
                    currentStack.append(node.right.left)
                else:
                    currentStack.append(node.right)
        return res

    def preDeserialize(self, s):
        # write code here
        values = s.strip().split("!")[:-1]
        # print(values)
        return self.preOrder(values)

    def preOrder(self, values):
        value = values.pop(0)
        if value == "#":
            return None
        head = TreeNode(int(value))
        head.left = self.preOrder(values)
        head.right = self.preOrder(values)
        return head


node = TreeNode(12)
node.left = TreeNode(3)
node.right = TreeNode(4)
node.left.left = TreeNode(5)
s = Solution().preSerialize(node)
print(s)
s = Solution().preSerialize_ditui(node)
print(s)
s = Solution().midSerialize(node)
print(s)
s = Solution().midSerialize_ditui(node)
print(s)
ss = "12!3!5!#!#!#!4!#!#!"
# Solution().preDeserialize(ss)
