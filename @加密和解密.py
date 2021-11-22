#加密和解密（50分） 
#对数字串（如密码）进行加密的最简单方法是将每一个数字用一个更大的随机数字来替换。
# 已知列表mingwen=[1,4,0,3,0,2,6,4]。
# 替换规则是将每一位数n替换为[100n,100n+100)区间内的随机正整数。如1被替换为[100,200)范围内随机正整数。

#a 请将mingwen的内容进行加密，并赋值给列表mima，并将mima输出在屏幕上。（15分） 
#b 不使用Python内置函数，计算这些mima中数值的最大值、最小值、平均值和方差。（16分）
#c 编写函数，输入一个成员为正整数的列表，输出为解密后的列表。并以mima为输入，进行调用。（19分）  

import random

def myEncode(ming):
    res=[]
    for i in ming:
        res.append(100*i+random.randint(0,99))
    return res

def findMax(pd):
    res=pd[0]
    for i in pd:
        if i>res:
            res=i
    return res

def findMin(pd):
    res=pd[0]
    for i in pd:
        if i<res:
            res=i
    return res

def findAve(pd):
    res=0
    for i in pd:
        res+=i
    return res/len(pd)

def findVar(pd):
    res=0
    ave=findAve(pd)
    for i in pd:
        res+=(i-ave)**2
    return res/len(pd)

def myDecode(mi):
    res=[]
    for i in mi:
        res.append(i//100)
    return res
#a问
mingwen=[1,4,0,3,0,2,6,4]
miwen=myEncode(mingwen)
print(miwen)

#b问
print(findMax(miwen),findMin(miwen),findAve(miwen),findVar(miwen))

#c问
print(myDecode(miwen))