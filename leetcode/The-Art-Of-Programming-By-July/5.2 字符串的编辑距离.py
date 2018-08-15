"""
字符串编辑距离
题目描述
给定一个源串和目标串，能够对源串进行如下操作：
在给定位置上插入一个字符
替换任意字符
删除任意字符
写一个程序，返回最小操作数，使得对源串进行这些操作后等于目标串，源串和目标串的长度都小于2000。

"""


class Solution:
    """
    edit[i][j]表示A串和B串的编辑距离。
    edit[i][j]表示A串从第0个字符开始到第i个字符和B串从第0个字符开始到第j个字符，这两个字串的编辑距离
    """

    def EditDistance(self, str1, str2):
        if not str1 or not str2:
            return 0

        m = len(str1)
        n = len(str2)

        if m == 0:
            return n
        if n == 0:
            return m

        dis = [[0 for col in range(n + 1)] for row in range(m + 1)]  # 长为m+1，宽为n+1的矩阵
        # dis = [[0] * (n + 1)] * (m + 1)
        # print(dis)
        for i in range(m + 1):  # j==0
            dis[i][0] = i
        for j in range(n + 1):  # i == 0
            dis[0][j] = j

        for i in range(1, m + 1):
            s1_i = str1[i - 1]
            for j in range(1, n + 1):
                s2_j = str2[j - 1]
                insert = dis[i - 1][j] + 1
                delete = dis[i][j - 1] + 1
                replace = dis[i - 1][j - 1]
                flag = 1 if s1_i != s2_j else 0
                dis[i][j] = self.min(insert, delete, replace + flag)

        return dis[m][n]

    def min(self, insert, delete, edit):
        tmp = insert if insert < delete else delete
        return tmp if tmp < edit else edit


'''
    动态规划——字符串的编辑距离
    s1 = "abc", s2 = "def"
    计算公式：
             | 0                                           i = 0, j = 0
             | j                                           i = 0, j > 0
    d[i,j] = | i                                           i > 0, j = 0
             | min(d[i,j-1]+1, d[i-1,j]+1, d[i-1,j-1])    s1(i) = s2(j)
             | min(d[i,j-1]+1, d[i-1,j]+1, d[i-1,j-1]+1)  s1(i) ≠ s2(j)
    定义二维数组[4][4]：
        d e f            d e f
    |x|x|x|x|        |0|1|2|3|
    a |x|x|x|x|  =>  a |1|1|2|3|  => 编辑距离d = [4][4] = 3
    b |x|x|x|x|      b |2|2|2|3|
    c |x|x|x|x|      c |3|3|3|3|
'''


def levenshtein(s1, s2):
    i = 0  # s1字符串中的字符下标
    j = 0  # s2字符串中的字符下标
    s1i = ""  # s1字符串第i个字符
    s2j = ""  # s2字符串第j个字符
    m = len(s1)  # s1字符串长度
    n = len(s2)  # s2字符串长度
    if m == 0:
        return n  # s1字符串长度为0，此时的编辑距离就是s2字符串长度
    if n == 0:
        return m  # s2字符串长度为0，此时的编辑距离就是s1字符串长度
    solutionMatrix = [[0 for col in range(n + 1)] for row in range(m + 1)]  # 长为m+1，宽为n+1的矩阵
    '''
             d e f
          |0|x|x|x|
        a |1|x|x|x|
        b |2|x|x|x|
        c |3|x|x|x|
    '''
    for i in range(m + 1):
        solutionMatrix[i][0] = i
    '''
             d e f
          |0|1|2|3|
        a |x|x|x|x|
        b |x|x|x|x|
        c |x|x|x|x|

    '''
    for j in range(n + 1):
        solutionMatrix[0][j] = j
    '''
        上面两个操作后，求解矩阵变为
             d e f
          |0|1|2|3|
        a |1|x|x|x|
        b |2|x|x|x|
        c |3|x|x|x|
        接下来就是填充剩余表格
    '''
    for x in range(1, m + 1):
        s1i = s1[x - 1]
        for y in range(1, n + 1):
            s2j = s2[y - 1]
            flag = 0 if s1i == s2j else 1
            solutionMatrix[x][y] = min(solutionMatrix[x][y - 1] + 1, solutionMatrix[x - 1][y] + 1,
                                       solutionMatrix[x - 1][y - 1] + flag)

    return solutionMatrix[m][n]


def min(insert, delete, edit):
    tmp = insert if insert < delete else delete
    return tmp if tmp < edit else edit


s1 = "Jult"
s2 = "July"
# distance = levenshtein(s1, s2)
# print(distance)
print(Solution().EditDistance("Jult", "Julys"))
