"""
描述：给定一个有序数组，对数组中的元素去重，使得原数组的每个元素只有1个。返回去重后数组的长度值
思路1：利用辅助数组存储不重复的值
思路2：设置2个指针，

"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 解法1：遍历原数组，将原数组中的元素赋值到新数组，复制的时候如果新数组中存在该元素则跳过
        # res = []
        # for tmp in nums:
        #     if tmp not in res:
        #         res.append(tmp)
        #
        # for i in range(len(res)):
        #     nums[i] = res[i]
        # return len(nums[:len(res)])

        # 解法2：
        # 设置2个指针，i:用于指定不重复元素应该在的位置；j遍历数组找到不重复元素的原始位置
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1


nums = [1, 1, 2]
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(Solution().removeDuplicates(nums))
