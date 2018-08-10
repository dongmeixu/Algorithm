"""
相关题目：有两个排序的数组A1和A2，内存在A1的末尾有足够多的空余空间容纳A2.
请实现一个函数，把A2中的所有数字插入到A1中并且所有的数字是排序的。

思路：
    合并两个数组（包括字符串）时，如果从前往后复制每个数字（或字符）
    需要重复移动数字（或字符）多次，那么我们可以考虑从后往前复制，
    这样就可减少移动次数，从而提高效率

"""


class Solution():
    def sove(self, A, B):
        # A, B是两个排序好的数组
        lenA = len(A)
        lenB = len(B)

        newLength = lenA + lenB
        # print(newLength)

        indexOfCombine = newLength - 1
        indexOfA = lenA - 1
        indexOfB = lenB - 1

        newArray = [0] * newLength
        # print(len(newArray))
        while indexOfCombine > 0:
            # if A[indexOfA] <= B[0]:
            #     newArray[:indexOfA] = A
            #     newArray[indexOfA + 1:] = B
            #     break
            # if A[indexOfA] >= B[0]:
            #     newArray[:indexOfB] = B
            #     newArray[indexOfB + 1:] = A
            #     break
            if A[indexOfA] < B[indexOfB]:

                newArray[indexOfCombine] = B[indexOfB]
                indexOfCombine -= 1
                indexOfB -= 1
                if indexOfB < 0:
                    newArray[: indexOfA + 1] = A[: indexOfA + 1]
                    break
            if A[indexOfA] > B[indexOfB]:
                newArray[indexOfCombine] = A[indexOfA]
                indexOfCombine -= 1
                indexOfA -= 1
                # if indexOfA > 0:
                #     indexOfA -= 1
            if A[indexOfA] == B[indexOfB]:
                newArray[indexOfCombine] = A[indexOfA]
                indexOfCombine -= 1
                newArray[indexOfCombine] = B[indexOfB]
                indexOfCombine -= 1
                indexOfA -= 1
                indexOfB -= 1
                # if indexOfB > 0:
                #     indexOfB -= 1
                # if indexOfA > 0:
                #     indexOfA -= 1

            # if indexOfB == 0:
            #     newArray[: indexOfCombine] = A[: indexOfA]
        # if abs(indexOfA) - abs(indexOfB) == 1:
        #     newArray[0] = B[0]
        # elif abs(indexOfA) - abs(indexOfB) == -1:
        #     newArray[0] = A[0]
        # print(indexOfA, indexOfB, indexOfCombine)
        print(newArray)
        return newArray


a = [1, 3, 4, 5, 6]
b = [6, 7, 9, 10]
# a = [1, 3, 4, 5, 8]
# b = [6, 7, 9, 10]
Solution().sove(a, b)
