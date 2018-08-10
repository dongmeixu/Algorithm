"""
2、判断一个栈是不是“回文”
分析：对于栈的话，只需要将字符串全部压入栈，然后依次将各字符出栈，这样得到的就是原字符串的逆置串，分别和原字符串各个字符比较，就可以判断了。
"""


# 时间复杂度跟空间复杂度都是O(n)
class Solution:
    def isPalindrom(self, origStack):
        if not origStack:
            return True

        stack = []
        # 入栈
        for s in origStack:
            stack.append(s)

        # 出栈
        popstack = []
        for i in range(len(stack) - 1, -1, -1):
            popstack.append(stack[i])

        if popstack != stack:
            return False
        else:
            return True


print(Solution().isPalindrom([1]))
