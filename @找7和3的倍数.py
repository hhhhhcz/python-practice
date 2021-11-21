#输出任意正整数范围内（用户指定大于7的上下界）的7和3的倍数
m = int(input('输入下界（大于7）：'))
n = int(input('输入上界：'))
c = []
v = []
while n > m:
    if n % 7 == 0:
        c.append(n)
    if n % 3 == 0:
        v.append(n)
    n -= 1
print('7的倍数有：',c,'\n3的倍数有：',v)