# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        res = []
        p = pHead
        while p:
            res.append(p.val)
            p = p.next
        # 原来这个reverse函数，针对列表的操作，
        # 其结果是直接改变列表本身（为了节省空间），
        # 所以，直接就把原先的list改为你所想要的reversed后的结果了，
        # 而返回值，是空的，不返回任何值。
        res.reverse()
        return res


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

s = Solution().ReverseList(node1)
print(s)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


l = list(map(int, input().split()))
pHead = ListNode(l[0])
p = pHead
for x in l[1:]:
    temp = ListNode(x)
    p.next = temp
    p = p.next
res = []
p = pHead
while p:
    print(p.val)
    res.append(p.val)
    p = p.next
res.reverse()
print(res)