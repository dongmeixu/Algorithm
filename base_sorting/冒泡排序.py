import cv2


def bubbleSort(arr):
    if arr is None:
        return

    left = 0
    right = len(arr)

    for i in range(left, right):
        for j in range(left, right - i - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp

    return arr


arr = [3, 4, 1, 2, 9, 6, 5]
print(bubbleSort(arr))
arr = ['3', '4', '1', '2', '9', '6', '5']
print(bubbleSort(arr))
arr = [3.0, 4.0, 1.0, 2.0, 9.0, 6.0, 5.0]
print(bubbleSort(arr))

arr = {"a": 3.0, "b": 4.0, "f": 1.0, "d": 2.0}
print(bubbleSort(list(arr.keys())))


ss = ["1_sogou_50_89", "1_baidu_150_89", "1_ga_500_89", "1_tectent_1000_89"]


for i, s in enumerate(ss):
    print(s)

import keras.metrics