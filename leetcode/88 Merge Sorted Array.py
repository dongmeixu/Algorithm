"""
给定两个有序整型数组nums1, nums2，将nums2的元素归并到nums1中

"""
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # 当其中一个为空的时候
        if not nums1:
            return nums2
        if not nums2:
            return nums1

        # p1,p2,pnew 分别指向nums1, nums2以及归并后的数组的最后一个索引的位置
        p1 = m - 1
        p2 = n - 1
        pnew = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[pnew] = nums1[p1]
                pnew -= 1
                p1 -= 1
            else:
                nums1[pnew] = nums2[p2]
                pnew -= 1
                p2 -= 1

        while p1 >= 0:
            nums1[pnew] = nums1[p1]
            p1 -= 1

        while p2 >= 0:
            nums1[pnew] = nums2[p2]
            p2 -= 1
        return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(Solution().merge(nums1, m, nums2, n))
