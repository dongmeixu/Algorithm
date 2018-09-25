def combinationSum(arr, target):
    if not arr or not target:
        return 0

    res = []
    tmp = []

    arr = list(set(arr))
    for num in arr:
        if num > target:
            arr.remove(num)

    dfs(arr, 0, target, tmp, res)

    if not res:
        return 0
    else:
        return 1
    # return res


def dfs(arr, index, target, tmp, res):
    if target == 0:
        res.append(tmp[:])
        return

    if target < 0:
        return

    for i in range(index, len(arr)):
        tmp.append(arr[i])
        dfs(arr[i + 1:], index, target - arr[i], tmp, res)
        tmp.pop()

        # while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        #     i += 1


# N = int(input())
# prices = list(map(int, input().split()))
# M = int(input())
# print(combinationSum(prices, M))
# nums = [10, 1, 2, 7, 6, 1, 5]
# T = 8


# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def miHomeGiftBag(p, m):
    dp = [0 for _ in range(m + 1)]
    for i in range(len(p)):
        for j in range(m, 0, -1):
            if j >= p[i]:
                dp[j] = max(dp[j], dp[j - p[i]] + p[i])
    return dp[-1] == m


# ******************************结束写代码******************************


# N = int(input())
# tmp = list(map(int, input().split()))
# M = int(input())
#
# res = miHomeGiftBag(sorted(tmp), M)
#
# print(str(int(res)) + "\n")


# coding=utf-8


# char_strs = list(input())
# count = 0
# length = 0
# temp = []
# dig = []
# # 遍历
# for i in range(len(char_strs)):
#     if "0" <= char_strs[i] <= "9":
#         count += 1
#         temp.append(char_strs[i])
#     else:
#         if count >= length:
#             length = count
#             count = 0
#             dig = temp[:]
#             temp = []
#         else:
#             temp = []
#             count = 0
# # 结果输出
# result = ''.join(dig)
# print("%s" % result)

# char_strs = list(input())
#
# maxLen, curLen, maxStr, curStr = 0, 0, "", ""
#
# for tmp in char_strs:
#     if tmp.isnumeric():
#         curLen += 1
#         curStr += tmp
#         if curLen >= maxLen:
#             maxLen = curLen
#             maxStr = curStr
#     else:
#         curLen = 0
#         curStr = ""
# print(maxStr)


# import re
# char_strs = input()
# split_char = re.split(r'\D*', char_strs)
# print(max(split_char, key=len))


def HoureRacing(tianji, qiweiwang):
    if not tianji or not qiweiwang:
        return []

    all_arr = tianji + qiweiwang
    for i in range(len(all_arr) >> 1):
        all_arr.append(tianji[i])
        all_arr.append(qiweiming[i])
    dfs(all_arr, 0, [], [])
    # print(res)


def dfs(arr, index, tmp, res):
    if len(tmp) == 2:
        if not (tmp[0] == "L" and tmp[1] == "XXXL"
                or (tmp[0] in tianji and tmp[1] in tianji)
                or (tmp[1] in qiweiming and tmp[1] in qiweiming)
                or (tmp[0] == "S" and (tmp[1] == "XXL" or tmp[1] == "XL"))):

            copy = tmp[:]
            if copy[0] not in res and copy[1] not in res:
                res.extend(copy)
                print(str(copy[0]) + " vs " + str(copy[1]))
                return

    for i in range(index, len(arr)):
        tmp.append(arr[i])
        dfs(arr[i + 1:], index, tmp, res)
        tmp.pop()
    return


tianji = ["L", "M", "S"]
qiweiming = ["XXXL", "XXL", "XL"]
HoureRacing(tianji, qiweiming)


def NumOfTrees(orchardIndex):
    if not orchardIndex:
        return 0
    numOf1 = NumberOf1(orchardIndex)
    return numOf1 ^ orchardIndex


def NumberOf1(n):
    # write code here
    count = 0

    while n:
        count += 1
        n = (n - 1) & n
    return count


print(NumOfTrees(5))
