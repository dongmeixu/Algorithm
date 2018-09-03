# -*- coding:utf-8 -*-
class Solution:
    data = []

    def Insert(self, num):
        # write code here
        self.data = num

    def GetMedian(self):
        # write code here

        len_ = len(self.data)
        if len_ == 0:
            return None
        elif len_ & 1 == 1:
            return self.data[len_ >> 1]
        else:
            return (self.data[len_ >> 1] + self.data[(len_ >> 1 + 1)]) // 2
