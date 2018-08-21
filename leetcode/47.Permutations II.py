"""
给定一个整型数组，其中可能有相同的元素，
返回这些元素所有排列的可能

[1, 1, 2]
返回[[1, 1, 2], [1, 2, 1], [2, 1, 1]]

"""


class Solution:
    res = []
    used = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return self.res

        self.used = [False] * len(nums)
        self.permute_main(nums, 0, [])
        return self.res

    def permute_main(self, nums, index, p):
        if index == len(nums):
            # TODO:这块还有其他办法嘛？
            if p not in self.res:
                self.res.append(p[:])
            return

        for i in range(len(nums)):

            # 如果该元素没用过就加入p中
            if not self.used[i]:
                p.append(nums[i])
                self.used[i] = True
                self.permute_main(nums, index + 1, p)
                p.pop(-1)
                # print(p)
                self.used[i] = False


nums = [1, 2, 1]
print(Solution().permute(nums))
