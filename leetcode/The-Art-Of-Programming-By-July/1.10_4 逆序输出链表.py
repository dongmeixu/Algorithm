"""
 4. 逆序输出链表
 输入一个链表的头结点，从尾到头反过来输出每个结点的值。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 时间复杂度O(n) 空间复杂度O(n)
    def ReverseList(self, pHead):
        res = []  # 当做栈，保存链表的每个节点的值
        if not pHead:
            return res

        p = pHead
        while p:
            res.append(p.val)
            p = p.next

        res.reverse()
        return res


p = phead = ListNode(1)
p.next = ListNode(2)
p.next.next = ListNode(3)
print(Solution().ReverseList(phead))
