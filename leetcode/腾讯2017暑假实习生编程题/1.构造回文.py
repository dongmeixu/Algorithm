"""
链接：https://www.nowcoder.com/questionTerminal/28c1dc06bc9b4afd957b01acdf046e69
来源：牛客网

给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？
输出需要删除的字符个数。

输入描述:


输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.



输出描述:


对于每组数据，输出一个整数，代表最少需要删除的字符个数。
示例1
输入

abcda
google
输出

2
2

"""

# Python版
# 思路：最长会文字序列：==  Str与reverse_Str的最长公共字序列
# 注意：碰到了楼上Python解法同样的问题，没把循环过程放到name中，一直说是过90%
# 然后超时，放进去就好了。猜一下：是不是给了程序入口能加快解析  # -*- coding:utf-8 -*-
import sys


def maxlcp(strs):
    if strs == None or len(strs) == 0:
        return 0
    lens = len(strs)
    dp = [0] * lens
    dp[0] = 1 if strs[0] == strs[lens - 1] else 0
    for i in range(lens):
        pre = dp[0]
        dp[0] = max(dp[0], 1 if strs[i] == strs[lens - 1] else 0)
        for j in range(1, lens):
            cur = dp[j]
            dp[j] = max(dp[j], dp[j - 1])
            if strs[i] == strs[lens - 1 - j]:
                dp[j] = max(dp[j], pre + 1)
                pre = cur
    return dp[lens - 1]


if __name__ == '__main__':
    while True:
        line = sys.stdin.readline().strip()
        lens = len(line)
        if not line:
            break
        maxLcp = maxlcp(line)
        # print(lens)
        # print(maxLcp)
        print(lens - maxLcp)
