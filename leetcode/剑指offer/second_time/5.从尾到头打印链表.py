# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        stack = []
        if not listNode:
            return stack

        p = listNode
        while p:
            stack.append(p.val)
            p = p.next

        stack.reverse()
        return stack


if __name__ == '__main__':
    input = list(map(int, input().split()))
    p = phead = ListNode(input[0])
    for i in input[1:]:
        p.next = ListNode(i)
        p = p.next
    print(Solution().printListFromTailToHead(phead))
