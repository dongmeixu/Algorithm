import sys
import math
MAX_INT = math.sqrt(sys.maxsize) / 2
print(MAX_INT)


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        abs_x = abs(x)
        print(abs_x)
        while abs_x != 0:
            if abs_x >= MAX_INT or abs_x <= -MAX_INT:
                return 0
            rev = rev * 10 + abs_x % 10
            # print(rev)
            # /代表浮点数的相除；//代表整数相除
            abs_x = abs_x // 10
            # print(x)
        print(rev)
        if x < 0:
            rev = -int(rev)
        else:
            rev = int(rev)
        print(int(rev))
        return rev

s = Solution().reverse(-2143847412)
print(s)