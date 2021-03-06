"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent
numbers on the row below.
For example, given the following triangle
[
[2],
[3,4],
[6,5,7],
[4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Note: Bonus point if you are able to do this using only O(n) extra space, where n is the total number of
rows in the triangle.
"""


class Solution:
    min = 0

    def minimumTotal(self, arr):
        if not arr:
            return

        self.minimunTotal_main(arr, 0)

    def minimunTotal_main(self, arr, index):
        for i in range(len(arr[0])):
            self.minimunTotal_main(arr[i], index + 1)


p = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
print(Solution().minimumTotal(p))