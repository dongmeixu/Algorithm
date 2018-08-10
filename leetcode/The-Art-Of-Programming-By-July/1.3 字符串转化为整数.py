import sys


def StrToInt(s):
    MAX_INT = sys.maxsize
    MIN_INT = MAX_INT + 1

    # 1. 字符串为空
    if not s:
        return -1

    # 2. 包含正负号
    sign = 1  # 默认是正的
    index = 0
    if s[index] == "-":
        sign = -1
        index = 1
    # 3. 是否包含非数字
    if not s[index:].isdigit():
        return -1

    # 4. 溢出
    n = 0
    for i in range(index, len(s)):
        current = s[i]
        if sign == 1 and (n > MAX_INT / 10 or (n == MAX_INT / 10 and int(current) > MAX_INT % 10)):
            n = MAX_INT
            break
        elif sign == -1 and (n > MIN_INT / 10 or (n == MIN_INT / 10 and int(current) > MIN_INT % 10)):
            n = MIN_INT
            break
        n = n * 10 + int(current)
    return sign * n


print(StrToInt("-1233465646456456456009090000"))
