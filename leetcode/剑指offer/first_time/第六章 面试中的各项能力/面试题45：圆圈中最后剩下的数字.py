"""

0,1.。。。。n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈里删除第m个数字，求出这个圆圈里剩下的最后一个数字
"""


# -*- coding:utf-8 -*-
class Solution:
    # 解法1：利用循环链表实现，时间复杂度O(mn)
    # def LastRemaining_Solution(self, n, m):
    #     # write code here
    #     if n < 1 or m < 1:
    #         return -1
    #
    #     numbers = []
    #     for i in range(n):
    #         numbers.append(i)
    #
    #     current = 0  # 开始的位置
    #
    #     while len(numbers) > 1:  # 只保留最后一个
    #
    #         for i in range(1, m):  # 执行m-1次
    #             # 如果当前位置为这个圆圈的最后一个位置，则更新下一个位置为头部
    #             if current == numbers[-1]:
    #                 # 当current表示数组下标的时候，不能直接比较其是否等于数组长度-1
    #                 # ====》因为后面删除元素是原地删除，所以直接比较会报错的！
    #                 current = numbers[0]
    #             else:  # 否则获取下一个位置的数据
    #                 current = numbers[numbers.index(current) + 1]
    #
    #         # 更新下一次开始的位置
    #         next = current
    #         if next == numbers[-1]:
    #             next = numbers[0]
    #         else:
    #             next = numbers[numbers.index(next) + 1]
    #
    #         # 删除第m个人
    #         numbers.remove(current)
    #
    #         # 更新当前指针
    #         current = next
    #
    #     return current

    def LastRemaining_Solution(self, n, m):
        # 递推公式，由于编号是从0开始的，那么我们可以令
        # f[1] = 0； // 当一个人的时候，出队人员编号为0
        # f[n] = (f[n - 1] + m) % n // m表示每次数到该数的人出列，n表示当前序列的总人数
        # 而我们只需要得到第n次出列的结果即可，那么不需要另外声明数组保存数据，只需要直接一个for循环求得n阶约瑟夫环问题的结果即可
        # 由于往往现实生活中编号是从1 - n，那么我们把最后的结果加1即可。
        res = [0] * n
        for i in range(1, n):
            res[i] = (res[i - 1] + m) % n
        print(res)
        return res[n - 1] + 1


print(Solution().LastRemaining_Solution(5, 2))
