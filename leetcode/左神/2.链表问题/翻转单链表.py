# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class ReverseSingleList:
#     def reverse(self, head):
#         pre = None
#
#         while head:
#             pnext = head.next
#             head.next = pre
#             pre = head
#             head = pnext
#         return pre
#
#
# ll = list(map(int, input().split()))
# head = p = ListNode(ll[0])
# for x in ll[1:]:
#     p.next = ListNode(x)
# print(ReverseSingleList().reverse(head).val)


# -*- coding:utf-8 -*-
class Different:
    # def checkDifferent(self, iniString):
    #     # write code here
    #     if not iniString:
    #         return True
    #     hash_map = {}
    #     for tmp in iniString:
    #         hash_map[tmp] = hash_map.get(tmp, 0) + 1
    #
    #     for key, value in hash_map.items():
    #         if value > 1:
    #             return False
    #     return True

    def checkDifferent(self, iniString):
        # write code here
        if not iniString:
            return True
        for i in range(len(iniString)):
            for j in range(i + 1, len(iniString)):
                if iniString[i] == iniString[j]:
                    return False
        return True


s = "ahfvf"
print(Different().checkDifferent(s))
print(Different().checkDifferent_1(s))
