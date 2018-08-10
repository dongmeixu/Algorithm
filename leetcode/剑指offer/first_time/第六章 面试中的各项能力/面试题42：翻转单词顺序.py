"""

题目描述
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？

"""
# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return ""
        s = list(s)
        start = 0
        end = len(s) - 1

        self.Reverse(s, start, end)

        # 翻转每个单词
        start = end = 0
        while start < len(s):
            if end == len(s) - 1:
                self.Reverse(s, start, end)
                return "".join(s)
            elif s[end] == " ":
                end -= 1
                self.Reverse(s, start, end)
                end += 2
                start = end
            else:
                end += 1

    def Reverse(self, s, start, end):
        # 整体翻转
        while start <= end:
            # 交换
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp

            start += 1
            end -= 1
        return s


print(Solution().ReverseSentence("student. a am I"))
