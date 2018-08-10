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




"""
[编程题] 矩形重叠
时间限制：1秒
空间限制：32768K
平面内有n个矩形, 第i个矩形的左下角坐标为(x1[i], y1[i]), 右上角坐标为(x2[i], y2[i])。
如果两个或者多个矩形有公共区域则认为它们是相互重叠的(不考虑边界和角落)。
请你计算出平面内重叠矩形数量最多的地方,有多少个矩形相互重叠。

输入描述:
输入包括五行。
第一行包括一个整数n(2 <= n <= 50), 表示矩形的个数。
第二行包括n个整数x1[i](-10^9 <= x1[i] <= 10^9),表示左下角的横坐标。
第三行包括n个整数y1[i](-10^9 <= y1[i] <= 10^9),表示左下角的纵坐标。
第四行包括n个整数x2[i](-10^9 <= x2[i] <= 10^9),表示右上角的横坐标。
第五行包括n个整数y2[i](-10^9 <= y2[i] <= 10^9),表示右上角的纵坐标。


"""