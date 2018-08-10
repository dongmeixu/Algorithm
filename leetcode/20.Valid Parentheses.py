"""
问题描述：给定一个字符串，只包含(, [, {, ), ], }，
判定字符串中的括号匹配是否合法
"""


class Solution:
    def isValid(self, s):
        if not s:
            return True

        # 定义一个栈
        stack = []
        # 遍历字符串
        for tmp in s:
            if tmp == "(" or tmp == "[" or tmp == "{":
                stack.append(tmp)
            else:

                # 此时代表输入的是右半部分的括号，而栈为空，直接返回Fasle
                if len(stack) == 0:
                    return False

                # 定义一个变量，用于保存右部分的括号应该匹配的括号类型
                match = ""

                if tmp == ")":
                    match = "("
                if tmp == "]":
                    match = "["
                if tmp == "}":
                    match = "{"

                c = stack[-1]
                stack.pop(-1)
                if c != match:
                    return False

        # 遍历完字符串之后还要判断下栈中是否为空
        if len(stack) != 0:
            return False
        return True


# s = "(){}"
s = "(]]]"
print(Solution().isValid(s))
