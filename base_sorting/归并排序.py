"""
1.归并排序是建立在归并操作上的一种有效的排序算法，该算法是采用分治法的一个典型的应用。它的基本操作是：将已有的子序列合并，达到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。

2.归并排序其实要做两件事：
    分解----将序列每次折半拆分
    合并----将划分后的序列段两两排序合并
因此，归并排序实际上就是两个操作，拆分+合并

3.如何合并？
L[first...mid]为第一段，L[mid+1...last]为第二段，并且两端已经有序，现在我们要将两端合成达到L[first...last]并且也有序。
首先依次从第一段与第二段中取出元素比较，将较小的元素赋值给temp[]
重复执行上一步，当某一段赋值结束，则将另一段剩下的元素赋值给temp[]
此时将temp[]中的元素复制给L[]，则得到的L[first...last]有序

4.如何分解？
在这里，我们采用递归的方法，首先将待排序列分成A,B两组；然后重复对A、B序列
分组；直到分组后组内只有一个元素，此时我们认为组内所有元素有序，则分组结束。

"""


# 分组的函数
def merge_sort(L, first, last, tmp):
    if first < last:
        mid = int(first + (last - first) / 2)
        # 递归的进行分组，使得左边序列有序
        merge_sort(L, first, mid, tmp)
        merge_sort(L, mid + 1, last, tmp)

        # 将2个有序序列合并
        merge_array(L, first, mid, last, tmp)


# 合并的函数：将L[first....mid] 与L[mid + 1, last]进行合并
def merge_array(L, first, mid, last, tmp):
    i, j, k = first, mid + 1, 0
    # 当左右两边都有数时进行比较，取较小的数
    while i <= mid and j <= last:
        if L[i] <= L[j]:
            tmp[k] = L[i]
            k += 1
            i += 1
        else:
            tmp[k] = L[j]
            k += 1
            j += 1
    # 当左边的序列还有数
    while i <= mid:
        tmp[k] = L[i]
        k += 1
        i += 1
    # 当右边的序列还有数
    while j <= last:
        tmp[k] = L[j]
        k += 1
        j += 1

    # 将tmp当中该段有序的元素赋值给L,使得待排序序列部分有序
    for i in range(k):
        L[first + i] = tmp[i]


def merge_main(L):
    tmp = len(L) * [0]
    print(tmp)
    merge_sort(L, 0, len(L) - 1, tmp)
    print(L)


L = [8, 4, 9, 2, 4, 0, 2]
merge_main(L)
