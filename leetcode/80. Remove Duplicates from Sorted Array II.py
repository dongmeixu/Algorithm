class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # res = []
        # for tmp in nums:
        #     if tmp not in res:
        #         res.append(tmp)
        #     elif res.count(tmp) < 2:
        #         res.append(tmp)
        # for i in range(len(res)):
        #     nums[i] = res[i]
        # return nums[: len(res)]
        i = 0
        count = 1
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                if count < 3:
                    i += 1
                    count += 1
            else:
                if count < 3:
                    count = 1
                    i += 1
                else:
                    nums[i] = nums[j]
                    i += 1
                    count = 1
        return i


class Solution_1:
    def removeDuplicates(self, nums):
        if not nums:
            return []

        if len(nums) < 2:
            return nums

        index = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[index - 2]:
                nums[index] = nums[i]
                index += 1
        return index - 1


# nums = [1, 1, 2, 2, 2, 3, 3]
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(Solution().removeDuplicates(nums))
print(Solution_1().removeDuplicates(nums))
