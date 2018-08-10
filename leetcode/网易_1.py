"""

题目描述：牛牛总是睡过头，所以他定了很多闹钟，只有在闹钟响的时候他才会醒过来并决定起不起床。
从他起床算起他需要X分钟到达教室，上课时间为当天的A时B分，请问他最晚可以什么时间起床。

输入描述：
每个输入包含一个测试用例
每个测试用例的第一行包含一个正整数，表示闹钟的数量N(N<=100)
接下来的N行每行包含2个整数，表示这个闹钟响起的时间为Hi(0<=A<4)时Mi(0<=B<60)分

接下来的一行包含一个整数，表示从起床算起他需要X(0<=X<=100)分钟到达教室

接下来一行包含两个整数，表示上课时间为A(0<=A<24)时B(0<=B<60)分
数据保证至少有一个闹钟可以让牛牛及时到达教室

输出描述
输出2个整数表示牛牛最晚起床时间

示例
输入
3
5 0
6 0
7 0
59
6 59

输出
6 0


"""
#
# N = int(input())  # 总的闹钟数
# alarm_times = []
# for _ in range(N):
#     h, m = list(map(int, input().split()))  # 定的闹钟
#     alarm_times.append(h * 60 + m)
# print(alarm_times)
#
# X = int(input())  # 多久能走到教室
#
# A, B = list(map(int, input().split()))
# class_time = A * 60 + B  # 上课时间
#
# alarm_times.sort()  # 升序排列
# print(alarm_times)
#
# """
# >>> s = 'abcdefgh'
# >>> s[::-1]   # 可以视为翻转操作
# 'hgfedcba'
# >>> s[::2]   # 隔一个取一个元素的操作
# 'aceg'
# """
# for get_up_time in alarm_times[::-1]:
#     if get_up_time + X <= class_time:
#         print(get_up_time / 60, get_up_time % 60)
#         break

import sys


class Solution:
    def latest_getup_time(self, alarm_times, X, class_time):
        """

        :param alarm_times:  所有定的闹钟组成的列表
        :param X: 走到教室的时间
        :param class_time: 上课时间
        :return: 最晚起床时间
        """
        # 边界判定

        for get_up_time in alarm_times[::-1]:
            if get_up_time + X <= class_time:
                print(int(get_up_time / 60), get_up_time % 60)
                break


if __name__ == '__main__':
    # 数据读取
    alarm_times = []

    N = int(sys.stdin.readline().strip())  # 闹钟个数
    while N:
        line = sys.stdin.readline().strip()
        h, m = line.split()
        alarm_times.append(int(h) * 60 + int(m))
        N -= 1
    alarm_times.sort()  # 升序排序

    X = int(sys.stdin.readline().strip())  # 多久能走到教室

    A, B = sys.stdin.readline().strip().split()
    class_time = int(A) * 60 + int(B)  # 上课时间

    # 求最晚起床时间
    Solution().latest_getup_time(alarm_times, X, class_time)
    # print(alarm_times)
    # print(X)
    # print(class_time)
