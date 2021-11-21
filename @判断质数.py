#课堂练习：
# 判断任意一个正整数是否是质数：
#        即是否只能被1整除
num = int(input('请输入一个正整数：'))
for i in range(2,num):
    if num%i == 0:
        print('不是质数！')
        break
else:
    print('是质数！！！！！！！！')

#for-else循环
#while-else循环