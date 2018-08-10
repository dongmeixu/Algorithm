# 输入为一个有序数列，及查找的内容

def binarySearch(arr, target):
    if not arr:
        return -1
    ##########################################
    # 循环不变量
    # 在arr[left.......right]的范围里寻找target
    left = 0
    right = len(arr) - 1

    while left <= right:  # 当left=right时，即在arr【right,right】内寻找，区间有效
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            left = mid + 1  # 在arr[mid+1..........right]
        if target < arr[mid]:
            right = mid - 1   # arr[left..........mid-1]
    return -1


arr = [1, 2, 3, 4, 5]
target = 4
print(binarySearch(arr, target))

