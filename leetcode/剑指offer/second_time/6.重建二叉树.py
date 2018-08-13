# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None

        startPreOrder = 0
        endPreOrder = len(pre) - 1
        startInOrder = 0
        endInOrder = len(tin) - 1

        return self.reConstructBinaryTree_main(pre, startPreOrder, endPreOrder,
                                        tin, startInOrder, endInOrder)

    def reConstructBinaryTree_main(self, pre, startPreOrder, endPreOrder, tin, startInOrder, endInOrder):
        rootValue = pre[startPreOrder]
        root = TreeNode(rootValue)
        root.left = root.right = None

        # 在中序遍历中找到根节点的位置
        rootInOrder = startInOrder

        while rootInOrder < endInOrder and tin[rootInOrder] != rootValue:
            rootInOrder += 1

        if rootInOrder == endInOrder and tin[rootInOrder] != rootValue:
            return "非法输入"

        leftLength = rootInOrder - startInOrder
        leftPreOrderEnd = startPreOrder + leftLength
        if leftLength > 0:
            root.left = self.reConstructBinaryTree_main(pre, startPreOrder + 1, leftPreOrderEnd, tin, startInOrder,
                                                        rootInOrder - 1)

        if leftLength < endPreOrder - startPreOrder:
            root.right = self.reConstructBinaryTree_main(pre, leftPreOrderEnd + 1, endPreOrder, tin, rootInOrder + 1,
                                                         endInOrder)
        return root


# pre = [1, 2, 4, 7, 3, 5, 6, 8]
# tin = [4, 7, 2, 1, 5, 3, 8, 6]
pre = [1, 2, 3, 4, 5, 6, 7]
tin = [3, 2, 4, 1, 6, 5, 7]
print(Solution().reConstructBinaryTree(pre, tin).val)
