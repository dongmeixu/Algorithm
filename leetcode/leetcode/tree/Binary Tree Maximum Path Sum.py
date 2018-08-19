"""
Given a binary tree, find the maximum path sum.
The path may start and end at any node in the tree. For example: Given the below binary tree,
1
/ \
2 3
Return 6.
"""
"""
这题很难，路径可以从任意节点开始，到任意节点结束

可以利用“最大连续子序列和”问题的思路。
如果说Array只有一个方向的话，那么BT其实只是左右两个方向而已，我们需要比较两个方向上的值。

不过，Array可以从头到尾遍历，那么BT怎么办呢?
我们可以采用BT最常用的dfs来进行遍历。先算出左右子树的结果L和R,
如果L大于0，那么对后续结果是有利的，我们加上L,如果R大于0， 对后续结果也是有利的，继续加上R
"""
class Solution:
    max_sum = -1
    
    def maxPathSum(self, root):
        self.dfs(root)
        return self.max_sum

    def dfs(self, root):
        if not root:
            return 0
        L = self.dfs(root.left)
        R = self.dfs(root.right)
        sum = root.val
        if L > 0:
            sum += L
        if R < 0:
            sum += R

        self.max_sum = max(self.max_sum, sum)
        return max(R, L) + root.val if max(R, L) > 0 else root.val
