"""
3、单词翻转。输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变，句子中单词以空格符隔开。为简单起见，标点符号和普通字母一样处理。例如，输入“I am a student.”，则输出“student. a am I”。
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


print(Solution().ReverseSequence("I am a student."))
