# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # 1.如果都为空
        if not s and not pattern:
            return True
        # 2.如果 s 不为空，pattern为空，则返回False
        elif s and not pattern:
            return False
        # 3.如果 s 为空，pattern不为空，分类讨论
        elif not s and pattern:
            # 如果p第二个元素为*，则p后移2位继续匹配
            if len(pattern) == 2 and pattern[1] == "*":
                return True
            elif len(pattern) > 2 and pattern[1] == "*":
                return self.match(s, pattern[2:])
            else:
                return False
        # 4.都不为空
        else:
            if len(pattern) > 1 and pattern[1] == "*":
                # 如果第一个字符不匹配，而且p第一个字符不为.,则将p后移继续匹配
                if s[0] != pattern[0] and pattern[0] != ".":
                    return self.match(s, pattern[2:])
                else:
                    # 如果第一个字符匹配，第二个字符为*时，有三种情况
                    return self.match(s[1:], pattern[1:]) or \
                           self.match(s, pattern[2:]) or \
                           self.match(s[1:], pattern)

            else:
                if s[0] == pattern[0] or pattern[0] == ".":
                    return self.match(s[1:], pattern[1:])
                else:
                    return False


print(Solution().match("aaa", "ab*ac*a"))
