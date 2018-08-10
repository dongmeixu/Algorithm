"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s.
如果有多对数字的和等于s,输出任意一对即可

"""


class Solution:
    def FindNumbersWithSUm(self, data, sum):
        if not data:
            return -1  # 表示没找到

        # 在data[start......end]寻找
        start = 0
        end = len(data) - 1
        
        while start <= end:
            if data[start] + data[end] == sum:
                return [data[start], data[end]]
            elif data[start] + data[end] > sum:
                end -= 1
            else:
                start += 1
        return -1  # 遍历完都没找到


print(Solution().FindNumbersWithSUm([1, 2, 4, 7, 8, 11, 15], 15))
