"""
小摩手里有一个字符串A，小拜的手里有一个字符串B，B的长度大于等于A，所以小摩想把A串变得和B串一样长，这样小拜就愿意和小摩一起玩了。
而且A的长度增加到和B串一样长的时候，对应的每一位相等的越多，小拜就越喜欢。比如"abc"和"abd"对应相等的位数为2，为前两位。
小摩可以在A的开头或者结尾添加任意字符，使得长度和B一样。现在问小摩对A串添加完字符之后，不相等的位数最少有多少位？

输入描述:
第一行 为字符串A，第二行 为字符串B，
A的长度小于等于B的长度，B的长度小于等于100。
字符均为小写字母。


输出描述:
输出一行整数表示A串添加完字符之后，A B 不相等的位数最少有多少位？

输入例子1:
abe
cabc
shi
输出例子1:
1

"""
import sys


class Solution:
    def solve(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)

        result = 0
        equal = 0
        if n1 == n2:  # 当两个字符串长度一致时
            for i in range(n1):
                if s1[i] == s2[i]:
                    equal += 1
            return equal
        else:
            assert n1 < n2
            for i in range(n2 - n1 + 1):
                k = i
                for j in range(n1):
                    if s2[k] == s1[j]:
                        equal += 1

                    k += 1
                result = max(result, equal)
                equal = 0
        return n2 - (result + (n2 - n1))


try:
    while True:
        s1 = sys.stdin.readline().strip()
        s2 = sys.stdin.readline().strip()
        print(Solution().solve(s1, s2))
except:
    pass
