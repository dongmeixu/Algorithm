# -*- coding:utf-8 -*-
"""
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

"""
"""
解题思路：
    二叉搜素树：左《根《右
    后序遍历：最后一个节点是根节点，剩下的部分，比根节点值小的为其左子树，比其值大的为其右子树
相关题目：
    输入一个整数数组，判断该数组是不是某二叉搜索树的前序遍历的结果。
    只是在前序遍历得到的序列中，第一个数字是根节点的值。
"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        length = len(sequence)
        if length == 0:
            return False
        root = sequence[-1]  # 根节点
        i = 0  # 用于记录左子树的结束
        for i in range(length):  # 找到左子树的范围
            if sequence[i] > root:
                break
        # j = i
        for j in range(i, length):  # 找到右子树的范围
            if sequence[j] < root:
                return False

        # 判断左子树是不是二叉搜索树
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])

        # 判断右子树是不是二叉搜索树
        right = True
        if j < length - 1:
            right = self.VerifySquenceOfBST(sequence[j: i - 1: -1])
        return left and right


seq = [5, 7, 6, 9, 11, 10, 8]
# seq = [1,2,3,4,5]
s = Solution().VerifySquenceOfBST(seq)
print(s)
