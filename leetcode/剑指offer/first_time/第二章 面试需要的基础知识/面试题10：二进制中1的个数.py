"""
题目描述：
    输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""

"""
分析：
    1. 基本思路：先判断整数二进制表示中最右边一位是不是1.
    接着把输入的整数右移一位，此时原来处于从右边数起的第二位被移到最右边了，
    再判断是不是1.这样每次移动一位，直到整个整数变为0为止。
    
    存在的问题，如果输入的整数是负数，会陷入死循环
    
    
    2. 基本思想：让1左移，而保持原来的整数不变
    
    3. 基本思想：把一个整数减去1，再和原整数做与运算，会把该整数最右边一个1变为0.
    那么一个整数的二进制表示中有多少个1，就可以进行多少次这样的操作。
    
    
相关题目：
    1. 用一条语句判断一个整数是不是2的整数次方。
    一个整数如果是2的整数次方，那么它的二进制表示中有且只有一位是1，而其他所有位都是0.
    根据前面的分析，把这个整数减去1之后再和它自己做与运算，这个整数中唯一的1就会变成0
    
    2. 输入两个整数m和n, 计算需要改变m的二进制表示中的多少位才能得到n。
    比如10的二进制表示为1010,13的二进制表示为1101，需要改变1010中的3位才能得到1101.
    我们可以分为两步解决这个问题：第一步求这两个数的异或，第二步统计异或结果中1的位数
    
"""


class Solution:
    # 1.判断n是不是负数，若是，求补
    # 2.将除去1之外的字符串用空代替，统计长度即可
    def NumberOf1(self, n):
        # write code here
        count = 0
        while n:
            if n & 1:
                count += 1
            n = n >> 1
        return count

    def NumberOf1_2(self, n):
        # write code here
        count = 0
        flag = 1
        while flag:
            if n & flag:
                count += 1
            flag = flag << 1
        return count

    def NumberOf1_3(self, n):
        # write code here
        count = 0

        while n:
            count += 1
            n = (n - 1) & n
        return count


print(Solution().NumberOf1(5))
# print(Solution().NumberOf1_2(5))
# print(Solution().NumberOf1_3(5))
