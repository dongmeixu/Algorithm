class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        list_j = list(J)
        list_S = list(S)
        for i in list_S:
            if i in list_j:
                count += 1
        # print(count)
        return count

Solution().numJewelsInStones("aa", "aAAbbbb")
Solution().numJewelsInStones("z", "AZ")


class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i in range(len(A)):
            if abs(A[i] - i) >= 2:
                return False
        return True
l = Solution().isIdealPermutation([1, 2, 0])
q = Solution().isIdealPermutation([1, 0, 2])

print(l)
print(q)