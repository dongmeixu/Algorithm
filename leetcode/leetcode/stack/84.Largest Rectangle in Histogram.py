"""
Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.
భ 4-1 Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3]
"""

# 用一个栈来维护高度非递减的下标：
# 1.如果栈为空或者当前栈顶元素对应的高度小于等于当前扫描到的高度，入栈
# 2.若不满足：弹出栈顶元素，计算面积并更新面积（面积=栈顶元素对应的高度*i if not stack else i - top + 1）,
#   直到该栈再次满足非递减这个性质为止
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
