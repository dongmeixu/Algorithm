# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return None

        B = [1 for _ in range(len(A))]
        left = [1 for _ in range(len(A))]
        right = [1 for _ in range(len(A))]
        for i in range(1, len(A)):
            left[i] = left[i - 1] * A[i - 1]
            right[i] = A[len(A) - i] * right[i - 1]

        for i in range(len(A)):
            B[i] = left[i] * right[len(A) - i - 1]
        return B


A = [1, 2, 3, 4, 5]
print(Solution().multiply(A))
