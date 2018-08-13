"""
题目描述
将一句话的单词进行倒置，标点不倒置。比如 I like beijing. 经过函数后变为：beijing. like I

输入描述:
每个测试输入包含1个测试用例： I like beijing. 输入用例长度不超过100

输出描述:
依次输出倒置之后的字符串,以空格分割

示例1
输入
I like beijing.

输出
beijing. like I

"""


class Solution:
    def ReverseSequence(self, sequence):
        if not sequence:
            return ""

        sequence = list(sequence)
        len_s = len(sequence)

        start = end = 0

        self.Reverse(sequence, 0, len_s - 1)

        for i in range(len_s):
            if end == len_s - 1:  # 遍历结束
                self.Reverse(sequence, start, end)
            elif sequence[end] == " ":
                self.Reverse(sequence, start, end - 1)
                start = end + 1
                end += 1
            else:
                end += 1

        return "".join(sequence)

    def Reverse(self, s, start, end):
        while start <= end:
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            start += 1
            end -= 1
        return s


seq = input().strip()
print(Solution().ReverseSequence(seq))
