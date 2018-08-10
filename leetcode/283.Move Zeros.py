"""

给定一个数组nums,写一个函数，将数组中所有的0
挪到数组的末尾，而维持其他所有非0元素的相对位置
nums = [0, 1, 0, 3, 12]  ======> 返回 [1, 3, 12, 0, 0]
"""
"""
思路：
    1. 遍历下整个数组，将所有非零元素都拿出来，有几个非零元素就将原数组相应的位置赋值，剩下的位置补零 =====》 时间复杂度O(n)  空间复杂度O(n)
    2. 双指针（直接覆盖） =====》 时间复杂度O(n)  空间复杂度O(1)
    3. 双指针（将非零元素与零元素交换位置）


"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 解法1：暴力解法  时间复杂度O(n), 空间复杂度O(n)
        # nonZeroElements = []
        # for i in nums:
        #     if i:
        #         nonZeroElements.append(i)
        #
        # for i, tmp in enumerate(nonZeroElements):
        #     nums[i] = tmp
        #
        # for i in range(len(nonZeroElements), len(nums)):
        #     nums[i] = 0

        # # 解法2：双指针
        # k = 0   # [0....k)中保存所有当前遍历过的非0元素
        # # 遍历到第i个元素后，保证[0.....i]中所有非0元素都按照顺序排列在[0....k)中
        # for i in range(len(nums)):
        #     if nums[i]:
        #         nums[k] = nums[i]
        #         k += 1
        # for j in range(k, len(nums)):
        #     nums[j] = 0

        # 解法3：将非0元素跟0元素交换位置
        k = 0   # [0....k)中保存所有当前遍历过的非0元素
        # 遍历到第i个元素后，保证[0.....i]中所有非0元素到按照顺序排列在[0......k)中，
        # 同时， [k......i]为0
        for i in range(len(nums)):
            if nums[i]:
                if i != k:  # 交换
                    tmp = nums[k]
                    nums[k] = nums[i]
                    nums[i] = tmp
                    k += 1
                else:
                    k += 1
        return nums


nums = [0, 1, 0, 3, 12]
print(Solution().moveZeroes(nums))
