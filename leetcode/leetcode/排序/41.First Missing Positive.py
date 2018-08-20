"""

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""


class Solution:
    # 时间复杂度O(nlogn) 排序，遍历数组，如果数组元素不等于其下标且元素值大于0，返回下标,不行！！！！！！！！！！！
    # def firstMissingPositive(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if not nums:
    #         return -1
    #     nums.sort()
    #
    #     for i, tmp in enumerate(nums):
    #         if tmp != (i + 1) and tmp > 0:
    #             return i + 1
    #     return -1
    #

    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        self.bucket_sort(nums)
        for i in range(len(nums)):
            if nums[i] != (i + 1):
                return i + 1
        return len(nums) + 1

    def bucket_sort(self, nums):
        for i in range(len(nums)):
            if 0 < nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                # 交换
                tmp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp
                i -= 1
        # return nums


# nums = [7, 8, 9, 11, 12]
nums = [0, 2, 4, -1]
print(Solution().firstMissingPositive(nums))
