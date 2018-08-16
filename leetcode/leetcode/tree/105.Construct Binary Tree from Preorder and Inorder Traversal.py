"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

"""根据前序序列、中序序列重构二叉树PASS"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return []

        if len(preorder) != len(inorder):
            return []

        startPreOrder = 0
        endPreOrder = len(preorder) - 1

        startInOrder = 0
        endInOrder = len(inorder) - 1

        return self.bulidTree_main(preorder, startPreOrder, endPreOrder, inorder, startInOrder, endInOrder)

    def bulidTree_main(self, preorder, startPreOrder, endPreOrder, inorder, startInOrder, endInOrder):

        rootValue = preorder[startPreOrder]
        root = TreeNode(rootValue)

        # 找到在中序遍历中根节点的位置
        rootInOrder = startInOrder
        while rootInOrder < endInOrder and inorder[rootInOrder] != rootValue:
            rootInOrder += 1

        # 遍历中序序列，如果找不到根节点，应该提示
        while rootInOrder == endInOrder and inorder[rootInOrder] != rootValue:
            print("输入有误")

        leftLength = rootInOrder - startInOrder
        # rightLength = endInOrder - rootInOrder
        leftPreorderEnd = startPreOrder + leftLength  # 因为在前序遍历中左子树跟右子树是挨着的

        if leftLength:
            root.left = self.bulidTree_main(preorder, startPreOrder + 1, leftPreorderEnd, inorder, startInOrder,
                                            rootInOrder - 1)

        if leftLength < endPreOrder - startPreOrder:
            root.right = self.bulidTree_main(preorder, leftPreorderEnd + 1, endPreOrder, inorder, rootInOrder + 1,
                                             endInOrder)

        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
print(Solution().buildTree(preorder, inorder))
