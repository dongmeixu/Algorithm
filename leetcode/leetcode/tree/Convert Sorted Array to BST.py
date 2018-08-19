class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二分法 时间复杂度O(n) 空间复杂度O(logn)
class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:  # 终止条件
            return None

        start = 0
        end = len(nums) - 1
        return self.sortedArrayToBST_main(nums, start, end)

    def sortedArrayToBST_main(self, nums, start, end):
        if start >= end:
            return
        mid = start + (end - start) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST_main(nums, start, mid - 1)
        root.right = self.sortedArrayToBST_main(nums, mid + 1, end)
        return root


nums = [1, 2, 3, 4, 5]
print(Solution().sortedArrayToBST(nums))
