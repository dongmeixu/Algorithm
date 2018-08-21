class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len_all = len(nums1) + len(nums2)

        if len_all & 1 == 0:  # 偶数
            return (self.findKth(nums1, nums2, 0, len(nums1), 0, len(nums2), len_all // 2) + self.findKth(nums1, nums2,
                                                                                                          0, len(nums1),
                                                                                                          0, len(nums2),
                                                                                                          len_all // 2 + 1)) / 2
        else:
            return self.findKth(nums1, nums2, 0, len(nums1), 0, len(nums2), len_all // 2 + 1)

    def findKth(self, nums1, nums2, start1, len1, start2, len2, k):
        # 始终让len1表示较短的那个数组
        if len1 > len2:
            return self.findKth(nums2, nums1, start2, len2, start1, len1, k)

        if len1 == 0:
            return nums2[start2 + k - 1]

        if k == 1:
            return min(nums1[start1], nums2[start2])

        p1 = min(max(k // 2, 1), len1)
        p2 = k - p1

        if nums1[start1 + p1 - 1] == nums2[start2 + p2 - 1]:
            return nums1[start1 + p1 - 1]
        elif nums1[start1 + p1 - 1] > nums2[start2 + p2 - 1]:
            return self.findKth(nums1, nums2, start1, len1, start2 + p2, len2 - p2, k - p2)
        else:
            return self.findKth(nums1, nums2, start1 + p1, len1 - p1, start2, len2, k - p1)


nums1 = [1, 2]
nums2 = [4, 5, 6]
print(Solution().findMedianSortedArrays(nums1, nums2))
