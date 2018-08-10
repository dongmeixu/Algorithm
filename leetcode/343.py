class Solution:
    # # 将n进行分割（至少分割两部分）， 可以获得的最大乘积
    # def breakInteger(self, n):
    #     if n == 1:
    #         return 1
    #     res = -1
    #     for i in range(1, n):
    #         # i * (n-i)
    #         res = max(res, i * (n - i), i * self.breakInteger(n - i))
    #     return res
    #
    # def integerBreak(self, n):
    #     return self.breakInteger(n)

    # 记忆性搜索
    # memo = []
    #
    # # 将n进行分割（至少分割两部分）， 可以获得的最大乘积
    # def breakInteger(self, n):
    #     if n == 1:
    #         return 1
    #
    #     if self.memo[n] != -1:
    #         return self.memo[n]
    #
    #     res = -1
    #     for i in range(1, n):
    #         # i + (n-i)
    #         res = max(res, i * (n - i), i * self.breakInteger(n - i))
    #     self.memo[n] = res
    #     return res
    #
    # def integerBreak(self, n):
    #     self.memo = [-1] * (n + 1)
    #     return self.breakInteger(n)

    # 动态规划
    def integerBreak(self, n):
        memo = [-1] * (n + 1)
        memo[1] = 1

        for i in range(2, n + 1):
            # 求解memo[i]
            for j in range(1, i):
                # j + (i - j)
                memo[i] = max(memo[i], j * (i - j), j *memo[i - j])
        return memo[n]


n = 6
print(Solution().integerBreak(n))