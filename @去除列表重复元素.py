#写函数，参数为一个list，该函数得到并返回对该list去掉重复元素的新列表（对重复元素，只保留一个）。
#测试用例：[1, 2, 3, 4, 4, 3, 5, 6, 8, 2, 2]
#输出样例：[1,2, 3, 4,5,6,8]


list = [1, 2, 3, 4, 4, 3, 5, 6, 8, 2, 2]
def duplicate(list):
    c = []
    for i in range(len(list)):
        if list[i] not in c:    #请不要遗忘 in / not in ，十分实用！！！
            c.append(list[i])
    return c
print(duplicate(list))