"""
给定一个字符串str,求其中全部数字串所代表的数字之和
"""


def numSum(strnum):
    if not strnum:
        return -1

    tag = 0
    res = 0
    for tmp in strnum:
        if tmp == "-":
            tag += 1
        elif "0" < tmp < "9":
            if tag % 2 == 0:  # 偶数，则为正
                res += int(tmp)
            else:
                res -= int(tmp)
            tag = 0
        else:
            pass
    return res


# strs = "A1CD2E33"
strs = "A-1B--2C--D6E"
print(numSum(strs))
