def Reverse(x):
    if not x:
        return
    x = list(str(x))
    left = 0
    right = len(x) - 1

    while left <= right:
        tmp = x[left]
        x[left] = x[right]
        x[right] = tmp
        left += 1
        right -= 1
    return int(''.join(x))


# x, y = input().strip().split()
# print(Reverse(x) + Reverse(y))
a = input().split()
print(str(int(a[0][::-1]) + int(a[1][::-1]))[::-1].lstrip("0"))