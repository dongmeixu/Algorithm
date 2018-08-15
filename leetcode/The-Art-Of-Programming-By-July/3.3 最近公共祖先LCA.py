class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 树是个二叉排序树的情况
class Solution:
    def LCA(self, root, p1, p2):
        if not root:
            return

        # 三个节点的值都相等
        if root.val == p1.val == p2.val:
            return root

        # TODO:之前写的代码在if、elif语句那块没写return， 导致最后返回的都是None!!!!
        if p1.val < root.val and p2.val < root.val:
            return self.LCA(root.left, p1, p2)
        elif p1.val > root.val and p2.val > root.val:
            return self.LCA(root.right, p1, p2)
        else:
            return root

    def LCA_binarySearchTree(self, root, p1, p2):
        if not root:
            return

        # 三个节点的值都相等
        if root.val == p1.val == p2.val:
            return root

        """下面的代码由之前的三个元素值比较大小转化为两个元素比较大小，后面的判断语句会更简便一点"""
        # 二叉查找树内，如果左结点大于右结点，不对，交换
        if p1.val > p2.val:  # 交换值,保证p1的值永远是最小的（p1.val > p2.val总是成立）
            tmp = p1.val
            p1.val = p2.val
            p2.val = tmp

        while True:
            if root.val > p1.val:
                root = root.left
            elif root.val < root.val:
                root = root.right
            else:
                return root

    def LCA_notBinarySearchTree(self, root, p1, p2):
        if not root:
            return

        if root.val == p1.val or root.val == p2.val:
            return root

        left = self.LCA_notBinarySearchTree(root.left, p1, p2)
        right = self.LCA_notBinarySearchTree(root.right, p1, p2)

        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return


p = root = TreeNode(4)
p.left = TreeNode(2)
p.right = TreeNode(6)
p.left.left = TreeNode(1)
p.left.right = TreeNode(3)
p.right.left = TreeNode(5)
p.right.right = TreeNode(7)
print(Solution().LCA(root, TreeNode(2), TreeNode(3)).val)
print(Solution().LCA_binarySearchTree(root, TreeNode(2), TreeNode(3)).val)
print(Solution().LCA_notBinarySearchTree(root, TreeNode(2), TreeNode(3)).val)
