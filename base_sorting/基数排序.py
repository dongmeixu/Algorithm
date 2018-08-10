"""
1. 基数排序：通过序列中各个元素的值，对排序的N个元素进行若干趟的“分配”与“收集”来实现排序。
    分配：我们将L[i]中的元素取出，首先确定其个位上的数字，根据该数字分配到与之序号相同的桶中
    收集：当序列中所有的元素都分配到对应的桶中，再按照顺序依次将桶中的元素收集形成新的一个待排序列L[ ]
    对新形成的序列L[]重复执行分配和收集元素中的十位、百位...直到分配完该序列中的最高位，则排序结束

2. 根据上述“基数排序”的展示，我们可以清楚的看到整个实现的过程

"""


# 首先确定排序的次数：排序次数与序列中最大元素的位数相关
def radix_sort_nums(L):
    if not L:
        return
    # 找到最大元素
    max_num = L[0]
    for num in L:
        if num > max_num:
            max_num = num
    # 计算最大元素的位数
    times = 0
    while max_num > 0:
        max_num = int(max_num / 10)
        times += 1
    print("最大位数为：", times)

    return times


# 找到num从低到高第pos位的数据
def get_num_pos(num, pos):
    return (int(num / 10 ** (pos - 1))) % 10


# 基数排序
def radix_sort(L):
    count = 10 * [0]  # 存放各个桶的数据统计个数
    bucket = len(L) * [None]  # 暂时存放排序结果
    # 从低位到高位依次执行循环
    for pos in range(1, radix_sort_nums(L) + 1):
        # 统计当前该位的元素数目
        for x in L:
            j = get_num_pos(x, pos)
            count[j] += 1
            # count[i]表示第i个桶的右边界索引
            for x in range(1, 10):
                count[x] = count[x] + count[x - 1]
            # 将数据依次装入桶中
            for x in range(len(L) - 1, -1, -1):
                # 求出元素第K位的数字
                j = get_num_pos(L[x], pos)
                # 放入对应的桶中，count[j]-1是第j个桶的右边界索引
                bucket[count[j] - 1] = L[x]
                # 对应桶的装入数据索引-1
                count[j] = count[j] - 1
            # 将已分配好的桶中数据再倒出来，此时已是对应当前位数有序的表
            for x in range(0, len(L)):
                L[x] = bucket[x]

