"""
题目描述
统计一个数字在排序数组中出现的次数。
"""
"""二分查找----查找第一个k,查找最后一个k"""

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0

        length = len(data)
        start = 0
        end = length - 1

        number = 0

        firstIndex = self.GetFirstK(data, k, start, end)
        lastIndex = self.GetLastK(data, length, k, start, end)

        if firstIndex > -1 and lastIndex > -1:
            number = lastIndex - firstIndex + 1
        return number

    def GetFirstK(self, data, k, start, end):
        if start > end:
            return -1
        mid = start + (end - start) // 2
        if data[mid] == k:  # 中间元素等于k,接下来判断是不是第一个k
            if (mid > 0 and data[mid - 1] != k) or mid == 0:
                return mid
            else:
                end = mid - 1
        elif data[mid] > k:
            end = mid - 1
        else:
            start = mid + 1

        return self.GetFirstK(data, k, start, end)

    def GetLastK(self, data, length, k, start, end):
        if start > end:
            return -1
        mid = start + (end - start) // 2
        if data[mid] == k:  # 中间元素等于k,接下来判断是不是第一个k
            if (mid < length - 1 and data[mid + 1] != k) or mid == length - 1:
                return mid
            else:
                start = mid + 1
        elif data[mid] > k:
            end = mid - 1
        else:
            start = mid + 1

        return self.GetLastK(data, length, k, start, end)


arr = [3, 3, 3, 3, 4, 5]
print(Solution().GetNumberOfK(arr, 3))
