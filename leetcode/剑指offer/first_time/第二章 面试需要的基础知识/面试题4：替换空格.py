"""
题目描述
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy。

"""

"""
在网络编程中，如果URL中含有特殊字符，如空格、“#”等，可能导致服务器端无法获得正确的参数值。
我们需要将这些特殊符号转换成服务器可以识别的字符。转换的规则是在“%”后面跟上ASCII的两位十六进制的表示。
比如空格的ASCII是32，即十六进制的0x20，因此空格被替换成“%20”。再比如“#”的ASCII码位35，
即16进制的0x23，它在URL被替换成“%23”
"""

"""
分析：首先想到原来是一个空格字符，替换之后变成了3个字符，因此字符串会变长。
      1. 如果是在原来的字符串上做替换，那么就有可能覆盖修改在该字符串后面的内存。
      2. 如果是创建新的字符串并在新的字符串上做替换，那么我们可以自己分配足够多的内存。
      
      应该问清楚到底是那种情况
      
      下面假设面试官让我们在原来的字符串上做替换，并且保证输入的字符串后面有足够的空余内存。
      
      （1）时间复杂度为O(n*n)的解法，不足以拿到offer
      最直观的做法：从头到尾扫描字符串，每一次碰到空格字符的时候做替换，此时必须把空格后面所有的字符都后移两个字符。
      但是数组中很多字符都移动了很多次
      
      （2）时间复杂度为O(n)
      可以先遍历一次字符串，这样就能统计出字符串中空格的总数，并可以由此计算出替换之后的字符串的总长度。
      从字符串的后面开始复制和替换。首先准备2个指针，P1,p2。p1指向原始字符串的末尾，而p2指向替换之后的字符串的末尾。
      接下来我们向前移动指针p1,逐个把它指向的字符复制到p2指向的位置，直到碰到第一个空格为止。
      直到碰到空格时，p1向前移动一位，p2向前移动3位
      停止条件：p1 p2指针指向相同位置
"""


# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = s.replace(" ", "%20")
        return s

    def replaceSpace_1(self, s):
        if not s:
            return s
        length = len(s)

        # 统计空格的个数：
        numberOfBlank = 0
        for i in range(length):
            if s[i] == " ":
                numberOfBlank += 1
        # print(numberOfBlank)

        # 把空格替换后的长度，新字符串的长度
        newLength = length + numberOfBlank * 2
        # print(newLength)

        # 声明新字符串列表（因为字符串是不可改变的）
        newStringList = [' '] * newLength

        # 从后往前开始替换
        # 设置两个指针，分别指向那个原字符串和新字符串的末尾位置
        indexOfOriginal = length - 1
        indexOfNew = newLength - 1

        while indexOfOriginal != indexOfNew:  # 如果两个指针位置不同，则表明没有替换完成
            if s[indexOfOriginal] == " ": # 字符为空
                newStringList[indexOfNew] = "0"
                newStringList[indexOfNew - 1] = "2"
                newStringList[indexOfNew - 2] = "%"
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStringList[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1

        if indexOfOriginal > 0: # 将指针相同时，把之前的字符也补上
            for i in range(indexOfOriginal, -1, -1):
                newStringList[i] = s[indexOfOriginal]
                indexOfOriginal -= 1
        return ''.join(newStringList)


s = "we are happy."
print(Solution().replaceSpace_1(s))


