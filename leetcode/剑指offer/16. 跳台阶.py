# -*- coding:utf-8 -*-


"""

题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

"""

class Solution:
    # 1.溢出了
    # def jumpFloor(self, number):
    #     # write code here
    #     if number <= 2:
    #         return number
    #     return self.jumpFloor(number - 1) + self.jumpFloor(number - 2)

    # def jumpFloor(self, number):
    #     # write code here
    #     if number <= 3:
    #         return number
    #     result = [1, 2, 3]
    #     for i in range(4, number + 1):
    #         result.append(result[-1] + result[-2])
    #     return result[-1]

    def jumpFloor(self, number):
        # write code here
        result = [0, 1, 2]
        while len(result) <= number:
            result.append(result[-1] + result[-2])
        return result[number]


Solution = Solution().jumpFloor(8)
print(Solution)