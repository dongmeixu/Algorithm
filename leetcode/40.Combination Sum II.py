"""
给出一个集合，其中元素可能相同，以及一个数字T.
寻找所有该集合中的元素组合，使得组合中所有的元素和为T
(注意：集合中每一个元素只可以使用一次)

-如给定集合 nums = [10, 1, 2, 7, 6, 1, 5], T = 8
-返回[[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]
"""


class Solution:
    res = []

    def combinationSum(self, candidates, target):
        if not candidates or not target:
            return self.res

        self.dfs(candidates, 0, target, [])
        return self.res

    def dfs(self, candidates, index, target, tmp):
        if target == 0:
            self.res.append(tmp[:])
            return

        if target < 0:
            return

        for i in range(index, len(candidates)):
            tmp.append(candidates[i])
            self.dfs(candidates[i + 1:], index + 1, target - candidates[i], tmp)
            tmp.pop()


nums = [10, 1, 2, 7, 6, 1, 5]
T = 8
print(Solution().combinationSum(nums, T))
