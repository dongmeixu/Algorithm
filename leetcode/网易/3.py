"""

牛牛以前在老师那里得到了一个正整数数对(x, y), 牛牛忘记他们具体是多少了。
但是牛牛记得老师告诉过他x和y均不大于n, 并且x除以y的余数大于等于k。
牛牛希望你能帮他计算一共有多少个可能的数对。

"""


def sovle(n, k):
    if not n or not k:
        return

    res = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i % j >= k:
                res.append((i, j))

    return len(res)


print(sovle(5, 2))

# 输入：
# 5 2
#
# 输出例子1:
# 7
#
# 例子说明1:
# 满足条件的数对有(2,3),(2,4),(2,5),(3,4),(3,5),(4,5),(5,3)
