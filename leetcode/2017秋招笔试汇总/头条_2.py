"""
给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：

区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。如给定序列  [6 2 1]则根据上述公式, 可得到所有可以选定各个区间的计算值:



[6] = 6 * 6 = 36;

[2] = 2 * 2 = 4;

[1] = 1 * 1 = 1;

[6,2] = 2 * 8 = 16;

[2,1] = 1 * 3 = 3;

[6, 2, 1] = 1 * 9 = 9;



从上述计算可见选定区间 [6] ，计算值为 36， 则程序输出为 36。

区间内的所有数字都在[0, 100]的范围内;

"""

class Solution:
    result = []

    def Combination(self, s):
        if not s:
            return
        res = []
        for i in range(1, len(s) + 1):
            self.Combination_main(s, i, res)
        return max(self.result)

    # 从数组s中选择m个字符
    def Combination_main(self, s, m, res):
        # m=0,递归结束，输出当前结果
        if m == 0:
            chengji = int(min(res)) * int(sum(res))
            self.result.append(chengji)
            return

        if len(s) != 0:
            # 选择当前元素
            res.append(s[0])
            self.Combination_main(s[1:], m - 1, res)
            # 不选择当前元素
            res.pop()
            self.Combination_main(s[1:], m, res)


N = int(input())
arr = list(map(int, input().strip().split()))
print(Solution().Combination(arr))
