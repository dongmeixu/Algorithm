# 首尾指针跟踪
# 两个数不相等就进行加法：小的数加上相邻的值
n = input().strip()
arr = [int(x) for x in input().strip().split()]


def parlindrom(arr, head, tail):
    times = 0
    left = arr[head]
    right = arr[tail]
    while head < tail:
        if left < right:
            head += 1
            left += arr[head]
            times += 1
            continue
        elif left > right:
            tail -= 1
            right += arr[tail]
            times += 1
            continue
        elif left == right:
            head += 1
            tail -= 1
            left = arr[head]
            right = arr[tail]
    return times


print(parlindrom(arr, 0, int(n) - 1))
