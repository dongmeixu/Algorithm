"""
题目描述
输入n个整数，输出其中最小的k个。

"""


class Solution:
    # 方法1：进行排序，再选择前k个元素，O(nlogn)
    def getK(self, arr, k):
        if not arr or not k:
            return []
        if k > len(arr):
            return arr
        arr.sort()
        return arr[:k]

    # 方法2：快排  经过一次patition操作就有一个元素排在了正确的位置；
    def getK_1(self, arr, k):

        if not arr or not k:
            return []
        if k > len(arr):
            return arr

        index = self.partition(arr, 0, len(arr) - 1)
        print(index)
        while index != (k - 1):
            if index > (k - 1):
                index = self.partition(arr, 0, index - 1)
            else:
                index = self.partition(arr, index + 1, len(arr) - 1)
        return arr[:k]

    def partition(self, arr, left, right):

        """

        一趟快速排序的算法是：

        1）设置两个变量i、j，排序开始的时候：i=0，j=N-1；
        2）以第一个数组元素作为关键数据，赋值给key，即key=A[0]；
        3）从j开始向前搜索，即由后开始向前搜索(j--)，找到第一个小于key的值A[j]，将A[j]和A[i]互换；
        4）从i开始向后搜索，即由前开始向后搜索(i++)，找到第一个大于key的A[i]，将A[i]和A[j]互换；
        5）重复第3、4步，直到i=j；
        (3,4步中，没找到符合条件的值，即3中A[j]不小于key,4中A[i]不大于key的时候改变j、i的值，使得j=j-1，i=i+1，直至找到为止。
        找到符合条件的值，进行交换的时候i， j指针位置不变。另外，i==j这一过程一定正好是i+或j-完成的时候，此时令循环结束）。

        """
        pivot = arr[left]
        while left < right:
            while left <= right and arr[right] >= pivot:
                right -= 1
            arr[left] = arr[right]
            while left <= right and arr[left] <= pivot:  # 从前往后找到一个比pivot大的元素
                left += 1
            arr[right] = arr[left]

            arr[left] = pivot
            print(arr)
        return left


arr = [6, 2, 7, 3, 8, 9]
# print(Solution().getK(arr, 4))
print(Solution().getK_1(arr, 4))
