"""
Implement regular expression matching with support for '.' and '*'.
'.' Matches any single character. '*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)
Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""
class Solution:
    def isMatch(self, s, p):
        return self.isMatch_main(s, 0, len(s) - 1, p, 0, len(p) - 1)

    def isMatch_main(self, s, index_s, len_s, p, index_p, len_p):
        if index_p == len_p:
            return index_s == len_s and s[index_s] == p[index_p]

        if p[index_p + 1] != "*":
            if p[index_p] == s[index_s] or p[index_p] == "." and index_s != len_s:
                return self.isMatch_main(s, index_s + 1, len_s, p, index_p + 1, len_p)
            else:
                return False
        else:
            while p[index_p] == s[index_s] or (p[index_p] == "." and index_s != len_s):
                if self.isMatch_main(s, index_s, len_s, p, index_p + 1, len_p):
                    return True
                index_s += 1

            return self.isMatch_main(s, index_s, len_s, p, index_p + 1, len_p)


s = "aa"
p = ".*"
print(Solution().isMatch(s, p))