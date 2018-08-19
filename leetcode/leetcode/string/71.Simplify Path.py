"""
问题描述：给定一个Unix系统下的路径，简化这个路径

/home/ ====>/home
/a/./b/../../c/ ====>/c
"""


# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def simplifyPath(self, path):
        if not path:
            return ""

        stack = [path[0]]
        start = 1  # path[start.....len(path) - 1]为待扫描字符串
        k = 0  # 指向字符串中最后一个合法字符的位置
        while start < len(path):
            if path[start] != "/" and path[start] != ".":
                stack.append(path[start])
                k = start
                start += 1
            elif path[k] != path[start] and (path[k] not in [".", "/"] or path[start] not in [".", "/"]):
                stack.append(path[start])
                k = start
                start += 1
            else:  # 连续出现//或者..
                start += 1

        # 特殊情况：去除最后一个”/“ 或者”.“
        if stack[-1] == "/" or stack[-1] == ".":
            stack.pop()

        # 特殊情况：”/../“
        if not stack:
            return "/"
        return "".join(stack)


path = "///..home///..foo///."
# path = "/../"
print(Solution().simplifyPath(path))
