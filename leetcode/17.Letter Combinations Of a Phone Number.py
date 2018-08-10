"""
给定一个数字字符串，返回这个数字字符串能表示的所有字母组合
"""
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

"""

class Solution:
    digits2string = {
        0: " ",
        1: "",
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }

    res = []

    def letterCombinations(self, digits):
        # 不加这句话在leetcode上会报错---依旧显示的是上次运行的结果
        # self.res = []
        if not digits:
            return self.res
        self.findCombinations(digits, 0, "")  # 从数字字符串数组的第一个字符开始
        return self.res

    # s中保存了此时从digits[0...index-1]翻译得到的一个字母字符串
    # 寻找和digits[index]匹配的字母，获得digits[0...index]翻译得到的解
    def findCombinations(self, digits, index, s):
        print(str(index) + ":" + s)
        if index == len(digits):
            # 保存结果
            self.res.append(s)
            print("get " + s + ", return")
            return

        # 做了下处理，当输入的数字字符串为0或者1时
        if int(digits[index]) == 0 or int(digits[index]) == 1:
            letters = "*"
        else:
            letters = self.digits2string[int(digits[index])]
        for letter in letters:
            print("digits[" + str(index) + "] = " + letters, "use: " + letter)
            self.findCombinations(digits, index + 1, s + letter)

        print("digits[" + str(index) + "] = " + s + " complete, return")


s = "23"
print(Solution().letterCombinations(s))
