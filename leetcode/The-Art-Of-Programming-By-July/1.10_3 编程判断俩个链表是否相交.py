"""
3、编程判断俩个链表是否相交
 给出俩个单向链表的头指针，比如h1，h2，判断这俩个链表是否相交。
 为了简化问题，我们假设俩个链表均不带环。

 问题扩展： 如果链表可能有环列? 如果需要求出俩个链表相交的第一个节点列?
"""
class Solution:
    def isCircle(self, list1, list2):
        if not list1 or not list2:
            return False

        # 遍历获取链表长度
        len_A = 0
        while list1:
            len_A += 1
            list1 = list1.next

        len_B = 0
        while list2:
            len_B += 1
            list2 = list2.next

        dif_len = len_A - len_B
        p1 = list1
        p2 = list2

        # 让长的链表走到跟短的链表一样长
        if len_A < len_B:
            dif_len = len_B - len_A
            # 让B先走
            while dif_len:
                p2 = p2.next
                dif_len -= 1
        else:
            while dif_len:
                p1 = p1.next
                dif_len -= 1

        while p1 and p2:
            if p1.next == p2.next:
                return True
        return False

