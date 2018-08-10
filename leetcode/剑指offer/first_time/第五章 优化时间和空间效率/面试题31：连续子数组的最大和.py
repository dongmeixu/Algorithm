"""
题目描述
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
今天测试组开完会后,他又发话了:在古老的一维模式识别中,
常常需要计算连续子向量的最大和,当
向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,
并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
你会不会被他忽悠住？(子向量的长度至少是1)
"""

"""
动态规划：
    用函数f(i)表示以第i个数字结尾的子数组的最大和，那么我们需要求出max[f(i)] 0<=i<=n
            pData[i]                i = 0 or f(i - 1) <= 0
    f(i) = 
            f(i - 1) + pData[i]     i!=0 and f(i - 1) > 0
            
    公式的意义：当以第i-1个数字结尾的子数组中所有数字的和小于0时，
    1. 如果把这个负数与第i个数累加，得到的结果比第i数字本身还要小，
        所以这种情况下以第i数字结尾的子数组就是第i个数字本身
    2. 如果以第i-1个数字结尾的子数组中所有数字的和大于0，
        与第i数字累加就得到以第i个数字结尾的子数组中所有数字的和。


"""

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        ret = -1  # 最大值
        sum = 0  # 和
        for item in array:
            if sum <= 0:
                sum = item
            else:
                sum += item
            ret = ret if ret > sum else sum  # 更新最大值

        return ret


# arr = [6, -3, -2, 7, -15, 1, 2, 2]
arr = [1, -2, 3, 10, -4, 7, 2, -5]
print(Solution().FindGreatestSumOfSubArray(arr))
