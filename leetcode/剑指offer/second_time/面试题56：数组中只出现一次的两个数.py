class Solution:
    def FindNumsAppearOnce(self, array):
        if not array or len(array) < 2:
            return

        resultOfXOR = 0
        for tmp in array:
            resultOfXOR ^= tmp

        indexOfBit1 = self.FindFirstBitOf1(resultOfXOR)

        num1 = num2 = 0
        for tmp in array:
            if self.IsBit1(tmp, indexOfBit1):
                num1 ^= tmp
            else:
                num2 ^= tmp
        return [num1, num2]

    def FindFirstBitOf1(self, num):
        if not num:
            return
        index = 0
        while num & 1 == 0:
            num = num >> 1
            index += 1
        return index

    def IsBit1(self, num, index):
        num = num >> index
        return num & 1


data = [1, 2, 4, 3, 3, 2, 1, 6]
print(Solution().FindNumsAppearOnce(data))
