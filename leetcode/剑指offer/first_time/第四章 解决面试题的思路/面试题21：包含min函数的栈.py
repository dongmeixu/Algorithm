# coding=utf-8
"""
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数
"""


# 思路：构建2个栈，数据栈（存放数据） + 辅助栈（存放每次的最小值）
# 利用辅助栈来保存每一步的最小值，时间复杂度为O(n)，空间复杂度O(n);
# 1.先压入数据栈
# 2.然后比较当前的数跟辅助栈栈顶元素，哪个小哪个压入辅助栈

class Solution:
    m_data = []  # 数据栈
    m_min = []  # 辅助栈

    def push(self, node):
        # write code here
        self.m_data.append(node)  # 直接加入数据栈
        if len(self.m_min) == 0 or node < self.m_min[-1]:  # 当辅助栈中没有元素或者新加入的元素小于辅助栈栈顶元素
            self.m_min.append(node)  # 将该元素压入辅助栈
        else:  # 否则，直接将辅助栈栈顶元素再次加入
            self.m_min.append(self.m_min[-1])

    def pop(self):
        # write code here
        if len(self.m_data) > 0 and len(self.m_min) > 0:
            self.m_data.pop(-1)
            self.m_min.pop(-1)

    def top(self):
        # write code here
        return self.m_min[-1]  # 辅助栈栈顶元素

    def min(self):
        # write code here
        if len(self.m_data) > 0 and len(self.m_min) > 0:
            print(self.top())  # 输出辅助栈栈顶元素（栈顶元素即是最小值）
            return self.top()


# ["PSH3","MIN","PSH4","MIN","PSH2","MIN","PSH3","MIN","POP","MIN","POP","MIN","POP","MIN","PSH0","MIN"]
s = Solution()
s.push(3)
s.min()
s.push(4)
s.min()
s.push(2)
s.min()
s.push(3)
s.min()
s.pop()
s.min()
s.pop()
s.min()
s.pop()
s.min()
s.push(0)
s.min()

print(min)
