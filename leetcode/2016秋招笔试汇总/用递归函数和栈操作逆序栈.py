# -*- coding:utf-8 -*-

class ReverseStack:
    def reverseStackRecursively(self, stack, top):
        # write code here
        res = []
        if not stack or top <= 0:
            return res
        self.reverseStackRecursively_main(stack[: top], top, res)
        return res

    def reverseStackRecursively_main(self, stack, n, res):
        if not n:
            return
        res.append(stack[n - 1])
        self.reverseStackRecursively_main(stack[: n - 1], n - 1, res)
        return res


s = [1, 2, 3, 4, 5]
n = 5
print(ReverseStack().reverseStackRecursively([], n))