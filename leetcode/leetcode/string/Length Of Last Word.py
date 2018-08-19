"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length
of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.
For example, Given s = "Hello World", return 5.


"""


class Solution:
    def lengthOfLastWord(self, s):
        # 字符串为空
        if not s:
            return 0
        word_list = s.split(" ")
        return len(word_list[-1])

    # 顺序扫描：时间复杂度O(n),空间复杂度O(1)
    def lengthOfLastWord_1(self, s):
        if not s:
            return 0
        len_word = 0
        for tmp in s:
            if tmp != " ":
                len_word += 1
            else:
                len_word = 0
        return len_word


s = "Hello World"
# s = "he"
print(Solution().lengthOfLastWord(s))
print(Solution().lengthOfLastWord_1(s))
