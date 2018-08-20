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
        if len(s) <= 1:
            return True
        # Python isalnum() 方法检测字符串是否由字母和数字组成。
        # s.isalnum()

        s = s.lower()
        # 双指针
        left = 0
        right = len(s) - 1
        while left <= right and s.isalnum():
            while not ("a" <= s[left] <= "z") and left <= right:
                left += 1
            while not ("a" <= s[right] <= "z") and left <= right:
                right -= 1

            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome(".,"))
