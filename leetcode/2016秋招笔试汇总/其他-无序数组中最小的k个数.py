# -*- coding:utf-8 -*-
# 快排不行，最后求出的最小的k个数的顺序跟原数组是不一致的
# class KthNumbers:
#     def findKthNumbers(self, A, n, k):
#         # write code here
#         res = []
#         if not A or n <= 0 or k > n:
#             return res
#
#         start = 0
#         end = n - 1
#         index = self.partition(A, start, end)
#         while index != (k - 1):
#             if index > (k - 1):  # 说明最小的k个数在index前面的区间
#                 index = self.partition(A, start, index - 1)
#             else:
#                 index = self.partition(A, index + 1, end)
#         return A[:index + 1]
#
#     def partition(self, A, start, end):
#         pivot = A[start]
#         while start < end:
#             while start < end and A[end] >= pivot:
#                 end -= 1
#             A[start] = A[end]
#
#             while start < end and A[start] <= pivot:
#                 start += 1
#             A[end] = A[start]
#         A[end] = pivot
#         return end

class KthNumbers:
    def findKthNumbers(self, A, n, k):
        # write code here
        res = []
        if not A or n <= 0 or k > n:
            return res

        for i in range(n):
            if len(res) < k:
                res.append(A[i])
            else:  # 找出最大的，将现在的元素替换这个最大的值
                max = res[0]
                for tmp in res:
                    if tmp > max:
                        max = tmp
                if max > A[i]:
                    res.remove(max)
                    res.append(A[i])
        return res


A = [127, 1633, 759, 734]
n = 4
k = 2
print(KthNumbers().findKthNumbers(A, n, k))
