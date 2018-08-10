"""
排列问题：
问题描述：给定一个整型数组，其中的每一个元素都各不相同，
返回这些元素所有排列的可能

例如：[1, 2, 3]
    返回[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


"""
class Solution:
    res = []
    used = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # self.res = []
        if not nums:
            return self.res

        self.used = [False] * len(nums)
        p = []
        self.permute_main(nums, 0, p)
        return self.res

    # p中保存了一个有index个元素的排列
    def permute_main(self, nums, index, p):
        if index == len(nums):
            # print("每次获取到的结果：%s" % p)
            # !!!!!
            # list中的操作是原地操作，在下面的for循环中由于会对p进行pop操作，所以此处的p的值是变的！！！！
            copy = p.copy()
            self.res.append(copy)
            return

        for i in range(len(nums)):
            # 如果该元素没用过就加入p中
            if not self.used[i]:
                p.append(nums[i])
                self.used[i] = True
                self.permute_main(nums, index + 1, p)
                p.pop(-1)
                # print(p)
                self.used[i] = False


# class Solution:
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#
#         def dfs(nums, path, res):
#             for i in range(len(nums)):
#                 dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)
#             if len(nums) == 0:
#                 res.append(path)
#
#         res = []
#         dfs(nums, [], res)
#         return res


num = [1, 2, 1]
print(Solution().permute(num))
