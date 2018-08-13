"""

题目描述
输入两个整数 n 和 m，从数列1，2，3.......n 中随意取几个数,使其和等于 m ,要求将其中所有的可能组合列出来

输入描述:
每个测试输入包含2个整数,n和m

输出描述:
按每个组合的字典序排列输出,每行输出一种组合

示例1

输入
5 5

输出
1 4
2 3
5

"""


class Solution:
    res = []
    used = []

    def combinationSum(self, candidates, target):
        if not candidates:
            return self.res

        self.used = [False] * len(candidates)
        self.dfs(candidates, target, 0, [])
        for res in self.res:
            ss = ""
            for i in res:
                ss = ss + str(i) + " "
            print(ss.strip())
        # return self.res

    def dfs(self, candidates, target, index, tmp):
        if target == 0:
            t = sorted(tmp[:])
            if t not in self.res:
                self.res.append(tmp[:])
            return

        if target < 0:
            return

        for i in range(index, len(candidates)):
            if not self.used[i]:
                tmp.append(candidates[i])
                self.used[i] = True
                self.dfs(candidates, target - candidates[i], index + 1, tmp)
                tmp.pop()
                self.used[i] = False
        return

N, M = input().split()
nums = list(range(1, int(N) + 1))
T = int(M)
Solution().combinationSum(nums, T)

