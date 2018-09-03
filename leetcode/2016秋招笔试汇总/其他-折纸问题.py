"""
题目描述
请把纸条竖着放在桌⼦上，然后从纸条的下边向上⽅对折，压出折痕后再展 开。此时有1条折痕，突起的⽅向指向纸条的背⾯，这条折痕叫做“下”折痕 ；突起的⽅向指向纸条正⾯的折痕叫做“上”折痕。如果每次都从下边向上⽅ 对折，对折N次。请从上到下计算出所有折痕的⽅向。

给定折的次数n,请返回从上到下的折痕的数组，若为下折痕则对应元素为"down",若为上折痕则为"up".

测试样例：
1
返回：["down"]
"""


# -*- coding:utf-8 -*-
"""
考察的是二叉树的中序遍历，可以试着折两下子，发现每一次折都会在最新的折痕上下位置出现两个新的折痕，一上一下，上为down，下为up。打印的时候，从上往下打印，类似于二叉树的中序遍历。
"""
class FoldPaper:
    def foldPaper(self, n):
        # write code here
        res = []
        if n <= 0:
            return res
        self.inOrder(n, "left", res)
        return res

    def inOrder(self, n, position, res):
        # 递归截止条件
        if n == 0:
            return
        # 递归过程
        self.inOrder(n - 1, "left", res)
        if position == "left":
            res.append("down")
        else:
            res.append("up")
        self.inOrder(n - 1, "right", res)


print(FoldPaper().foldPaper(-1))
