"""
基本思想：
堆排序可以按照以下步骤来完成：

1. 首先将序列构建称为大顶堆；
（这样满足了大顶堆那条性质：位于根节点的元素一定是当前序列的最大值）

2. 取出当前大顶堆的根节点，将其与序列末尾元素进行交换；
（此时：序列末尾的元素为已排序的最大值；由于交换了元素，当前位于根节点的堆并不一定满足大顶堆的性质）

3. 对交换后的n-1个序列元素进行调整，使其满足大顶堆的性质；

"""


def LEFT(i):
    return 2 * i


def RIGHT(i):
    return 2 * i + 1


# ********** 调整大顶堆 **********
# L:待调整序列
# length: 序列长度
# i:需要调整的结点
def adjust_max_heap(L, length, i):
    # 保存当前序列最大值的下标
    largest = i
    # 执行循环操作：2个任务：1 寻找最大值的下标；2 最大值与父节点交换
    while 1:
        # 获得序列左右叶子节点的下标
        left, right = LEFT(i), RIGHT(i)
        # 当左叶子节点的下标小于序列长度 并且 左叶子节点的值大于父节点时，将左叶子节点的下标赋值给largest
        if left < length and L[left] > L[i]:
            largest = left
        # 当右叶子节点的下标小于序列长度 并且 右叶子节点的值大于父节点时，将右叶子节点的下标值赋值给largest
        if left < length and L[right] > L[largest]:
            largest = right

        # 如果largest不等于i 说明当前的父节点不是最大值，需要交换值
        if largest != i:
            temp = L[i]
            L[i] = L[largest]
            L[largest] = temp
            i = largest
            continue
        else:
            break


def build_max_heap(L):
    length = len(L)
    for i in range(int((length - 1) / 2), -1, -1):
        adjust_max_heap(L, length, i)


def heap_sort(L):
    # 先建立大顶堆，保证最大值位于根节点；并且父节点的值大于叶子结点
    build_max_heap(L)
    # i：当前堆中序列的长度.初始化为序列的长度
    i = len(L) - 1
    # 执行循环：1. 每次取出堆顶元素置于序列的最后(len-1,len-2,len-3...)
    #         2. 调整堆，使其继续满足大顶堆的性质，注意实时修改堆中序列的长度
    while i >= 0:
        temp = L[i]
        L[i] = L[0]
        L[0] = temp
        # 堆中序列长度减1
        i = i - 1
        # 调整大顶堆
        adjust_max_heap(L, i, 0)

    print(L)


L = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
heap_sort(L)
