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


arr = "abcfdsd"
reverse(arr)
