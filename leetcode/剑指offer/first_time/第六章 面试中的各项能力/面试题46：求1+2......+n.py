"""

求1+2+3+...+n，
要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

"""


# 思路1：逻辑与的短路性质：当 && 左部分的表达式为False,则不用计算右部分的表达式
class Solution:
    def Sum_Solution(self, n):
        return n > 0 and (n + self.Sum_Solution(n - 1))


print(Solution().Sum_Solution(5))

# 思路2：逻辑或的短路性质：当 || True,则不用计算右部分的表达式
class Solution:
    def Sum_Solution(self, n):
        return n == 0 or (n + self.Sum_Solution(n - 1))


print(Solution().Sum_Solution(5))
