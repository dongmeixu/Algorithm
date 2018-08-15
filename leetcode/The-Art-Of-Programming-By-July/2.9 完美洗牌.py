"""
完美洗牌算法
题目详情
有个长度为2n的数组{a1,a2,a3,...,an,b1,b2,b3,...,bn}，希望排序后{a1,b1,a2,b2,....,an,bn}，请考虑有无时间复杂度o(n)，空间复杂度0(1)的解法。
题目来源：此题是去年2013年UC的校招笔试题，看似简单，按照题目所要排序后的字符串蛮力变化即可，但若要完美的达到题目所要求的时空复杂度，则需要我们花费不小的精力。OK，请看下文详解，一步步优化。

"""


class Solution:
    # 方法1：借助辅助数组  时间复杂度O(n), 空间复杂度O(n)
    def sovle_1(self, arr):
        res = []
        if not arr:
            return res

        mid = len(arr) >> 1
        for i in range(mid):
            res.append(arr[i])
            res.append(arr[i + mid])
        return res

    # 蛮力 中间交换
    def sovle_2(self, arr):
        res = []
        if not arr:
            return res

        # mid = len(arr) >> 1
        # print(mid)
        # index = mid
        # for i in range(mid, len(arr) - 1):
        #     tmp = arr[index]
        #     arr[index] = arr[index - 1]
        #     arr[index - 1] = tmp
        #     index += 1
        #
        # for i in range(mid, -1, -1):
        #     tmp = arr[i]
        #     arr[i] = arr[i - 1]
        #     arr[i - 1] = tmp
        # return arr


print(Solution().sovle_1(["a1", "a2", "a3", "a4", "b1", "b2", "b3", "b4"]))
# print(Solution().sovle_2(["a1", "a2", "a3", "a4", "b1", "b2", "b3", "b4"]))
