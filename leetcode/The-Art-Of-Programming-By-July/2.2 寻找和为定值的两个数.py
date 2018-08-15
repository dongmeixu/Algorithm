class Solution:
    res = []
    used = []

    def TwoSum(self, arr, sum):
        if not arr or sum <= 0:
            return

        self.used = [False] * len(arr)
        self.TwoSum_main(arr, 0, sum, [])
        return self.res

    def TwoSum_main(self, arr, index, sum, p):
        if sum == 0 and len(p) == 2:
            self.res.append(p[:])
            return

        for i in range(index, len(arr) - len(p) - 1):
            # p.append(arr[i])
            # self.TwoSum_main(arr, index + 1, sum - arr[i], p)
            # p.pop()
            if not self.used[i]:
                p.append(arr[i])
                self.used[i] = True
                self.TwoSum_main(arr, index + 1, sum - arr[i], p)
                p.pop()
                self.used[i] = False


arr = [1, 2, 4, 7, 11, 15]
target = 3
print(Solution().TwoSum(arr, target))
