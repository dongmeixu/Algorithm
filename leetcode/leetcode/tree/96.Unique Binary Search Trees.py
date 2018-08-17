"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# PASS
# 一阶动态规划  时间复杂度O(n^2),空间复杂度O(n)
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 0:
            return

        res = [1, 1]
        for i in range(2, n + 1):
            tmp = 0
            for k in range(1, i + 1):
                tmp += res[k - 1] * res[i - k]
            res.append(tmp)
        return res[-1]


print(Solution().numTrees(3))
