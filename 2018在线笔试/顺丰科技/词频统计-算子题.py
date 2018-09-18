import operator

string = input()

word_list = list(string.lower().split(" "))
# print(word_list)

hash_map = {}
for tmp in word_list:
    if tmp != "":
        hash_map[tmp] = hash_map.get(tmp, 0) + 1
sorted_x = sorted(hash_map.items(), key=operator.itemgetter(1), reverse=True)
# res = list(hash_map.items())
# print(res)
# res.sort(key=lambda x: res[1])
print(sorted_x)





# 1.删除原数组中重复出现三次的元素
# 2.快速判断一个数是否是2的幂次方，并求出是多少次幂
# 3.堆排
# 4.连续子数组的最大和
# 5.百万数中找最大的10个数
# 6.找出第一个不重复的数字
# 7.快排
# 8.链表是否有环
# 9.python内存管理机制
# 10.约瑟夫环
# 11.链表翻转
# 12.最大公约数和最小公倍数