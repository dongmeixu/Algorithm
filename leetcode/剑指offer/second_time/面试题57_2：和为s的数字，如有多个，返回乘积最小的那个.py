"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s.
如果有多对数字的和等于s,输出任意一对即可

"""


class Solution:
    def FindNumbersWithSum(self, data, sum):
        res = []
        if not data or not sum or len(data) < 2:
            return res  # 表示没找到

        # 在data[start......end]寻找
        start = 0
        end = len(data) - 1

        while start < end:  # 不能等于，当等于的时候相当于此时两个指针指向的是同一元素
            if data[start] + data[end] == sum:
                res.append([data[start], data[end]])
                start += 1
                end -= 1

            while data[start] + data[end] > sum and start < end:
                end -= 1
                if data[start] + data[end] == sum:
                    res.append([data[start], data[end]])
            start += 1

        if res:
            minF = res[0][0] * res[0][1]
            index = 0
            for i in range(1, len(res)):
                if minF > res[i][0] * res[i][1]:
                    minF = res[i][0] * res[i][1]
                    index = i

            return [res[index][0], res[index][1]]
        else:
            return []


print(Solution().FindNumbersWithSum([1,2,4,7,11,16],10))