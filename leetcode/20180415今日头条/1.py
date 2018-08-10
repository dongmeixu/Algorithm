import sys

if __name__ == '__main__':
    # 读取第一行的n
    N = int(sys.stdin.readline().strip())
    A = []
    for i in range(N):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        A.append(values)
    # print(A)

    for Ai in A:
        n = Ai[0]
        Ai = Ai[1:]
        index = 1
        t = Ai[index] - Ai[0]
        while index < n:
            flag = True
            for i in range(0, n):
                if (Ai[i] + t not in Ai) and (Ai[i] - t not in Ai):
                    flag = False
                    break
            if flag:
                print(t)
                break
            index += 1
            t = Ai[index] - Ai[0]
            if index == n - 1:
                print(t)
                break