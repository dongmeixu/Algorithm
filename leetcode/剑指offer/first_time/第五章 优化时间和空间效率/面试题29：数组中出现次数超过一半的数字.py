"""
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

"""


# # -*- coding:utf-8 -*-
# class Solution:
#     global g_bInputInvalid
#     g_bInputInvalid = True
#
#     def partition(self, arr, low, high):
#         if not arr or low < 0 or high > len(arr):
#             return 0
#
#         tmp = arr[low]
#         # print(tmp)
#
#         while low < high:
#             # 从右往左扫描
#             # 从右往左找到第一个比tmp小的数
#             while arr[high] > tmp and high > low:
#                 high -= 1
#             # 此时找到了比tmp小的数，将最开始选定的值赋值为high
#             arr[low] = arr[high]
#
#             # 从左往右找到第一个比tmp大的数
#             while arr[low] <= tmp and high > low:
#                 low += 1
#
#             # 此时找到了比tmp大的数，将high位置的值用该值替换掉
#             arr[high] = arr[low]
#
#         arr[high] = tmp
#         return high
#
#     def checkInvalidArray(self, numbers, length):
#         g_bInputInvalid = False
#         if not numbers and length <= 0:
#             g_bInputInvalid = True
#         return g_bInputInvalid
#
#     def checkMoreThanHalf(self, numbers, length, result):
#         times = 0
#         for number in numbers:
#             if number == result:
#                 times += 1
#         isMoreThanHalf = True
#
#         if times * 2 <= length:
#             # g_bInputInvalid = False
#             isMoreThanHalf = False
#
#         return isMoreThanHalf
#
#     def MoreThanHalfNum_Solution(self, numbers):
#         # write code here
#         if not numbers:
#             return 0
#
#         length = len(numbers)
#
#         if self.checkInvalidArray(numbers, length):
#             return 0
#
#         start = 0
#         end = length - 1
#         mid = start + (end - start) // 2
#
#         index = self.partition(numbers, start, end)
#
#         while index != mid:
#             if index > mid:
#                 end = index - 1
#                 index = self.partition(numbers, start, end)
#             else:
#                 start = index + 1
#                 index = self.partition(numbers, start, end)
#
#         result = numbers[mid]
#
#         if not self.checkMoreThanHalf(numbers, length, result):
#             return 0
#
#         return result
#
#     # 分析：数组中有一个数字出现的次数超过数组长度的一般，
#     # 也就是说它出现的次数比其他所有数字出现的次数的和还要多。
#     # 因此我们可以考虑在遍历数组的时候保存两个值：一个是数组中的一个数字，一个是次数。
#     # 当我们遍历到下一个数字的时候，如果下一个数字和我们之前保存的数字相同，则次数加一；
#     # 如果下一个数字和我们之前保存的数字不同，则次数减一。
#     # 如果次数为零，我们需要保存下一个数字，并把次数设为1.
#     # 由于我们要找的数字出现的次数比其他所有数字出现的次数之和还要多，
#     # 那么要找的数字肯定是最后一次把次数设为1时对应的数字
#     def MoreThanHalfNum_Solution2(self, numbers):
#         length = len(numbers)
#
#         if self.checkInvalidArray(numbers, length):
#             return 0
#
#         result = numbers[0]
#         times = 1
#         for i in range(length):
#             if times == 0:
#                 result = numbers[i]
#                 times = 1
#             elif numbers[i] == result:
#                 times += 1
#             else:
#                 times -= 1
#         if not self.checkMoreThanHalf(numbers, length, result):
#             result = 0
#
#         return result
#

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        # 方法1：基于partition  时间复杂度O（n）
        n = len(numbers)
        if not n:
            return 0
        index = self.partition(numbers, 0, n - 1)

        start = 0
        end = n - 1
        target_index = n // 2
        while index != target_index:
            if index > target_index:
                index = self.partition(numbers, start, target_index - 1)
            else:
                index = self.partition(numbers, target_index + 1, end)

        if self.CheckMoreThanHalf(numbers, numbers[index]):
            return numbers[index]
        else:
            return 0

    def partition(self, numbers, start, end):
        if not numbers or start < 0 or end > len(numbers):
            return 0
        pivot = numbers[start + (end - start) // 2]

        while start < end:
            while start < end and numbers[end] > pivot:
                end -= 1
            numbers[start] = numbers[end]

            while start < end and numbers[start] < pivot:
                start += 1
            numbers[end] = numbers[start]

        numbers[end] = pivot
        return end

    def CheckMoreThanHalf(self, numbers, target):
        if not numbers:
            return False

        count = 0
        for tmp in numbers:
            if tmp == target:
                count += 1
        if count > len(numbers) // 2:
            return True
        else:
            return False


class Solution1:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        res = numbers[0]
        times = 1

        # 遍历数组
        for i in range(1, len(numbers)):
            if times == 0:
                res = numbers[i]
                times = 1
            elif res == numbers[i]:
                times += 1
            else:
                times -= 1

        if self.CheckMoreThanHalf(numbers, res):
            return res
        else:
            return 0

    def CheckMoreThanHalf(self, numbers, target):
        if not numbers:
            return False

        n = len(numbers)

        count = 0
        for tmp in numbers:
            if tmp == target:
                count += 1
        if n & 1 == 1: # 奇数
            return count >= n // 2
        else:
            return count > n // 2


# arr = [4, 2, 4, 1, 4, 2]
arr = [1, 2, 2, 2]
print(Solution1().MoreThanHalfNum_Solution(arr))
