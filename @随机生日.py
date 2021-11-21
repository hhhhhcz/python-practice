#课堂练习：
#随机产生整数，19000101-25000101，看第几次能碰到你的生日（如20011203），并显示出这是第几个随机数
import random
i = 0
bir = 20030309
while True:
    n = random.randint(19000101,25000101)
    if n == bir:
        print('这是第',i,'次随机。')
        break
    else:
        i += 1