"""
一个整型数组里除了两个数字之外，其他的数字都出现了一次。
请写程序找出这两个只出现一次的数字。要求时间复杂度为O(n)，空间复杂度是O(1)

"""


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        xor = 0
        # 求出异或的结果
        for i in array:
            xor ^= i
            
        num1, num2 = 0, 0
        mask = 1
        while xor & mask == 0:
            mask <<= 1
        for num in array:
            if num & mask == 0:
                num1 ^= num
            else:
                num2 ^= num
        print([num1, num2])
        return [num1, num2]


data = [1, 2, 4, 3, 3, 2, 1, 6]
Solution().FindNumsAppearOnce(data)
