"""
7.1 Search for a Range

Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm’s runtime complexity must be in the order of O(logn).
If the target is not found in the array, return [-1, -1].
For example, Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].


"""


class Solution:
    def searchForRange(self, arr, target):

        if not arr:
            return [-1, -1]

        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                if arr[mid - 1] == target:
                    firstTarget = self.getFirstTarget(arr, target, left, mid - 1)
                else:
                    firstTarget = mid

                if arr[mid + 1] == target:
                    LastTarget = self.getLastTarget(arr, target, mid + 1, right)
                else:
                    LastTarget = mid

                return [firstTarget, LastTarget]

            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1, -1]

    def getFirstTarget(self, arr, target, left, right):

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                if arr[mid - 1] == target:
                    firstTarget = self.getFirstTarget(arr, target, left, mid - 1)
                else:
                    firstTarget = mid
                return firstTarget

            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

    def getLastTarget(self, arr, target, left, right):

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                if arr[mid + 1] == target:
                    LastTarget = self.getLastTarget(arr, target, mid + 1, right)
                else:
                    LastTarget = mid
                return LastTarget

            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1


print(Solution().searchForRange([5, 7, 7, 8, 8, 10], 9))
