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
        print(nums[:i])
        return i


# nums = [1, 1, 2, 2, 2, 3, 3]
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(Solution().removeDuplicates(nums))
