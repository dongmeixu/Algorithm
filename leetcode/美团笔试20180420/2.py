# import sys
# T = int(raw_input())
# for i in range(T):
#     n = int(raw_input())
#     count = 0
#     for i in range(1, n+1):
#         count += len(str(i))
#     sys.stdout.write(str(count) + "\n")



import sys
T = int(raw_input())
for i in range(T):
    n = int(raw_input())
    count = 0
    l = len(str(n))
    # print("==========")
    for j in range(1, l):
        count += ((10**(j-1)) * 9) * j
        print(count)
    count += l * (n-(10**(l-1))+1)
    print(count)
    sys.stdout.write(str(count) + "\n")