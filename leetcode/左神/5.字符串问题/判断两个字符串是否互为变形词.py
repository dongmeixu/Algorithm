"""
判断给定两个字符串是够互为变形词

给定两个字符串str1和str2，
如果str1 和str2中出现的字符种类一样且每种字符出现的次数也一样，
那么str1
"""
def isDeformation(str1, str2):
    if not str1 or not str2 or len(str1) != len(str2):
        return False

    hash_map = {}
    for tmp in str1:
        hash_map[tmp] = hash_map.get(tmp, 0) + 1

    for tmp in str2:
        if tmp not in hash_map.keys():
            return False

        hash_map[tmp] -= 1
        if hash_map[tmp] < 0:
            return False
    return True


str1 = "123"
str2 = "324"
print(isDeformation(str1, str2))
