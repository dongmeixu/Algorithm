class Solution:
    # 1.判断n是不是负数，若是，求补
    # 2.将除去1之外的字符串用空代替，统计长度即可
    def NumberOf1(self, n):
        # write code here
        if not n:
            return 0

        count = 0
        while n:
            if n & 1:
                count += 1
            n = n >> 1
        return count
    # def NumberOf1(self, n):
    #     # write code here
    #     if not n:
    #         return 0
    #
    #     flag = 1
    #     count = 0
    #     while flag:
    #         if n & flag:
    #             count += 1
    #         flag = flag << 1
    #     return count

    # def NumberOf1(self, n):
    #     if not n:
    #         return 0
    #
    #     count = 0
    #     while n:
    #         n = (n - 1) & n
    #         count += 1
    #     return count


print(Solution().NumberOf1(5))
