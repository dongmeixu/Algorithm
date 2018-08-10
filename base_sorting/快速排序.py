"""
快速排序的基本思想：挖坑填数+分治法
1. 从序列当中选择一个基准数(pivot)
在这里我们选择序列当中第一个数最为基准数

2. 将序列当中的所有数依次遍历，比基准数大的位于其右侧，比基准数小的位于其左侧

3. 重复步骤1.2，直到所有子集当中只有一个元素为止。
用伪代码描述如下：
    1．i =L; j = R; 将基准数挖出形成第一个坑a[i]。
    2．j--由后向前找比它小的数，找到后挖出此数填前一个坑a[i]中。
    3．i++由前向后找比它大的数，找到后也挖出此数填到前一个坑a[j]中。
    4．再重复执行2，3二步，直到i==j，将基准数填入a[i]中

"""


def quick_sort(L, start, end):
    if start < end:

        i, j, pivot = start, end, L[start]
        while i < j:
            # 右到左找比pivot小的元素
            while i < j and L[j] > pivot:
                j -= 1

            if i < j:
                L[i] = L[j]
                i += 1

            # 左到右找比pivot大的元素
            while i < j and L[i] < pivot:
                i += 1

            if i < j:
                L[j] = L[i]
                j -= 1

            L[i] = pivot

            quick_sort(L, start, i - 1)
            quick_sort(L, i + 1, end)