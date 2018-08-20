"""
Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.
భ 4-1 Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3]
"""


class Solution:
    # 时间复杂度O(n),空间复杂度O(n)
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        heights.append(0)
        result = 0

        i = 0
        while i < len(heights):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                tmp = stack[-1]
                stack.pop()
                result = max(result, heights[tmp] * (i if not stack else i - stack[-1] - 1))

        return result


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
