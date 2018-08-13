"""
题目：输入一个链表的头结点，从尾到头反过来打印每个节点的值


思路：
    思路1：栈-----》先全部入栈，之后全部出栈
    思路2：递归，每访问到一个节点的时候，先递归输出它后面的节点，再输出该节点自身。

"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        # 用列表模拟栈
        result = []
        if not listNode:
            return result
        while listNode:
            result.append(listNode.val)
            listNode = listNode.next

        result.reverse()
        return result

    def printListFromTailToHead_digui(self, listNode):
        # write code here
        # 用列表模拟栈
        p = listNode
        result = []
        if not p:
            return result
        if p.next:
            result.extend(self.printListFromTailToHead(p.next))
        result.extend([p.val])

        return result


if __name__ == '__main__':
    input = list(map(int, input().split()))
    p = phead = ListNode(input[0])
    for i in input[1:]:
        p.next = ListNode(i)
        p = p.next
    Solution().printListFromTailToHead_digui(phead)
