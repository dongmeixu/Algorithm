"""
在一个整型序列中寻找第k大的元素
-如给定数组[3, 2, 1, 5, 6, 4], k = 2，结果为5

利用快排partition中，将pivot放置在其正确的位置上的性质
"""


class Solution:
    def getKLagestEle(self, nums, k):
        if not nums or k > len(nums) or k <= 0:
            return -1
        if k == len(nums):
            return nums[0]

        start = 0
        end = len(nums) - 1
        index = self.partition(nums, start, end)

        while index != len(nums) - k:
            if index > k:
                index = self.partition(nums, start, index - 1)
            else:
                index = self.partition(nums, index + 1, end)
        return nums[index]

    def partition(self, nums, start, end):
        pivot = nums[start]
        while start <= end:
            while start <= end and nums[end] >= pivot:
                end -= 1
            nums[start] = nums[end]

            while start <= end and nums[start] <= pivot:
                start += 1
            nums[end] = nums[start]
        nums[start] = pivot
        return start


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(Solution().getKLagestEle(nums, k))
