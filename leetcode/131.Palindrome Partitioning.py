"""
给出一个字符串，拆分这个字符串，
使得所有拆分的子串都是回文字符串。
返回所有的拆分的可能。

给定字符串 s="aab"
结果为[["aa", "b"], ["a", "a", "b"]]
"""


class Solution:
    res = []

    def s(self, nums):
        self.s_main(nums, 0, "")

    def s_main(self, nums, index, p):
        for i in range(len(nums)):
            self.s_main(nums, index + 1, p + nums[i])
