#编写函数lc，实现正整数n到m的连乘（用户输入m和n，且m>n）
#并计算lc(1,50)+lc(2,50)+lc(3,50)...lc(49,50)的结果。

def lc(m,n):
    s = 1
    for i in range(n-m+1):
        s *= (m+i)
    return s

v = 0
for i in range(1,50):
    v += lc(i,50)
print(v)