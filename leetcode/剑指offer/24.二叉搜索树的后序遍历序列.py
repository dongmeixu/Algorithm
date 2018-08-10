"""
输入一个整数数组，
判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同

"""


# 递归：
# 对于后序遍历而言，数组最后一个元素一定是根，
# 然后根据根把该数组分为左右两部分（左部分的值都小于根的值，右部分的值都大于根的值）
# 递归判断左右部分

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        length = len(sequence)
        if length == 0:
            return False
        root = sequence[-1]
        i = 0
        for i in range(length):
            if sequence[i] > root:
                break
        for j in range(i, length):
            if sequence[j] < root:
                return False

        left = True
        right = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[: i])
        if j < length - 1:
            right = self.VerifySquenceOfBST(sequence[i: -2])
        return left and right


# s = Solution().VerifySquenceOfBST([5, 7, 6, 9, 11, 10, 8])
# s1 = Solution().VerifySquenceOfBST([7, 4, 6, 5])
s1 = Solution().VerifySquenceOfBST([4, 6, 7, 5])
print(s1)


def lengthOfLastWord(s):
    last_word = s.split(" ")[-1]
    return len(last_word)


if __name__ == "__main__":
    string = input()
    print(string)
    print(lengthOfLastWord(string))
