#给定字母与摩尔斯电码的对照表morse，将用摩尔斯电码编写的一段文字code翻译成明文。其中：
#code中字母的编码之间用符号/间隔，明文不需要输出符号/。
#morse中的A.-表示：A的摩尔斯编码为.-。注意，其中有个空格的morse编码。
#测试用例：
#code = '.-../---/...-/./-....-/-././...-/./.-./-....-/..-./.-/../.-../.../'
"""
morse = '''
A.-
B-...
C-.-.
D-..
E.
F..-.
G--.
H....
I..
J.---
K-.-
L.-..
M--
N-.
O---
P.--
Q--.-
R.-.
S...
T-
U..-
V...-
W.--
X-..-
Y-.--
Z--..
 -....-
'''
"""
def decodeMorse(inp):
    #这是从ppt中复制的，等下周学了文件读写，你们就舒服了
    morse = '''
A.-
B-...
C-.-.
D-..
E.
F..-.
G--.
H....
I..
J.---
K-.-
L.-..
M--
N-.
O---
P.--
Q--.-
R.-.
S...
T-
U..-
V...-
W.--
X-..-
Y-.--
Z--..
 -....-
'''
    #把摩尔斯电码表拆分成列表，letter-code-pairs=lcps
    lcps=morse.split('\n')
    
    #把摩尔斯电码表变成成员为列表的列表，内层列表为[字母,代码]
    letters=[]
    for i in lcps:
        if i: #split可能会产生空字符串，因此要加判断，只对有内容的进行操作
            letters.append([i[0],i[1:]])#运用字符串切片构造内层列表
    
    #把输入的电报用斜杠为标记拆分成字母代码
    res=''
    codes=inp.split('/')
    for i in codes:
        for j in range(len(letters)):
            if i==letters[j][1]: #第1号元素是代码
                res+=letters[j][0] #第0号元素是字母
            
    return res

#主程序
inp='.-../---/...-/./-....-/-././...-/./.-./-....-/..-./.-/../.-../.../'
print(decodeMorse(inp))