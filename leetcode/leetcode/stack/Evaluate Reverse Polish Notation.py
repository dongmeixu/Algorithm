"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.
Some examples:
["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

# 时间复杂度O（n）,空间复杂度O（logn）
class Solution:
    def evalRPN(self, tokens):
        # 表达式为空，返回0
        if not tokens:
            return 0

        # 定义合法的操作符
        operators = ["+", "-", "*", "/"]

        # 左到右扫描表达式，遇到数字则入栈，若遇到操作符，则依次从栈中弹出2个元素与操作符进行运算，将运算后的结果再次入栈
        stack = []  # 数字栈
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                if len(stack) < 2:
                    print("不是标准的后缀表达式")
                digit2 = int(stack[-1])
                digit1 = int(stack[-2])
                stack.pop()
                stack.pop()
                if tokens[i] == "+":
                    stack.append(digit1 + digit2)
                elif tokens[i] == "-":
                    stack.append(digit1 - digit2)
                elif tokens[i] == "*":
                    stack.append(digit1 * digit2)
                else:
                    assert tokens[i] == "/"
                    if digit2 == 0:
                        print("除零溢出")
                    stack.append(digit1 / digit2)

        return stack[0]


# tokens = ["2", "1", "+", "3", "*"]
tokens = ["4", "13", "5", "/", "+"]
print(Solution().evalRPN(tokens))
print("/*" in ["*", "/"])
