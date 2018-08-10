"""

描述：给定一个有n个元素的数组，数组中元素的取值只有0， 1， 2三种可能。为这个数组排序

"""
"""
思路1：分别统计0,1,2元素的个数，然后再赋值给原数组（计数排序）
"""

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # num_1 = 0
        # num_2 = 0
        # num_3 = 0
        # for num in nums:
        #     print(num)
        #     if num == 0:
        #         num_1 += 1
        #     elif num == 1:
        #         num_2 += 1
        #     elif num == 2:
        #         num_3 += 1
        # for i in range(num_1):
        #     nums[i] = 0
        # for i in range(num_1, num_1 + num_2):
        #     nums[i] = 1
        # for i in range(num_1 + num_2, (num_1 + num_2 + num_3)):
        #     nums[i] = 2
        # return nums

        """"
        三路快排
        时间复杂度O(n)
        空间复杂度O(1)
        """
        zero = -1  # 不能是0，当为-1时，初始化时就是个无效数组
        #  nums[0....zero]  == 0
        two = len(nums)  # nums[two.....n-1] == 2

        i = 0
        while i < two:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                tmp = nums[i]
                two -= 1
                nums[i] = nums[two]
                nums[two] = tmp
            else:
                zero += 1

                tmp = nums[zero]
                nums[zero] = nums[i]
                nums[i] = tmp
                i += 1
            return nums


# nums = [2, 2, 0, 1, 2, 0, 2, 0]
nums = [2, 0, 2, 1, 1, 0]
print(Solution().sortColors(nums))
