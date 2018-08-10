"""
题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3, 4, 5, 1, 2}为{1, 2, 3, 4, 5}的一个旋转，该数组的最小值为1
"""

"""
分析：
    观察旋转数组：它本身是个部分有序的数组，前部分+后部分都是递增的，
    而且前面最小的元素大于等于后面最大的元素
    1.初始化：指针left，right分别指向数组中的第一个元素和最后一个元素
    2.当arr[left] >= arr[right]时，mid = left + (right - left) / 2,
        if arr[mid] >= arr[left], 更新left = mid(left指针总是指向第一个递增数组)
        if arr[mid] < arr[right], 更新right = mid(right总是指向第二个递增数组)
        if right - left == 1，循环结束的条件
     当arr[left] <= arr[right]时,return arr[0]
    3.第一个指针总是指向前面递增数组的元素，而第二个指针总是指向后面递增数组的元素。
    最终第一个指针将指向前面子数组的最后一个元素，而第二个指针会指向后面子数组的第一个元素。
    也就是说它们最终会指向指向两个相邻的元素，而第二个指针指向的刚好是最小的元素。
    
    
    会存在一个问题：就是当arr[left] == arr[mid] == arr[right] 智能顺序查找了
    比如数组{0,1,1,1,1} 它的旋转数组为{1,0,1,1,1}，{1,1,1,0,1}
"""


# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0

        left = 0
        right = len(rotateArray) - 1
        indexReturn = left

        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:
                indexReturn = right
                break
            mid = left + (right - left) // 2
            # 当三个指针指向的元素值相等的时候，只能顺序查找了
            if rotateArray[left] == rotateArray[mid] == rotateArray[right]:
                return self.findMinByOrder(rotateArray, left, right)

            if rotateArray[mid] >= rotateArray[left]:
                left = mid

            else:
                right = mid

        return rotateArray[indexReturn]

    def findMinByOrder(self, arr, left, right):
        min = arr[left]
        for i in range(left, right + 1):
            if arr[i] < min:
                min = arr[i]
        return min


# arr = [3, 4, 5, 1, 2]
arr = [1, 0, 1, 1, 1]
s = Solution().minNumberInRotateArray(arr)
print(s)
