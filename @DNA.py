#DNA 链条由A、G、C、T四种碱基构成。
#已知规则A总与T形成氢键构成碱基对（反之亦然），而C总与G形成氢键构成碱基对（反之亦然）。 
#a.生成一个列表，模拟一条 DNA 链，含有120个随机的碱基符号（A、G、C、T）。并输出另一条与之配对的链条。（15分）
#b.写函数，用户可以指定DNA链条的长度，形成随机链条和它的配对链条，并输出其中的ACGT各自的数量。（25分） 

import random
def dna(a):
    d=[]
    b=[]
    a,g,c,t=0,0,0,0
    for j in range(120):
        a.append(random.choice("ATCG"))
    for i in a:
        if i=="A":
            b.append("T")
            a+=1
        elif i=="T":
            b.append("A")
            t+=1
        elif i=="C":
            b.append("G")
            c+=1
        else:
            b.append("C")
            g+=1
    return d,b,a,g,c,t
print(dna())