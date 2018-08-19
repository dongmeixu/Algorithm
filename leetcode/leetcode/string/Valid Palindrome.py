"""
给定一个字符串判断是否是回文

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring
cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
Note: Have you consider that the string might be empty? This is a good question to ask during an
interview.
For the purpose of this problem, we define empty string as valid palindrome

"""


class Solution:
    def isPalindrome(self, s):
        # 字符串为空，则认为是回文
        if not s:
            return True

        s = s.lower()
        # 双指针
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] == " " or s[left] == ",":
                left += 1
            elif s[right] == " " or s[right] == ",":
                right -= 1
            elif s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


print(Solution().isPalindrome("A man, a plan, a canal Panama"))
print(Solution().isPalindrome("Cooc"))
