"""
字符串数组的最长公共前缀
Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution:
    # 纵向扫描：从位置0开始，对每一个位置比较所有字符串，直到遇到一个不匹配
    # 时间复杂度O(n1+n2+.....)
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for idx in range(len(strs[0])):
            for i in range(1, len(strs)):
                # 加上test case ["aa", "a"]  len(strs[i]) <= idx
                if len(strs[i]) <= idx or strs[i][idx] != strs[0][idx]:
                    return strs[0][0:idx]
        return strs[0]

    # 横向扫描，每个字符串与第0个字符串，从左到右比较，直到遇到一个不匹配，然后继续下一个字符串
    def longestCommonPrefix_1(self, strs):
        if not strs:
            return ""

        right_most = len(strs[0]) - 1
        for i in range(1, len(strs)):
            for j in range(right_most):
                if strs[i][j] != strs[0][j]:
                    right_most = j - 1
        return strs[0][0:right_most + 1]


print(Solution().longestCommonPrefix(["qwe", "qq", "qdd"]))
print(Solution().longestCommonPrefix_1(["qwe", "qq", "qdd"]))
