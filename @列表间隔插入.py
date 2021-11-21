#写函数，可将两个相同长度的list，间隔插入，生成并返回一个新的list。
#例如：给两个list，a=[1,2,3,4], b=[5,6,7,8]。则可以生成：[1,5,2,6,3,7,4,8]。
b1 = [5,6,7,8]
a1 = [1,2,3,4]
def kong(a,b):    
    c = []
    for i in range(len(a)):
        c.append(a[i])
        c.append(b[i])
    return c
print(kong(a1,b1))