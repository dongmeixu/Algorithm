#
# str1, str2 = list(map(str, input().split()))
#
# str1_start = str2_start = 0
# count = 0
# flag = 1
# first = True
#
# tmp = []
# if str1 == str2 and len(set(str1)) == 1:
#     print(flag)
# else:
#     while str1_start < len(str1) and str2_start < len(str2):
#
#         if str1[str1_start] != str2[str2_start]:
#             if first:
#                 tmp.append(str1_start)
#                 tmp.append(str2_start)
#                 first = False
#
#             if [str2_start, str1_start] != tmp:
#                 print(flag)
#                 break
#
#             count += 1
#         str1_start += 1
#         str2_start += 1
#
#     if count != 2:
#         print(0)
#


# -*- coding:utf-8 -*-
class ReverseEqual:
    def checkReverseEqual(self, s1, s2):
        # write code here

        len_s1 = len(s1)
        len_s2 = len(s2)

        if not s1 or not s2 or len_s1 != len_s2:
            return False

        """
        以s1=ABCD为例，我们先分析s1进行循环移位之后的结果：
        ABCD->BCDA->CDAB->DABC->ABCD  .......
        假设我们把前面移走的数据进行保留：
        ABCD->ABCDA->ABCDAB->ABCDABC->ABCDABCD.....
        因此看出，对s1做循环移位，所得字符串都将是字符串s1s1的子字符串。
        如果s2可以由s1循环移位得到，则一定可以在s1s1上。
        """
        str_s = s1 + s1
        if str_s.find(s2):
            return True

        return False

    #     for k in range(1, len_s1):  # 循环n-1次
    #         if self.leftRotateReverse(s1, k) == s2:
    #             return True
    #     return False
    #
    # def leftRotateReverse(self, s, k):
    #     self.reverse(s, 0, k)
    #     self.reverse(s, k + 1, len(s) - 1)
    #     self.reverse(s, 0, len(s) - 1)
    #     # 旋转整体
    #     # self.reverse(s, 0, len(s) - 1)
    #     #
    #     # 左旋
    #     # self.reverse(s, 0, len(s) - 1 - k)
    #     #
    #     # self.reverse(s, len(s) - k, len(s) - 1)
    #     return s
    #
    # def reverse(self, s, left, right):
    #     while left <= right:
    #         tmp = s[left]
    #         s[left] = s[right]
    #         s[right] = tmp
    #         left += 1
    #         right -= 1
    #     return s


s1 = "bwdyorsngiayocsksyybigrvqxtvhmfyyhmbhhlcenxalcpodllikancwwqbdfrfpcjftfknrekmvdkugdljtlrjcwlwwmswucgebmmsovdezsqtuohnnjjeqyhsnyumngxlgulsiclfrtzzynawgraqctkhrjluykmfujhrwgcgybhaulhmskstwjvgfmofxeuflkkqajialclnlzggccqwdgpkiiobpzgnipliekufylogjrarvxdwslnkwczfltveebzcrjcttxpizhsweeogsixegkwhfwtmtngqjhgkwduahgyyjxihuyxlsksfzpzikdnqvsgyzisnmqgdymkglbtuhjpxhbeybiewrvbdabprqzpvsvdejahfqsnvoijyypmmhpcpbjsukftobgnzxbdltfdfwjk"
s2 = "yypmmhpcpbjsukftobgnzxbdltfdfwjDbwdyorsngiayocsksyybigrvqxtvhmfyyhmbhhlcenxalcpodllikancwwqbdfrfpcjftfknrekmvdkugdljtlrjcwlwwmswucgebmmsovdezsqtuohnnjjeqyhsnyumngxlgulsiclfrtzzynawgraqctkhrjluykmfujhrwgcgybhaulhmskstwjvgfmofxeuflkkqajialclnlzggccqwdgpkiiobpzgnipliekufylogjrarvxdwslnkwczfltveebzcrjcttxpizhsweeogsixegkwhfwtmtngqjhgkwduahgyyjxihuyxlsksfzpzikdnqvsgyzisnmqgdymkglbtuhjpxhbeybiewrvbdabprqzpvsvdejahfqsnvoij"
print(ReverseEqual().checkReverseEqual(s1, s2))


class Palindrome:
    # 方法1：时间复杂度是O(n),空间复杂度O(n),对链表所有元素都进行了遍历
    # def isPalindrome(self, pHead):
    #     # write code here
    #     if not pHead:
    #         return True
    #     stack = []
    #     p = pHead
    #     while p:
    #         stack.append(p.val)
    #         p = p.next
    #
    #     return stack == stack[::-1]

    # 方法2：只比较了一半，将链表划分为左半区跟右半区
    # def isPalindrome(self, pHead):
    #     # write code here
    #     if not pHead or not pHead.next:
    #         return True
    #
    #     stack = []
    #
    #     # 找到中间节点，然后比较右半区逆序的依次跟左半区作比较
    #     right = pHead.next
    #     cur = pHead
    #     while cur.next and cur.next.next:
    #         cur = cur.next.next
    #         right = right.next
    #
    #     # 将右半区的值保存到栈中
    #     while right:
    #         stack.append(right.val)
    #         right = right.next
    #
    #     while stack:
    #         if stack.pop() != pHead.val:
    #             return False
    #         pHead = pHead.next
    #
    #     return True

    def isPalindrome(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return True

        # 1.找到中间节点
        pfast = pslow = pHead
        while pfast.next and pfast.next.next:
            pfast = pfast.next.next  # 尾部
            pslow = pslow.next  # 中间

        pright_first = pslow.next  # 右部分第一个节点
        pslow.next = None  # 中间节点的next指针为空

        # 2.翻转右部分链表
        pre = None
        while pright_first:
            pnext = pright_first.next
            pright_first.next = pre
            pre = pright_first
            pright_first = pnext
        # 此时pre为翻转后的头结点

        # 3.设置头尾指针，从两边依次比较是否相等
        p1 = pHead
        p2 = pre

        res = True
        while p1 and p2:
            if p1.val != p2.val:
                res = False
                break
            p1 = p1.next  # 从左到中间
            p2 = p2.next  # 从右到中间

        # 4.恢复列表
        pright = None
        while pre:
            pnext = pre.next
            pre.next = pright
            pre = pright
            pright = pnext
        pslow.next = pre

        return res