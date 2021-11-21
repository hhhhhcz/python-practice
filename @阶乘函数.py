#写函数factorial，该函数有1个参数（正整数），功能是计算该整数的阶乘，
#要求用for循环。主程序测试：键盘读入三个正整数m,n,k，以其分别作为参数来调用函数，并打印 m!+n!+k!的值。
#测试用例：6, 7, 8（读入时分行读入，每个一行，并无逗号）
#输出样例：SUM = 46080

def factorial(num):
    s = 1
    for i in range(1,num+1):
        s *= i
    return s

def main():
    m = int(input('输入一个正整数：'))
    n = int(input('输入一个正整数：'))
    k = int(input('输入一个正整数：'))
    print(factorial(m)+factorial(n)+factorial(k))
main()