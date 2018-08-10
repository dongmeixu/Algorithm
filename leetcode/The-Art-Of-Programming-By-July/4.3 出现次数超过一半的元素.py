"""

题目：数组中有一个数字出现的次数超过了数组长度的一半，找出这个数字。

"""


class Solution:
    # 思路1：首先先对数组排序（O(nlogn)）， 然后直接判断排序后的数组中间位置的数字出现的次数，如果大于一半，则返回该元素
    def moreThanHalf_1(self, nums):
        if not nums:
            return -1
        nums.sort()

        mid = len(nums) >> 1

        return self.isOverHalf(nums, mid)

    # 思路2：遍历数组建立哈希表，时间复杂度O(n)，空间复杂度O(n);然后直接遍历整个哈希表，输出输出次数超过一半的数字
    def moreThanHalf_2(self, nums):
        if not nums:
            return -1

        # 建立个hash表
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1

        # 再次遍历哈希表，找出出现次数超过一半的数字
        for key, value in map.items():
            if value > (len(nums) >> 1):
                return key
        return -1

    # 思路3：遍历整个数组，如果2个数不同则删除==》时间复杂度O(n),空间复杂度O(1)
    def moreThanHalf_3(self, nums):
        if not nums:
            return -1

        i = 0
        # 千万记住啊：nums删除操作是原地操作！！！，列表的长度是动态变化的！！！
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:

                if i == len(nums) - 2:
                    nums.pop(i)  # 删除i之后，原本是i + 1的元素现在在第i个元素的位置
                    nums.pop(i)
                    break
                else:
                    nums.pop(i)
                    nums.pop(i)
            else:
                i += 1

        return nums[-1]

    # 思路4：定义两个变量，current表示当前出现的某个元素，time为其出现的次数
    # 1.初始化 current = nums[0]  time = 1
    # 2.遍历整个数组，如果与current相同，则time++
    # 3.不同，则time--
    # 4.当time == 0 时，更新current为当前遍历的元素，time = 1
    def moreThanHalf_4(self, nums):
        if not nums:
            return -1

        time = 1
        current = nums[0]

        for i in range(1, len(nums)):
            print(i)
            # print(current, time)
            if time == 0:
                current = nums[i]
                time = 1
            elif nums[i] == current:
                time += 1
            else:
                time -= 1
        return current

    def isOverHalf(self, nums, mid):
        count = 0
        for num in nums:
            if num == nums[mid]:
                count += 1

        if count > len(nums) // 2:
            return nums[mid]
        else:
            return -1


# print(Solution().moreThanHalf_1([0, 1, 2, 1, 1]))
# print(Solution().moreThanHalf_2([0, 1, 2, 1, 1]))
# print(Solution().moreThanHalf_3([0, 1, 2, 1, 1]))
print(Solution().moreThanHalf_3([5, 5, 7, 2, 1]))
print(Solution().moreThanHalf_4([5, 5, 5, 5, 1]))
print(Solution().moreThanHalf_4([0, 1, 2, 1]))
