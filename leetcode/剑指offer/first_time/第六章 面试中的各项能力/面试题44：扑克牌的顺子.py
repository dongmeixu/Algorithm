"""
题目描述
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。
"""

class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False

        # 1.数组排序
        numbers.sort()

        # 2.统计数组中0的个数
        numberOfZero = 0
        numberOfGap = 0

        for num in numbers:
            if num == 0:
                numberOfZero += 1

        # 3.统计数组中的间隔数目
        small = numberOfZero  # 代表数组中第一个非0元素的下标
        big = small + 1
        while big < len(numbers):
            # 两个数相等，有对子，不可能是顺子
            if numbers[small] == numbers[big]:
                return False

            numberOfGap += numbers[big] - numbers[small] - 1
            small = big
            big += 1
        return False if numberOfGap > numberOfZero else True


print(Solution().IsContinuous([1, 2, 3, 4, 5]))
