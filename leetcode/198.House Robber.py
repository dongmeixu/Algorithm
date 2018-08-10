class Solution:
    # 方式1：递归
    # # 考虑抢劫nums[index.....nums.size()]这个范围的所有房子
    # def tryRob(self, nums, index):
    #     if index == len(nums):
    #         return 0
    #     res = 0
    #     for i in range(index, len(nums)):
    #         res = max(res, nums[i] + self.tryRob(i + 2))
    #
    #     return res
    #
    # def rob(self, nums):
    #     if not nums:
    #         return 0
    #     return self.tryRob(nums, 0)

    # 方式2：记忆化搜索
    # 定义一个数组，用于保存已经算过的结果
    memo = []

    def tryRob(self, nums, index):
        if index >= len(nums):
            return 0
        if self.memo[index] != -1:
            return self.memo[index]

        res = 0
        for i in range(index, len(nums)):
            res = max(res, nums[i] + self.tryRob(i + 2))
        self.memo[index] = res
        return res

    def rob(self, nums):
        self.memo = [-1] * len(nums)
        if not nums:
            return 0
        return self.tryRob(nums, 0)

    # 方式3：DP
    def rob(self, nums):
        n = len(nums)

        if n == 0:
            return 0

        memo = [-1] * n
        memo[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            for j in range(i, n):
                if j + 2 < n:
                    tmp = memo[j + 2]
                else:
                    tmp = 0
                memo[i] = max(memo[i], nums[j] + tmp)
        return memo[0]
