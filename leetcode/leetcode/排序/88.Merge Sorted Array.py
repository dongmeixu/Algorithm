# 时间复杂度O(m + n),空间复杂度O(1)
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            return

        p1 = m - 1
        p2 = n - 1
        pnew = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[pnew] = nums1[p1]
                pnew -= 1
                p1 -= 1
            elif nums1[p1] < nums2[p2]:
                nums1[pnew] = nums2[p2]
                pnew -= 1
                p2 -= 1
            else:
                nums1[pnew] = nums1[p1]
                nums1[pnew - 1] = nums2[p2]
                pnew -= 2
                p1 -= 1
                p2 -= 1
        while p1 >= 0:
            nums1[pnew] = nums1[p1]
            pnew -= 1
            p1 -= 1
        while p2 >= 0:
            nums1[pnew] = nums2[p2]
            pnew -= 1
            p2 -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(Solution().merge(nums1, m, nums2, n))
print(nums1)
