"""
有序数组==》首先想到是不是可以用二分查找法  时间复杂度为O(logn)
"""


class Solution:
    def binartSearch(self, nums, target):
        # 如果数组为空，则直接返回-1
        if not nums:
            return -1

        # 查找的初始位置
        left = 0
        right = len(nums) - 1
        """
        如果right=len(nums),即在nums[left.....right)范围内查找，则以下这两处需要修改：
        1.循环条件：while left < right
        2.循环内部：right = mid
        """

        # 循环不变量：在nums[left......right]范围内查找
        while left <= right:
            mid = left + (right - left) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


print(Solution().binartSearch([i for i in range(10 ** 3)], 2))

