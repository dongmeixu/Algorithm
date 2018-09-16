t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().split()))
    i = 1
    remainder_list = []
    flag = False
    while True:
        remainder = (a*i) % b
        if remainder == c:
            flag = True
            break
        if remainder in remainder_list:
            break
        else:
            remainder_list.append(remainder)
        i += 1
    if flag:
        print("YES")
    else:
        print("NO")