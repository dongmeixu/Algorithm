class editor:
    def __init__(self, s, e):
        self.start = s
        self.end = e


class Solution:
    def editorArrange(self, editors):
        if not editors:
            return
        editors.sort()  # 按开始时间升序排序

        res = []
        pre = 0

        tmp = [0] * 2
        tmp[0] = editors[pre][0]
        for i in range(1, len(editors)):
            if editors[i][0] <= editors[pre][1]:  # 排序后的下一个区间的开始位置小于等于前一个区间的结束位置
                # 去重！！
                if editors[i][1] not in tmp:
                    tmp[1] = editors[i][1]  # 更新
            else:
                res.append(tmp[:])
                tmp[0] = editors[i][0]
            pre = i

        # 打印
        for tmp in res:
            print("{} {}".format(tmp[0], tmp[1]))
        return res


import sys

editors = []
N = int(sys.stdin.readline().strip())  # 编辑数量

while N:
    line = sys.stdin.readline().strip().split(";")
    for str in line:
        start, end = str.split(",")
        editors.append([int(start), int(end)])
    N -= 1

Solution().editorArrange(editors)
