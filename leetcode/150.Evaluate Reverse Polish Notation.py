"""

问题描述：逆波兰表达式求值。给定一个数组，表示一个逆波兰表达式。求其值
如：["2", "1", "+", "3", "*"], 表示(2 + 1) * 3 = 9
如：["4", "13", "5", "/", "+"],表示4 + (13 / 5) = 6

"""

class Solution():
    def sovle(self, arr):
        if not arr:
            return
        stack = []
        for tmp in arr:
            pass
            # if tmp shi shuzi:
            #     stack.append(tmp)
            # elif tmp == "+" or tmp == "-" and tmp == "*" or tmp == "/":
            #     if not stack:
            #         char1 = stack[-1]
            #         char1 = stack[-2]
            #         stack.pop(-1)
            #         stack.pop(-2)
            #         stack.append(int(char1) tmp int(char2))

