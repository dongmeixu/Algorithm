"""
题目：输入数字n,打印-----n=3, 则打印1， 2， 3.。。。。。999

"""


# 问题：当输入的n很大时，我们求最大的n位数是不是用整型或者长整型都会溢出呢？

# 需要考虑大数问题
def print1ToMaxOfNDigits_1(n):
    number = 1
    for i in range(n):  # 找到范围 比如3位数，则打印[1, 10^4)之间的所有数
        number *= 10
    print(number)

    for i in range(1, number):
        print(i)


# 在字符串上模拟数字加法的解法
def print1ToMaxOfNDigits_2(n):
    if n < 0:
        return
    number = [''] * n
    print(len(number))

    while not increment(number):
        printNumber(number)


def increment(number):
    pass


def printNumber(number):
    isBeginning0 = True
    length = len(number)
    res = []
    for i in range(length):
        if isBeginning0 and number[i] != '0':
            isBeginning0 = False
        if not isBeginning0:
            res += number[i]
    # print(res)
    if not res:
        return
    print(''.join(res))


# ###########################递归
def print1ToMaxOfNDigits_3(n):
    if n <= 0:
        return
    number = [''] * n  # 将n位全部初始化为0
    # print(len(number))
    for i in range(10):
        number[0] = str(i)
        print1ToMaxOfNDigits_3_Main(number, n, 0)


def print1ToMaxOfNDigits_3_Main(number, n, index):
    if index == n - 1:  # 已经设置好最后一位了，则打印
        # print(''.join(number).replace("^0+(?!$)", ""))
        printNumber(number)
        return
    for i in range(10):
        number[index + 1] = str(i)
        print1ToMaxOfNDigits_3_Main(number, n, index + 1)


# print1ToMaxOfNDigits_1(6)
print1ToMaxOfNDigits_3(3)
