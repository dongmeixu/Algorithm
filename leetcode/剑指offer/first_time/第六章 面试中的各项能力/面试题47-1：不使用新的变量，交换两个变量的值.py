"""
不使用新的变量，交换两个变量的值。比如有两个变量a,b，交换其值
"""


# 基于加减法
def change(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


# 基于异或法
def change_1(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


print(change(4, 5))
print(change_1(4, 5))
