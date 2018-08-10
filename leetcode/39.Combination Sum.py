"""
给出一个集合，其中所有的元素各不相同，以及一个数字T.
寻找所有该集合中的元素集合，使得组合中所有的元素和为T
(注意：集合中每一个元素可以使用多次)

example: nums=[2, 3, 6, 7], T = 7

        returns=[[7], [2, 2, 3]]
"""


class Solution:
    res = []

    def combinationSum(self, candidates, target):
        if not candidates:
            return self.res

        self.dfs(candidates, target, 0, [])
        return self.res

    def dfs(self, candidates, target, index, tmp):
        if target == 0:
            self.res.append(tmp[:])
            return

        if target < 0:
            return

        for i in range(len(candidates)):
            tmp.append(candidates[i])
            self.dfs(candidates, target - candidates[i], index + 1, tmp)
            tmp.pop()
        return


nums = [2, 3, 6, 7]
T = 7
print(Solution().combinationSum(nums, T))
