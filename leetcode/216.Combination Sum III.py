"""
在 1-9这9个数字中，选出k个数字，每个数字只能使用一次，使得其和为n

-如 n=7, k=3, 结果为：[[1, 2, 4]]
-如 n=9, k=3,结果为：[[1, 2, 6], [1, 3, 5], [2, 3, 4]]
"""


class Solution:
    res = []
    used = []

    def s(self, n, k):
        self.res.clear()
        self.used = [False] * 9

        if k <= 0 or n <= 0:
            return self.res

        self.main(n, k, 1, [])
        return self.res

    def main(self, n, k, index, sum):
        if index == k + 1:
            copy = sum[:]
            copy.sort()
            if n == 0 and copy not in self.res:
                self.res.append(copy)
            return
        for i in range(index, n + 1 - (k - len(sum)) + 1):
            if not self.used[i - 1]:
                sum.append(i)
                self.used[i - 1] = True
                self.main(n - i, k, index + 1, sum)
                sum.pop()
                self.used[i - 1] = False
        return


n = 9
k = 3
print(Solution().s(n, k))
