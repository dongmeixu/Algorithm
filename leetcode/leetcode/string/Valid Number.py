"""
Validate if a given string is numeric.
Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up
front before implementing one.
"""


class Solution:
    def isNumbers(self, s):
        if not s:
            return False

        for i, tmp in enumerate(s):
            count = self.count(s, i)
            if tmp == "." and count > 1:
                return False
            elif not s[i - 1].isdigit() or not s[i + 1].isdigit() or count > 1:
                return False
            else:
                # tmp > "9" or tmp < "0":
                return False
        return True

    def count(self, s, index):
        if index >= len(s):
            return

        i = 0
        count = 0
        while i < len(s):
            if s[index] == s[i]:
                count += 1
            i += 1
        return count


s = "2e10"
print(Solution().isNumbers(s))
