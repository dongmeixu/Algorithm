class Solution:
    def IsInterleave(self, s1, s2, s3):

        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)
        if s1_len + s2_len != s3_len:
            return False
        dp = [[False for col in range(s2_len + 1)] for row in range(s1_len + 1)]

        dp[0][0] = True

        for i in range(s1_len + 1):
            for j in range(s2_len + 1):
                if dp[i][j] \
                        or (i - 1 >= 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) \
                        or (j - 1 >= 0 and dp[i][j - 1] and s1[j - 1] == s3[i + j - 1]):
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        return dp[s1_len][s2_len]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(Solution().IsInterleave(s1, s2, s3))
