"""
问题一、活动安排问题
问题表述：设有n个活动的集合E = {1,2,…,n}，其中每个活动都要求使用同一资源，如演讲会场等，而在同一时间内只有一个活动能使用这一资源。
每个活i都有一个要求使用该资源的起始时间si和一个结束时间fi,且si < fi 。如果选择了活动i，则它在半开时间区间[si, fi)内占用资源。
若区间[si, fi)与区间[sj, fj)不相交，则称活动i与活动j是相容的。也就是说，当si >= fj或sj >= fi时，活动i与活动j相容。
由于输入的活动以其完成时间的非减序排列，所以算法greedySelector每次总是选择具有最早完成时间的相容活动加入集合A中。
直观上，按这种方法选择相容活动为未安排活动留下尽可能多的时间。
也就是说，该算法的贪心选择的意义是使剩余的可安排时间段极大化，以便安排尽可能多的相容活动。

算法greedySelector的效率极高。
当输入的活动已按结束时间的非减序排列，算法只需O(n)的时间安排n个活动，使最多的活动能相容地使用公共资源。
如果所给出的活动未按非减序排列，可以用O(nlogn)的时间重排。


"""
import sys

"""

注意：这块的活动起止时间是一个类-----》如果将开始时间，截止时间分为用数组表示如何求解。。。。。


"""


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
        res[0] = True  # 第一个活动一定选（因为它的结束时间最早）
        pre = 0
        idx.append(0)
        for i in range(1, len(activities)):
            if activities[i][1] >= activities[pre][0]:  # 下一个活动的开始时间大于等于上一个活动的结束时间
                res[i] = True
                pre = i
                idx.append(i)
        print(idx)
        return res


if __name__ == '__main__':
    activities = []
    N = int(sys.stdin.readline().strip())  # 活动个数
    while N:
        line = sys.stdin.readline().strip()
        start, end = line.split()
        activities.append([int(start), int(end)])
        N -= 1

    print(Solution().activityArrange(activities))

    # list = [[3, 8], [5, 9], [3, 10], [1, 2]]
    # list.sort(key=lambda x: x[1])   # 按照第二个元素升序排序
    # print(list)
