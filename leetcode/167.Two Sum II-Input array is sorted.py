"""
给定一个有序整型数组和一个整数target,在其中寻找两个元素，使其和为target.
返回这两个数的索引。

-如果没有解怎样？
-如果有多少个解？
"""
"""
1. 最直接的思考：暴力解法。双层遍历O(n^2)
"""

# class Solution:
#     def twoSum(self, numbers, target):
#         if not numbers:
#             return -1
#         N = len(numbers)
#         for i in range(N):
#             for j in range(i, N):
#                 if numbers[i] + numbers[j] == target:
#                     return i + 1, j + 1


"""
2. 最直接的思考：暴力解法。双层遍历O(n^2)
"""


class Solution:
    def twoSum(self, numbers, target):
        if not numbers:
            return -1
        N = len(numbers)
        for i in range(N):
            j = self.binarySearch(numbers[i + 1:], target - numbers[i])

            if j != -1:  # 找到了
                return i + 1, j + 1 + (i + 1)
        return -1

    def binarySearch(self, numbers, target):
        if not numbers:
            return -1
        left = 0
        right = len(numbers)  # 在numbers[left, right)范围内查找

        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] == target:
                return mid
            if target > numbers[mid]:
                left = mid + 1
            if target < numbers[mid]:
                right = mid - 1

        return -1


"""
3. 对撞指针（设置两个指针）
"""


class Solution_1:
    def twoSum(self, numbers, target):
        if not numbers:
            return -1
        left = 0
        right = len(numbers) - 1

        while left <= right:
            if numbers[left] + numbers[right] == target:
                return left + 1, right + 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return -1


numbers = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(numbers, target))
print(Solution_1().twoSum(numbers, target))
