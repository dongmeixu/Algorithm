"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
"""根据中序序列跟后序序列重构二叉树PASS"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder or len(inorder) != len(postorder):
            return []

        startInOrder = 0
        endInOrder = len(inorder) - 1
        startPostOrder = 0
        endPostOrder = len(postorder) - 1

        return self.buildTree_main(inorder, startInOrder, endInOrder, postorder, startPostOrder, endPostOrder)

    def buildTree_main(self, inorder, startInOrder, endInOrder, postorder, startPostOrder, endPostOrder):
        # 根节点
        rootValue = postorder[endPostOrder]
        root = TreeNode(rootValue)

        # 在中序遍历中找到该根节点
        rootInOrder = startInOrder
        while rootInOrder < endInOrder and inorder[rootInOrder] != rootValue:
            rootInOrder += 1

        while rootInOrder == endInOrder and inorder[rootInOrder] != rootValue:
            print("非法")

        leftLength = rootInOrder - startInOrder
        leftEnd = startPostOrder + leftLength

        if leftLength:
            root.left = self.buildTree_main(inorder, startInOrder, rootInOrder - 1, postorder, startPostOrder,
                                            leftEnd - 1)
        if leftLength < endInOrder - startInOrder:
            root.right = self.buildTree_main(inorder, rootInOrder + 1, endInOrder, postorder, leftEnd, endPostOrder - 1)

        return root


ino = [9, 3, 15, 20, 7]
post = [9, 15, 7, 20, 3]
root = Solution().buildTree(ino, post)
