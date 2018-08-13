# coding=utf-8
import sys

# 数据读取
squence_1 = []
squence_2 = []

N = int(sys.stdin.readline().strip())  # 每个序列个数

line = sys.stdin.readline().strip()
squence_1.append([int(i) for i in line.split()])

line = sys.stdin.readline().strip()
squence_2.append([int(i) for i in line.split()])

max(squence_1)

max = sorted(squence_1, reverse=True)
min = sorted(squence_2)
print(max)
print(max[0][0] - min[0][-1])


