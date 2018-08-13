# -*- coding:utf-8 -*-
class Solution:
    # 按照快排的思路，设置两个指针，这样得到的元素间的相对位置发生了改变
    # def reOrderArray(self, array):
    #     # write code here
    #     if not array:
    #         return
    #
    #     left = 0
    #     right = len(array) - 1
    #     while left <= right:
    #         while left <= right and not self.operator(array[left]):
    #             left += 1
    #         while left <= right and self.operator(array[right]):
    #             right -= 1
    #         # 此时从前往后找到了一个偶数， 从后往前找到了一个奇数，交换
    #         if left <= right:
    #             tmp = array[left]
    #             array[left] = array[right]
    #             array[right] = tmp
    #     return array

    def reOrderArray(self, array):
        newArray = []
        if not array:
            return newArray

        for tmp in array:
            if not self.operator(tmp):
                newArray.append(tmp)

        for tmp in array:
            if self.operator(tmp):
                newArray.append(tmp)
        return newArray

    def operator(self, num):
        if num & 1 == 0:  # 偶数
            return True
        else:
            return False


# array = [1, 2, 3, 4, 5]
array = [1, 2, 3, 4, 5, 6, 7]
print(Solution().reOrderArray(array))
array = [1, 2, 3, 4, 5, 6, 7]
print(Solution().reOrderArray(array))
