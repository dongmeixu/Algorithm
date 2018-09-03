"""
题目描述
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""
"""
总结：
                        基于partition函数的思路        基于堆或者红黑树的思路
    时间复杂度                   O(n)                            O(n *logK)
    是否需要修改输入数组          是                               否       
    是否适用于海量数据            否                               是

需要问清楚需求：1.输入的数据量有多大、
                2. 能否一次性载入内存、
                3. 是否允许交换输入数据中数字的顺序等
"""


"""
思路1：
    快速选择
    
    复杂度：O(N) + O(1)
    只有当允许修改数组元素时才可以使用
    快速排序的 partition() 方法，会返回一个整数 j 使得 a[l..j-1] 小于等于 a[j]，
    且 a[j+1..h] 大于等于 a[j]，此时 a[j] 就是数组的第 j 大元素。
    可以利用这个特性找出数组的第 K 个元素，
    这种找第 K 个元素的算法称为快速选择算法。
    
    找到第 K 个元素之后，就可以再遍历一次数组，所有小于等于该元素的数组元素都是最小的 K 个数。
"""


# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k <= 0:
            return []

        length = len(tinput)
        if k > length:
            return []

        start = 0
        end = length - 1
        index = self.partition(tinput, length, start, end)
        print(index)

        while index != (k - 1):
            if index > (k - 1):
                end = index - 1
                index = self.partition(tinput, length, start, end)
                print("---", index)
            else:
                start = index + 1
                index = self.partition(tinput, length, start, end)
        tinput.sort()
        return tinput[:k]

    def partition(self, numbers, length, start, end):
        if not numbers or length <= 0 or start < 0 or end > length:
            return

        tmp = numbers[start]
        while start < end:
            while start < end and numbers[end] >= tmp:
                end -= 1

            numbers[start] = numbers[end]

            while start < end and numbers[start] <= tmp:
                start += 1

            numbers[end] = numbers[start]

        numbers[end] = tmp
        return end


"""
思路2：
   大小为 K 的最小堆

    复杂度：O(NlogK) + O(K)
    特别适合处理海量数据
    应该使用大顶堆来维护最小堆，而不能直接创建一个小顶堆并设置一个大小，企图让小顶堆中的元素都是最小元素。
    
    维护一个大小为 K 的最小堆过程如下：在添加一个元素之后，如果大顶堆的大小大于 K，那么需要将大顶堆的堆顶元素去除。
"""

"""
python的话，直接调用tinput.sort()======》list自带的这个排序函数底层实现：TimSort算法
"""


# -*- coding:utf-8 -*-
class Solution3:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k <= 0:
            return []

        length = len(tinput)
        if k > length:
            return []
        tinput.sort()
        return tinput[:k]


arr = [1, 2, 4, 3]
# arr.sort()
print(Solution().GetLeastNumbers_Solution(arr, 3))
print(Solution3().GetLeastNumbers_Solution(arr, 3))
