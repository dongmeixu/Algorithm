"""
题目描述：在英语中，如果两个单词中出现的字母相同，并且每个字母出现的次数也相同，
    那么这两个单词互为变位词（Anagram）.
    例如silent与listen、evil与live等互为变位词。
    请完成一个函数，判断输入的两个字符串是不是互为变位词。


思路：
    我们可以创建一个用数组实现的简单哈希表，用来统计字符串中每个字符出现的次数。
    当扫描到第一个字符串中的每个字符时，为哈希表对应的项的值增加1.
    接下来扫描第二个字符串，扫描到每个字符时，为哈希表对应的项的值减去1.
    如果扫描完第二个字符串后，哈希表中所有的值都是0，那么这两个字符串就互为变位词
"""

def changeWord(s1, s2):
    dict = {}
    tag = True
    for i in s1:
        dict[i] = dict.get(i, 0) + 1
    for j in s2:
        dict[j] = dict.get(j, 0) - 1

    for value in dict.values():
        if value != 0:
            tag = False
            break

    # print(list(dict.values()))
    return tag


s1 = 'evil'
s2 = 'live'

print(changeWord(s1, s2))