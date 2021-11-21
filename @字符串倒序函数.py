#自己定义一个reverse(s)函数，功能返回字符串s的倒序字符串。
s = 'weiyidezhuhuo'
def reverse(s):
    c = []
    v = ''
    for i in range(1,len(s)+1):
        c.append(s[-i])
    for i in range(len(c)):
        v += c[i]
    return v
print(reverse(s))