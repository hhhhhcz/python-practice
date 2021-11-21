#写函数，根据给定符号和行数，打印相应直角三角形(四种，上下左右角直角)，等腰三角形（2种）。
#symble = input('给个符号：')
#line = int(input('给个行数：'))
symble = '@'
line = 3


for i in range(line):
    print(symble*(i+1))

for i in range(line):
    print(symble*(line-i))

for i in range(1,line+1):
    print(' '*(line-i),symble*(i),sep='')

for i in range(line+1):
    print(' '*(i),symble*(line-i),sep='')

for i in range(1,line+1):
    print(' '*(-i+line),symble*(2*i-1),sep='')

for i in range(1,line+1):
    print(' '*(i-1),symble*(-2*i+7),sep='')