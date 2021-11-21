#写函数，可求两个数值向量的相似度，计算结果保留4位小数，向量可放在list中。主程序调用该函数。
#测试用例：[1,2,3,4,5]   [5,4,3,2,1]
#样例输出：0.6364

a = [1,2,3,4,5]
b = [5,4,3,2,1]

def similar(a,b):
    v = a1 = b1 = 0
    for i in range(len(a)):
        v += (a[i]*b[i])
        a1 += a[i]**2
        b1 += b[i]**2
    similarity = v/((a1**0.5)*(b1**0.5))
    return similarity

print(similar(a,b))