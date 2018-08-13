import sys


class Activity:
    def __init__(self, s, e):
        self.start = s
        self.end = e


class Solution:
    def activityArrange(self, activities):
        if not activities:
            return
        activities.sort(key=lambda x: x[1])  # 将活动按结束时间升序排序

        res = [False] * len(activities)

        idx = []

        if activities[0][1] > M:  # 如果结束时间最早的那个活动比总的时间都长
            return 0

        res[0] = True  # 第一个活动一定选（因为它的结束时间最早）
        pre = 0
        # idx.append(0)
        for i in range(1, len(activities)):
            if activities[pre][1] <= activities[i][0] < M and activities[pre][1] < M and activities[i][1] < M:  # 下一个活动的开始时间大于等于上一个活动的结束时间
                res[i] = True
                pre = i
                # idx.append(i)
        # print(idx)
        c = 0
        for i in range(len(res)):
            if res[i]:
                c += 1
        return c


if __name__ == '__main__':
    activities = []
    N = int(sys.stdin.readline().strip())  # 活动个数
    M = int(sys.stdin.readline().strip())

    line = sys.stdin.readline().strip().split()
    start = [int(tmp) for i, tmp in enumerate(line) if i & 1 == 0]
    end = [int(tmp) for i, tmp in enumerate(line) if i & 1 == 1]

    i = 0
    while i < len(start):
        if start[i] > end[i]:
            end[i] += M
        activities.append([int(start[i]), int(end[i])])
        i += 1
    print(Solution().activityArrange(activities))

# 抖音
