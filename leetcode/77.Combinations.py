"""
计算1-n中k个数字的组合

"""


# 回溯法-解决组合问题
class Solution:
    res = []

    def combine(self, n, k):
        self.res.clear()
        if n <= 0 or k <= 0 or k > n:
            return self.res
        # 求解C(n, k),当前已经找到的组合存储在c，需要从start开始搜索新元素
        start = 1
        c = []
        self.combine_main(n, k, start, c)
        return self.res

    def combine_main(self, n, k, start, zuhe):
        if len(zuhe) == k:
            tmp = zuhe.copy()
            self.res.append(tmp)
            return
        ### 优化-剪枝###
        # for i in range(start, n + 1):
        for i in range(start, n + 1 - (k - len(zuhe)) + 1):
            zuhe.append(i)
            self.combine_main(n, k, i + 1, zuhe)
            zuhe.pop(-1)
        return


print(Solution().combine(4, 2))
