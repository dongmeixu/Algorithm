# -*- coding:utf-8 -*-
"""
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""
"""
解题思路：实质上是二叉树的层次遍历，利用列表模拟队列
    1.根节点入队
    2.从队列头部取出一个节点，打印该节点，将该节点的左右子树入队列
    3.重复2，直至该队列为空
"""
"""
本题扩展：
    如何广度优先遍历一个有向图？这同样也可以基于队列实现。
    树是图的一种特殊退化形式，从上到下按层遍历二叉树，从本质上来说就是广度优先遍历二叉树。
    
举一反三：
    不管是广度优先遍历一个有向图还是一棵树，都要用到队列。
    1.第一步我们把起始结点（对树而言是根节点）放入队列中。
    2.接下来每一次从队列的头部取出一个结点，遍历这个结点之后把它能到达的节点（对树而言是子节点）都依次放入队列。
    3.重复这个过程，直到队列中的节点全部被遍历为止
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        result = [] # 保存结果
        if not root:
            return result
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)  # 出队列
            result.append(node.val) # 打印该节点的值
            if node.left:
                queue.append(node.left) # 左孩子入队
            if node.right:
                queue.append(node.right) # 右孩子入队
        return result


p = TreeNode(8)
p.left = TreeNode(6)
p.right = TreeNode(10)
p.left.left = TreeNode(5)
p.left.right = TreeNode(7)
p.right.left = TreeNode(9)
p.right.right = TreeNode(11)

re = Solution().PrintFromTopToBottom(p)
print(re)