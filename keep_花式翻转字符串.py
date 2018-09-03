"""
Keep 1  花式翻转字符串
输入一个字符串及一个数字k,对字符串从头开始每3*k个子串的前k个进行反转，剩下的字符不变。
如果剩余长度小于k，则将剩下的全部反转；如果字符串长度大于3*k但小于等于k,则反转前k个字符，剩下的字符不变
"""
# AC
def reverseString(s, k):
    if not s or not k:
        return ""
    s = list(s)
    len_s = len(s)

    index = 0
    res = []
    for i in range(int(len_s / (3 * k))):
        res.extend(reverse(s[index: index + 3 * k], k))
        index += 3 * k

    if index < len_s:
        if (len_s - index) < k:
            res.extend(reverse(s[index:], -1))
        elif k < (len_s - index) < 3 * k:
            res.extend(reverse(s[index:], k))
    return "".join(res)


def reverse(s, k):
    if not s or not k:
        return

    left = 0
    if k == -1:
        right = len(s) - 1
    else:
        right = k - 1
    while left <= right:
        tmp = s[left]
        s[left] = s[right]
        s[right] = tmp
        left += 1
        right -= 1
    return s


import sys

for line in sys.stdin:
    a = line.split()
    print(reverseString(str(a[0]), int(a[1])))
# print(reverseString("wer", 2))