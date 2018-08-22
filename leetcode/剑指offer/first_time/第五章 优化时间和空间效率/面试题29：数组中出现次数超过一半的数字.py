"""
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

"""


# -*- coding:utf-8 -*-
class Solution:
    global g_bInputInvalid
    g_bInputInvalid = True

    def partition(self, arr, low, high):
        if not arr or low < 0 or high > len(arr):
            return 0

        tmp = arr[low]
        # print(tmp)

        while low < high:
            # 从右往左扫描
            # 从右往左找到第一个比tmp小的数
            while arr[high] > tmp and high > low:
                high -= 1
            # 此时找到了比tmp小的数，将最开始选定的值赋值为high
            arr[low] = arr[high]

            # 从左往右找到第一个比tmp大的数
            while arr[low] <= tmp and high > low:
                low += 1

            # 此时找到了比tmp大的数，将high位置的值用该值替换掉
            arr[high] = arr[low]

        arr[high] = tmp
        return high

    def checkInvalidArray(self, numbers, length):
        g_bInputInvalid = False
        if not numbers and length <= 0:
            g_bInputInvalid = True
        return g_bInputInvalid

    def checkMoreThanHalf(self, numbers, length, result):
        times = 0
        for number in numbers:
            if number == result:
                times += 1
        isMoreThanHalf = True

        if times * 2 <= length:
            # g_bInputInvalid = False
            isMoreThanHalf = False

        return isMoreThanHalf

    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0

        length = len(numbers)

        if self.checkInvalidArray(numbers, length):
            return 0

        start = 0
        end = length - 1
        mid = start + (end - start) // 2

        index = self.partition(numbers, start, end)

        while index != mid:
            if index > mid:
                end = index - 1
                index = self.partition(numbers, start, end)
            else:
                start = index + 1
                index = self.partition(numbers, start, end)

        result = numbers[mid]

        if not self.checkMoreThanHalf(numbers, length, result):
            return 0

        return result

    # 分析：数组中有一个数字出现的次数超过数组长度的一般，
    # 也就是说它出现的次数比其他所有数字出现的次数的和还要多。
    # 因此我们可以考虑在遍历数组的时候保存两个值：一个是数组中的一个数字，一个是次数。
    # 当我们遍历到下一个数字的时候，如果下一个数字和我们之前保存的数字相同，则次数加一；
    # 如果下一个数字和我们之前保存的数字不同，则次数减一。
    # 如果次数为零，我们需要保存下一个数字，并把次数设为1.
    # 由于我们要找的数字出现的次数比其他所有数字出现的次数之和还要多，
    # 那么要找的数字肯定是最后一次把次数设为1时对应的数字
    def MoreThanHalfNum_Solution2(self, numbers):
        length = len(numbers)

        if self.checkInvalidArray(numbers, length):
            return 0

        result = numbers[0]
        times = 1
        for i in range(length):
            if times == 0:
                result = numbers[i]
                times = 1
            elif numbers[i] == result:
                times += 1
            else:
                times -= 1
        if not self.checkMoreThanHalf(numbers, length, result):
            result = 0

        return result


# arr = [1, 2, 2, 2, 2, 3, 4, 1]
arr = [1, 2, 2, 2]
print(Solution().MoreThanHalfNum_Solution(arr))
