"""
题目描述：
对于仅由小写字母组成的字符串A和B，如果分别存在一个小写字母a到z的排列，使得将A中所有字母a替换为排列的第一个字母，所有字母b替换为排列的第二个字母……所有字母z替换为排列的最后一个字母之后，A和B完全相同，那么称字符串A和B相似，如abcc和xyaa。现在给定仅由小写字母组成且长度不超过105的字符串S和T，求S中有多少子串与T相似？
"""
S = input()
T = input()
l = 0
t_len = len(T)
r = t_len
similar_t = [T]
res = 0
while r <= len(S):
    sub_s = S[l:r]
    if sub_s in similar_t:
        res += 1
    else:
        replace_dict = {}
        error = False
        for i in range(t_len):
            if T[i] not in replace_dict:
                replace_dict[T[i]] = sub_s[i]
            elif T[i] in replace_dict and replace_dict[T[i]] != sub_s[i]:
                error = True
                break
        if not error:
            res += 1
            similar_t.append(sub_s)
    r += 1
    l += 1
print(res)