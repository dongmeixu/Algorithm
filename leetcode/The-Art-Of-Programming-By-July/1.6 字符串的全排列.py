class Solution:
    res = []
    used = []

    def quanpailie(self, s):
        if not s:
            return self.res

        s = list(s)
        len_s = len(s)
        self.used = [False] * len_s

        self.main(s, 0, [])
        return self.res

    def main(self, s, index, p):
        if index == len(s):
            self.res.append("".join(p[:]))
            return

        for i in range(len(s)):
            """0. 输入一个字符串，打印出该字符串中字符的所有排列。"""
            if not self.used[i]:
                p.append(s[i])
                self.used[i] = True
                self.main(s, index + 1, p)
                p.pop()
                self.used[i] = False

            """
            1、已知字符串里的字符是互不相同的，现在任意组合，比如ab，则输出aa，ab，ba，bb，编程按照字典序输出所有的组合。
            """
            # p.append(s[i])
            # self.main(s, index + 1, p)
            # p.pop()
        return


print(Solution().quanpailie("abc"))
