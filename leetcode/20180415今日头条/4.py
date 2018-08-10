# # -*- coding:utf-8 -*-
# import sys
#
#
# def parttion(v, left, right):
#     key = v[left]
#     low = left
#     high = right
#     while low < high:
#         while (low < high) and (v[high] >= key):
#             high -= 1
#         v[low] = v[high]
#         while (low < high) and (v[low] <= key):
#             low += 1
#         v[high] = v[low]
#         v[low] = key
#     return low
#
# def quicksort(v, left, right):
#     if left < right:
#         p = parttion(v, left, right)
#         quicksort(v, left, p-1)
#         quicksort(v, p+1, right)
#     return v
#
#
# if __name__ == '__main__':
#     # 读取第一行的n
#     N = int(sys.stdin.readline().strip())
#     A = []
#     for i in range(N):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         A.append(values)
#     # print(A)
#     for Ai in A:
#         k = Ai[0]
#         n = len(Ai)
#         s = Ai.copy()
#         s[0] = 1
#
#         # s1 = quicksort(s, left=0, right=len(s) - 1)
#         print(s[k - 1], n)

# ! /usr/bin/env python
# -*- coding:utf-8 -*-

from math import ceil

import sys


class SelectList:
    def __init__(self, l):
        self.array = list()
        for i in l:
            self.array.append(i)

    def select(self, a, low, high, k):
        result = 0
        p = high - low + 1

        if p < 6:
            a.sort()
            return a[k - 1]
        q = p / 5
        M = [0] * q
        for i in range(0, q):
            t = a[i * 5:i * 5 + 5]
            t.sort()
            M[i] = t[2]
        mm = self.select(M, 0, q - 1, int(ceil(q / 2.0)))

        a1 = []
        a2 = []
        a3 = []
        count1 = 0
        count2 = 0
        count3 = 0
        for i in a:
            if i < mm:
                a1.append(i)
                count1 += 1
            elif i == mm:
                a2.append(i)
                count2 += 1
            else:
                a3.append(i)
                count3 += 1

        if count1 >= k:
            result = self.select(a1, 0, count1 - 1, k)
        elif count1 + count2 >= k:
            result = mm
        elif count1 + count2 < k:
            result = self.select(a3, 0, count3 - 1, k - count1 - count2)
        return result

    def getSelectedElement(self, k):
        return self.select(self.array, 0, len(self.array) - 1, k)


if __name__ == '__main__':

    # 读取第一行的n
    N = int(sys.stdin.readline().strip())
    A = []
    for i in range(N):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        A.append(values)
    # print(A)
    for Ai in A:
        k = Ai[0]
        n = len(Ai)
        s = Ai.copy()
        s[0] = 1
        sl = SelectList(s)
        # s1 = quicksort(s, left=0, right=len(s) - 1)
        # print(s[k - 1], n)
        ss = sl.getSelectedElement(k)
        print(ss, n)