class Solution:
    res = []

    def ManySum(self, n, sum):
        if n == 0 or sum == 0:
            return

        list = [i for i in range(1, n + 1)]

        self.ManySum_main(list, 0, sum, [])
        return self.res

    def ManySum_main(self, arr, index, sum, p):
        if sum == 0:
            self.res.append(p[:])
            return

        for i in range(index, len(arr)):
            p.append(arr[i])
            self.ManySum_main(arr, index + 1, sum - arr[i], p)
            p.pop()


n = 4
sum = 3
print(Solution().ManySum(n, sum))
