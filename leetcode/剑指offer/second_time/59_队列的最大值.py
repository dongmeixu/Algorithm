# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or not size or size > len(num):
            return []

        n = len(num)

        res = []
        queue = [num[0]]
        for i in range(1, n):
            if len(queue) == size:
                res.append(max(queue))
                queue.pop(0)

            queue.append(num[i])
            if i == n - 1:
                res.append(max(queue))

        return res


# num = [2, 3, 4, 2, 6, 2, 5, 1]
num = [10,14,12,11]
k = 5
print(Solution().maxInWindows(num, k))
