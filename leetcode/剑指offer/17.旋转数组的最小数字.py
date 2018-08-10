"""
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。


"""

"""

链接：https://www.nowcoder.com/questionTerminal/9f3231a991af4f55b95579b44b7a01ba
来源：牛客网

旋转之后的数组实际上可以划分成两个有序的子数组：前面子数组的大小都大于后面子数组中的元素
注意到实际上最小的元素就是两个子数组的分界线。本题目给出的数组一定程度上是排序的，因此我们试着用二分查找法寻找这个最小的元素。
思路：
（1）我们用两个指针left,right分别指向数组的第一个元素和最后一个元素。按照题目的旋转的规则，第一个元素应该是大于最后一个元素的（没有重复的元素）。
但是如果不是旋转，第一个元素肯定小于最后一个元素。
（2）找到数组的中间元素。
中间元素大于第一个元素，则中间元素位于前面的递增子数组，此时最小元素位于中间元素的后面。我们可以让第一个指针left指向中间元素。
移动之后，第一个指针仍然位于前面的递增数组中。
中间元素小于第一个元素，则中间元素位于后面的递增子数组，此时最小元素位于中间元素的前面。我们可以让第二个指针right指向中间元素。
移动之后，第二个指针仍然位于后面的递增数组中。
这样可以缩小寻找的范围。
（3）按照以上思路，第一个指针left总是指向前面递增数组的元素，第二个指针right总是指向后面递增的数组元素。
最终第一个指针将指向前面数组的最后一个元素，第二个指针指向后面数组中的第一个元素。
也就是说他们将指向两个相邻的元素，而第二个指针指向的刚好是最小的元素，这就是循环的结束条件。

"""

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        # write code here
        left = 0  # 指向数组第一个元素
        right = len(rotateArray) - 1  # 指向数组最后一个元素

        while left < right:
            if right - left == 1:
                mid = right
                return rotateArray[mid]
            mid = left + (right - left) // 2
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            else:
                right = mid


s = Solution().minNumberInRotateArray([1,0,1,1,1])
print(s)

