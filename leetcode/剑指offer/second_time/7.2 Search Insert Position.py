class Solution:
    def searchInsertPos(self, arr, target):
        if not arr:
            return

        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


print(Solution().searchInsertPos([1, 3, 5, 6], 5))
print(Solution().searchInsertPos([1, 3, 5, 6], 2))
print(Solution().searchInsertPos([1, 3, 5, 6], 7))
print(Solution().searchInsertPos([1, 3, 5, 6], 0))
print(Solution().searchInsertPos([], 2))

