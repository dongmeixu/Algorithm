# 基本思路是对任意字符串，如果头和尾相同，那么它的最长回文子串一定是去头去尾之后的部分的最长回文子串加上头和尾。
# 如果头和尾不同，那么它的最长回文子串是去头的部分的最长回文子串和去尾的部分的最长回文子串的较长的那一个。
# P[i,j]P[i,j]表示第i到第j个字符的回文子串数
# dp[i,i]=1dp[i,i]=1
# dp[i,j]=dp[i+1,j−1]+2|s[i]=s[j]dp[i,j]=dp[i+1,j−1]+2|s[i]=s[j]
# dp[i,j]=max(dp[i+1,j],dp[i,j−1])|s[i]!=s[j]dp[i,j]=max(dp[i+1,j],dp[i,j−1])|s[i]!=s[j]
def longestPalindrome(s):
    n = len(s)
    maxl = 0
    start = 0
    for i in range(n):
        if i - maxl >= 1 and s[i - maxl - 1: i + 1] == s[i - maxl - 1: i + 1][::-1]:
            start = i - maxl - 1
            maxl += 2
            continue
        if i - maxl >= 0 and s[i - maxl: i + 1] == s[i - maxl: i + 1][::-1]:
            start = i - maxl
            maxl += 1
    return s[start: start + maxl]


def longestPalindrome_2(s):
    n = len(s)
    dp = [[0] * n] * n
    start = 0
    for i in range(n):
        for j in range(n - 1, i + 1, -1):
            if i == j:
                dp[i][j] = 1
            if s[i] == s[j]:
                start = i
                dp[i][j] = dp[i - 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                start = max(i + 1, i)
    print(start, start + dp[-1][-1])
    return dp[-1][-1]


print(longestPalindrome("abaab"))
print(longestPalindrome_2("abaab"))
