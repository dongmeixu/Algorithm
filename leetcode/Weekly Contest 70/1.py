class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        str = '0'
        content = ''
        if N == 1:
            content = '0'
        for count in range(N - 1):
            list = []
            for i in str:
                if i == "0":
                    new = "01"
                else:
                    new = "10"
                list.append(new)
            content = "".join(list)
            str = content
            # print(content)
        # print(content[K - 1])
        return int(content[K - 1])


s = Solution().kthGrammar(1, 1)
print(s)