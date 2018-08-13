"""
题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3, 4, 5, 1, 2}为{1, 2, 3, 4, 5}的一个旋转，该数组的最小值为1
"""


# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0

        left = 0
        right = len(rotateArray) - 1
        returnPos = left

        # 当不满足while条件的时候，说明，第一个元素就是最小值
        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:  # 循环结束条件
                returnPos = right
                break

            mid = left + (right - left) // 2
            # 特殊情况，如果left, mid, right均相等，则只能顺序遍历了
            if rotateArray[left] == rotateArray[mid] == rotateArray[right]:
                return self.FindMinByOrder(rotateArray, left, right)

            if rotateArray[mid] >= rotateArray[left]:
                left = mid  # left指向前部分的最大值
            else:
                right = mid  # right指向后部分的最小值

        return rotateArray[returnPos]

    def FindMinByOrder(self, array, left, right):
        min = array[left]
        for i in range(left, right + 1):
            if array[i] < min:
                min = array[i]

        return min


print(Solution().minNumberInRotateArray([]))
print(Solution().minNumberInRotateArray([1, 2, 1, 1, 1]))
