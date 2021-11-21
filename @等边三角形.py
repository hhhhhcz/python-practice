#课堂练习：
#输出*构成的等边三角形，高度（层数）由用户控制
line = int(input('请输入行数：'))
symble = '*'
for i in range(1,line+1):
    print(' '*(-i+line),symble*(2*i-1),sep='')