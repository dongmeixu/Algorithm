"""
写一个函数，求两个整数之和，要求在函数体内不得使用+，-，*，/等四则运算

"""

# TODO:牛客上没通过
class Solution:
    def Add(self, num1, num2):
        # 逻辑异或，逻辑与
        exclusionOr = num1 ^ num2
        land = num1 & num2
        return exclusionOr | (land << 1)


print(Solution().Add(111, 899))
