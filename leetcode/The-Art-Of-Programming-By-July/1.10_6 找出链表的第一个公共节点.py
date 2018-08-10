"""

6、找出链表的第一个公共结点
两个单向链表，找出它们的第一个公共结点。

"""

class Solution:
    def isCircle(self, list1, list2):
        if not list1 or not list2:
            return -1

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
                return p1
        return -1

