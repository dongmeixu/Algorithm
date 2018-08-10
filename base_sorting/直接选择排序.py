"""

思想：
1. 从初始未排序的序列中选择最大（最小）的值，
2. 将其与初始位置的值进行交换；
3. 在剩下的未排序的序列中在进行步骤1,2

"""
import cv2


def selectSort(arr):
    if arr is None:
        return arr

    left = 0
    right = len(arr)

    for i in range(left, right):
        minIndex = i
        # 选择一个最小的值
        for j in range(i, right):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # 交换
        tmp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = tmp
    return arr


# arr = [3, 4, 1, 2, 9, 6, 5]
# print(selectSort(arr))
# arr = ['3', '4', '1', '2', '9', '6', '5']
# print(selectSort(arr))
# arr = [3.0, 4.0, 1.0, 2.0, 9.0, 6.0, 5.0]
# print(selectSort(arr))
#
# arr = {"a": 3.0, "b": 4.0, "f": 1.0, "d": 2.0}
# print(selectSort(list(arr.keys())))


