"""

You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

"""

"""
从最后一个房子抢劫，若抢则获得该房屋的钱同时不能抢n-1这个房子了
"""

# 1. 设计暴力搜索算法，找到冗余------->超时
# class Solution:
#     def rob(self, nums):
#         """
#         :type nums: List[int] 非负
#         :rtype: int
#         """
#         return self.sovle(len(nums) - 1, nums)
#
#     def sovle(self, idx, nums):
#         if idx < 0:
#             return 0
#
#         return max(nums[idx] + self.sovle(idx - 2, nums), self.sovle(idx - 1, nums))


# # 2. 设计并存储状态（一维，二维，三维数组，甚至用map）
# class Solution:
#     result = [] # 用于保存状态
#
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         self.result = [-1] * len(nums)  # 初始化
#         return self.sovle(len(nums) - 1, nums)
#
#     def sovle(self, idx, nums):
#         if idx < 0:
#             return 0
#
#         if self.result[idx] >= 0:
#             return self.result[idx]
#
#         self.result[idx] = max(nums[idx] + self.sovle(idx - 2, nums), self.sovle(idx - 1, nums))
#         return self.result[idx]


# 4. 自底向上计算最优解（编程方式）
class Solution:

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        result = [nums[0], max(nums[0], nums[1])]

        for idx in range(2, len(nums)):
            result.append(max(nums[idx] + result[idx - 2], result[idx - 1]))
        print(result)
        return result[len(nums) - 1]


list = [1, 2, 3, 4]

s = Solution().rob(list)
print(s)