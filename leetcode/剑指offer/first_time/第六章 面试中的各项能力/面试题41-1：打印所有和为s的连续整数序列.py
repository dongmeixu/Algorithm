"""
输入一个正数s,打印出所有和为s的连续正数序列（至少含有2个数）
例如输入15由于1+2+3+4+5=4+5+6=7+8=15，
所以结果打印出3个连续序列1-5、4-6、7-8
"""


class Solution:
    def FindContinuousSequence(self, sum):
        if sum <= 2:  # 和为2以下，则找不到至少2个数
            return []

        small = 1
        big = 2
        mid = (1 + sum) // 2
        curSum = small + big

        res = []

        while small < mid:
            if curSum == sum:
                res.append(self.PrintContinuousSequence(small, big))

            while curSum > sum and small < mid:
                curSum -= small
                small += 1
                if curSum == sum:
                    res.append(self.PrintContinuousSequence(small, big))

            big += 1
            curSum += big
        return res

    def PrintContinuousSequence(self, small, big):
        return [x for x in range(small, big + 1)]


print(Solution().FindContinuousSequence(15))
