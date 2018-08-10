"""
题目描述：给定一个数组nums和一个数值val，将数组中所有等于val的元素删除，并返回剩余的元素个数？


- 如何定义删除？从数组中去除？还是放在数组末尾？
- 剩余元素的排列是否要保证原有的相对顺序？
- 是否有空间复杂度的要求？O(1)

"""
"""
思路：类似283！！！！
"""


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #  暴力解法
        # new_arr = []
        # for ele in nums:
        #     if ele != val:
        #         new_arr.append(ele)
        # for i in range(len(new_arr)):
        #     nums[i] = new_arr[i]
        # return len(nums[:len(new_arr)])

        # 解法2
        k = 0  # 表示在原数组中，[0....k)范围内的非指定元素的其他元素
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return len(nums[:k])

        # left = 0
        # right = len(val) - 1  # 在val[0.....n-1]范围内寻找
        #
        # while left < right:  # 类似快排：从左向右找到第一个等于待删除的元素；从右往左找到第一个不等于待删除的元素，交换
        #     if val[left] == nums and val[right] != nums:
        #         tmp = val[left]
        #         val[right] = val[left]
        #         val[left] = tmp
        #
        #     if val[left] != nums:
        #         left += 1
        #     if val[right] == nums:
        #         right -= 1


val = 1
nums = [0, 1, 2, 2, 3, 0, 4, 2]
# nums = [3, 2, 2, 3]
print(Solution().removeElement(nums, val))
