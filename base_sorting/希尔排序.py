"""
希尔排序的算法思想：将待排序数组按照步长gap进行分组，然后将每组的元素利用直接插入排序的方法进行排序；每次将gap折半减小，循环上述操作；当gap=1时，利用直接插入，完成排序。
同样的：从上面的描述中我们可以发现：希尔排序的总体实现应该由三个循环完成：

第一层循环：将gap依次折半，对序列进行分组，直到gap=1
第二、三层循环：也即直接插入排序所需要的两次循环。具体描述见上。

"""


def shell_sort(L):
    gap = int(len(L) / 2)
    while gap >= 1:
        for i in range(gap, len(L)):
            for j in range(i - gap, -1, -gap):
                if L[i] < L[j]:
                    tmp = L[j]
                    L[j] = L[i]
                    L[i] = tmp
        gap = int(gap / 2)

    print(L)


L = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
shell_sort(L)
