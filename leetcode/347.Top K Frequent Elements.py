"""
描述：给定一个非空数组，返回前k个出现频率最高的元素

"""


class Solution:
    # 时间复杂度O(nlogk)
    def dd(self, nums, k):
        if k <= 0 or k > len(nums):
            return None
        if k == len(nums):
            return nums
        # 统计每个元素出现的次数
        num_maps = {}
        for num in nums:
            num_maps[num] = num_maps.get(num, 0) + 1
        print(num_maps)
        pro_queue = []
        for num, pinlv in num_maps.items():
            if len(pro_queue) >= k:  # 比较频率
                # 从优先队列中找到频率最小的
                min = pro_queue[0]
                for q in pro_queue:
                    if num_maps[q] < num_maps[min]:
                        min = q

                # 将最小频率的元素出队，此时的元素入队
                if num_maps[min] < pinlv:
                    pro_queue.pop(min)
                    pro_queue.append(num)

            else:
                pro_queue.append(num)
        print(pro_queue)


Solution().dd([2, 2, 2, 3, 2, 0, 0], 2)
