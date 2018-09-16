class Solution:
    def MaxSubArray(self, arr):
        if not arr:
            return 0

        # 对于当前的值，有2中选择，选与不选
        current = 0
        maxSum = arr[0]
        for i in range(len(arr)):
            if arr[i] > current + arr[i]:
                current = arr[i]
            else:
                current = current + arr[i]

            maxSum = max(maxSum, current)
        return maxSum


print(Solution().MaxSubArray([1, -2, 3, 10, -4, 7, 2, -5]))


# f(i,j) = f(i - 1, j - 1)  str1[i] ！=str2[j]
#        = 1 + f(i - 1, j - 1)

x = input()
y = input()

len_x = len(x)
len_y = len(y)


