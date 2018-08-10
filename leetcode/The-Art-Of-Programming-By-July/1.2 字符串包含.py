"""
题目描述
给定两个分别由字母组成的字符串A和字符串B，字符串B的长度比字符串A短。请问，如何最快地判断字符串B中所有字母是否都在字符串A里？
为了简单起见，我们规定输入的字符串只包含大写英文字母，请实现函数bool StringContains(string &A, string &B)
比如，如果是下面两个字符串：
String 1：ABCD
String 2：BAD
答案是true，即String2里的字母在String1里也都有，或者说String2是String1的真子集。
"""


class Solution:
    # 解法1：暴力解法 O(n*m)
    # 判断string2中的字符是否在string1中?最直观也是最简单的思路是，针对string2中每一个字符，逐个与string1中每个字符比较，看它是否在String1中。
    def StringContain(self, a, b):
        if not a or not b:
            return False

        a = list(a)
        b = list(b)

        len_a = len(a)
        len_b = len(b)
        assert len_a > len_b

        for tmp in b:
            if tmp not in a:
                return False
        return True

    # 解法2：如果允许排序的话，我们可以考虑下排序。
    # 比如可先对这两个字符串的字母进行排序，然后再同时对两个字串依次轮询。
    # 两个字串的排序需要(常规情况)O(m log m) + O(n log n)次操作，之后的线性扫描需要O(m+n)次操作
    def StringContain_1(self, a, b):
        if not a or not b:
            return False

        a = list(a)
        b = list(b)

        len_a = len(a)
        len_b = len(b)
        assert len_a > len_b

        # 对其排序
        a.sort()
        b.sort()

        pa = pb = 0
        while pb < len_b:
            while pa < len_a and a[pa] < b[pb]:  # 在a中找到第一个跟b首字母一样的元素
                pa += 1

            if pa >= len_a or a[pa] > b[pb]:
                return False

            # 当前位置的元素值相等，则继续比较
            pb += 1

        for tmp in b:
            if tmp not in a:
                return False
        return True


print(Solution().StringContain_1("abcd", "acd"))
