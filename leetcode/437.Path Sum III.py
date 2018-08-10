"""
给出一棵二叉树以及一个数字sum,判断在这棵二叉树上存在多少条路径，其路径上的所有节点和为sum
-其中路径不一定要起始于根节点；终止于叶子节点
-路径可以从任意节点开始，但是只能是向下走的。

"""


class Solution:
    # 在以root为根节点的二叉树中，寻找和为sum的路径，返回这样的路径个数
    def pathSum(self, root, sum):
        if not root:
            return 0
        # 处理包含当前节点和为sum的路径个数
        res = self.findPath(root, sum)
        # 处理不包含当前节点和为sum的路径个数
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)

        return res

    # 在以node为根节点的二叉树中，寻找包含node的路径，和为num返回这样的路径个数
    def findPath(self, node, num):
        if not node:
            return 0
        res = 0
        if node.val == num:
            res += 1
        res += self.findPath(node, num - node.val)
        res += self.findPath(node, num - node.val)

        return res
