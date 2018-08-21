def reverse(arr):
    if not arr:
        return
    stack = []
    result = ""
    for s in arr:
        stack.append(s)

    for i in range(len(stack)):
        result += stack.pop(-1)

    print(result)


def reverse_1(arr):
    if not arr:
        return
    # 'str' object does not support item assignment 字符串是不可变序列
    arr = list(arr)
    # 双指针
    left = 0
    right = len(arr) - 1
    while left <= right:
        tmp = arr[left]
        arr[left] = arr[right]
        arr[right] = tmp
        left += 1
        right -= 1

    print("".join(arr))
    return "".join(arr)


arr = "abcfdsd"
reverse(arr)
reverse_1(arr)
