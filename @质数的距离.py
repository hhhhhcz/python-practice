#质数的距离（50分） 
#写（多个）函数，用列表记录小于n的所有相邻质数之间的距离。
#如3和5之间的距离是2。5和7之间的距离也是2。7和11之间是4。本题规定第一个质数为3。主程序令n为1000进行测试。 

#a 计算小于n的所有质数，并输出。（15分） 
#b 计算所有质数之间的距离，装入列表并输出。（12分） 
#c 不使用Python内置函数，计算这些距离的最大值、最小值、平均距离和距离方差。（12分） 
#d 计算超过平均值的距离的个数。（11分）

def findPrimes(n):
    res=[]
    for i in range(3,n):
        if isPrime(i)==True:
            res.append(i)
    return res

def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def calDist(p):
    res=[]
    for i in range(1,len(p)):
        res.append(p[i]-p[i-1])
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

def countSupr(pd):
    res=0
    ave=findAve(pd)
    for i in pd:
        if i>ave:
            res+=1
    return res

#a问
print(findPrimes(int(input('请输入寻找质数的范围！'))))

#b问
print(calDist(findPrimes(int(input('请输入寻找质数的范围！')))))

#c问
pd=calDist(findPrimes(int(input('请输入寻找质数的范围！'))))
print(findMax(pd),findMin(pd),findAve(pd),findVar(pd))

#d问
print(countSupr(pd))