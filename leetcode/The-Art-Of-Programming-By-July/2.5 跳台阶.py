class Solution:
    # def jump(self, n):
    #     if n <= 1:
    #         return n
    #
    #     return self.jump(n - 1) + self.jump(n - 2)
    def jump(self, n):
        res = [0, 1]
        for i in range(2, n + 1):
            res.append(res[i - 1] + res[i - 2])
        return res[-1]


print(Solution().jump(3))
