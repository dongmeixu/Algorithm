"""
题目描述
拿破仑席卷欧洲大陆之后，代表自由，平等，博爱的竖色三色旗也风靡一时。荷兰国旗就是一面三色旗（只不过是横向的），自上而下为红白蓝三色。
img

该问题本身是关于三色球排序和分类的，由荷兰科学家Dijkstra提出。由于问题中的三色小球有序排列后正好分为三类，Dijkstra就想象成他母国的国旗，于是问题也就被命名为荷兰旗问题（Dutch National Flag Problem）。
下面是问题的正规描述： 现有n个红白蓝三种不同颜色的小球，乱序排列在一起，请通过两两交换任意两个球，使得从左至右，依次是一些红球、一些白球、一些蓝球。
"""


# 思路1：基数排序，分别统计下每个颜色出现的次数，然后遍历赋值
# 思路2:3路快排
class Solution:
    def sortColors(self, nums):
        if not nums:
            return

        num_red = 0
        num_blank = 0
        num_blue = 0
        for num in nums:
            if num == "红":
                num_red += 1
            elif num == "白":
                num_blank += 1
            elif num == "蓝":
                num_blue += 1
        index = 0
        for i in range(num_red):
            nums[index] = "红"
            index += 1
        for i in range(num_blank):
            nums[index] = "白"
            index += 1

        for i in range(num_blue):
            nums[index] = "蓝"
            index += 1
        return nums

    def sortColors_sanlukuaipai(self, nums):
        if not nums:
            return

        zero = -1  # nums[0....zero]  == 0
        two = len(nums)  # nums[two....len(nums)]  == 2
        i = 0

        while i < two:
            if nums[i] == 1:  # 将数组分为3部分（小于V、等于V、大于V），等于V的时候不用管，直接继续遍历
                i += 1
            elif nums[i] == 2:
                two -= 1
                # 将i指向的元素与two指向的元素交换位置
                tmp = nums[i]
                nums[i] = nums[two]
                nums[two] = tmp

            else:
                assert nums[i] == 0
                zero += 1
                # 将i指向的元素与zero指向的元素交换位置
                tmp = nums[i]
                nums[i] = nums[zero]
                nums[zero] = tmp
                i += 1

        return nums


arr = ["蓝", "白", "蓝", "红", "红"]
print(Solution().sortColors(arr))
arr = [2, 1, 2, 0, 0]
print(Solution().sortColors_sanlukuaipai(arr))

