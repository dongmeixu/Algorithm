a, b = list(map(int, input().split()))
if a % b == 0:  # a 能整除 b
    print(a // b)
else:
    second_pard = []
    remainder_list = []
    first_part = a // b
    a = a % b
    remainder_list.append(a)
    circle_start = -1

    while True:
        a *= 10
        remainder = a % b
        if remainder == 0:
            second_pard.append(a // b)
            break
        elif remainder in remainder_list:
            circle_start = remainder_list.index(remainder)
            second_pard.append(a // b)
            break
        else:
            second_pard.append(a // b)
            remainder_list.append(remainder)
            a = a % b
    if circle_start == -1:
        print(str(first_part) + "." + "".join(list(map(str, second_pard))))
    else:
        print(str(first_part) + "." + "".join(list(map(str, second_pard[0:circle_start]))) +
              "(" + "".join(list(map(str, second_pard[circle_start:]))) + ")")