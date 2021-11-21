#编写一个累加计算器，用户输入起始加数和终止加数，可以获得累加结果，并且一次启动多次使用。

m = int(input('输入起始加数：'))
n = int(input('输入终止加数：'))
s = n - m 
i = v = 0
while True:
    if i > s:  #用s避免m的变化影响
        print(v)
        break
    else:
        v += (m+i) #用v储存累加值
        i += 1