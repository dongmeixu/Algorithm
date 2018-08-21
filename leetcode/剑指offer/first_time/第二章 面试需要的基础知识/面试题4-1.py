"""
相关题目：有两个排序的数组A1和A2，内存在A1的末尾有足够多的空余空间容纳A2.
请实现一个函数，把A2中的所有数字插入到A1中并且所有的数字是排序的。

思路：
    合并两个数组（包括字符串）时，如果从前往后复制每个数字（或字符）
    需要重复移动数字（或字符）多次，那么我们可以考虑从后往前复制，
    这样就可减少移动次数，从而提高效率

"""


class Solution():
    def sove(self, A, m, B, n):
        # A, B是两个排序好的数组
        if not A:
            return B
        if not B:
            return A

        newLength = m + n
        # print(newLength)

        indexOfCombine = newLength - 1
        indexOfA = m - 1
        indexOfB = n - 1

        while indexOfA >= 0 and indexOfB >= 0:
            if A[indexOfA] > B[indexOfB]:
                A[indexOfCombine] = A[indexOfA]
                indexOfCombine -= 1
                indexOfA -= 1
            elif A[indexOfA] < B[indexOfB]:
                A[indexOfCombine] = B[indexOfB]
                indexOfCombine -= 1
                indexOfB -= 1
            else:
                A[indexOfCombine] = A[indexOfA]
                A[indexOfCombine - 1] = B[indexOfB]
                indexOfCombine -= 2
                indexOfA -= 1
                indexOfB -= 1

        while indexOfA >= 0:
            A[indexOfCombine] = A[indexOfA]
            indexOfCombine -= 1
            indexOfA -= 1

        while indexOfB >= 0:
            A[indexOfCombine] = B[indexOfB]
            indexOfCombine -= 1
            indexOfB -= 1

        return A


a = [1, 3, 4, 5, 6, 0, 0, 0, 0]
b = [6, 7, 9, 10]
# a = [1, 3, 4, 5, 8]
# b = [6, 7, 9, 10]
print(Solution().sove(a, 5, b, 4))
