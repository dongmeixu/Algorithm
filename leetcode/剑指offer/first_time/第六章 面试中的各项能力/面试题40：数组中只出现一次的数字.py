"""
一个整型数组里除了两个数字之外，其他的数字都出现了一次。
请写程序找出这两个只出现一次的数字。要求时间复杂度为O(n)，空间复杂度是O(1)

"""
"""
思路：
我们还是从头到尾依次异或数组中的每一个数字，那么最终得到的结果就是两个只出现一次的数字的异或结果。
因为其他数字都出现了两次，在异或中全部抵消掉了。
由于这两个数字肯定不一样，那么这个异或结果肯定不为0，也就是说在这个结果数字的二进制表示中至少就有一位为1。
我们在结果数字中找到第一个为1的位的位置，记为第N位。
现在我们以第N位是不是1为标准把原数组中的数字分成两个子数组，第一个子数组中每个数字的第N位都为1，而第二个子数组的每个数字的第N位都为0。
现在我们已经把原数组分成了两个子数组，每个子数组都包含一个只出现一次的数字，而其他数字都出现了两次。因此到此为止，所有的问题我们都已经解决。
"""


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    # def FindNumsAppearOnce(self, array):
    #     xor = 0
    #     # 求出异或的结果
    #     for i in array:
    #         xor ^= i
    #
    #     num1, num2 = 0, 0
    #     mask = 1
    #     while xor & mask == 0:
    #         mask <<= 1
    #     for num in array:
    #         if num & mask == 0:
    #             num1 ^= num
    #         else:
    #             num2 ^= num
    #     print([num1, num2])
    #     return [num1, num2]

    def FindNumsAppearOnce(self, array):
        if not array or len(array) < 2:
            return

        # 1. 获取2个只出现一次的数字的异或结果
        resultExclusiveOR = 0
        for tmp in array:
            resultExclusiveOR ^= tmp

        # 2. get index of the first bit, which is 1 in resultExclusiveOR
        indexOf1 = self.FindFirstBitIs1(resultExclusiveOR)

        num1 = num2 = 0
        for tmp in array:
            if self.IsBit1(tmp, indexOf1):
                num1 ^= tmp
            else:
                num2 ^= tmp
        print([num1, num2])
        return [num1, num2]

    def FindFirstBitIs1(self, res):
        index = 0
        while res & 1 == 0:
            res = res >> 1
            index += 1
        return index

    def IsBit1(self, num, indexBit1):
        num = num >> indexBit1
        return num & 1


data = [1, 2, 4, 3, 3, 2, 1, 6]
Solution().FindNumsAppearOnce(data)
