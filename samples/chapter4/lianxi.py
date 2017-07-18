'''
 去掉names中元素两边的空格并生成一个新的list

 '''
names = ['   Tom', '   Jack   ', 'Mary', 'Jerry     ']


striped_names = []
for name in names:
    striped_names.append(name.strip())
print(striped_names)

# 不用strip
striped_names = []
for name in names:
    striped_name = ''
    for c in name:
        if not c is ' ': 
            striped_name += c
    striped_names.append(striped_name)
print(striped_names)
'''
 统计一段英文文本中有多少不同的单词（不区分大小写，以空格分隔）

'''
text = '''
This library reference manual describes the standard library 
that is distributed with Python. It also describes some of 
the optional components that are commonly included in 
Python distributions.
'''
text_lowered = text.lower()
text_lst = text_lowered.split()
result = []
for word in text_lst:
    if word in result:
        continue
    result.append(word)
print(result)
print(len(result))

'''
练习：生成一个99乘法表的列表，
输出类似['1*1=1', '1*2=2', '1*3=3', '1*4=4', '1*5=5', '1*6=6', '1*7=7', '1*8=8', '1*9=9', '2*2=4', '2*3=6', '2*4=8', '2*5=10', '2*6=12', '2*7=14', '2*8=16', '2*9=18', '3*3=9', '3*4=12', '3*5=15', '3*6=18', '3*7=21', '3*8=24', '3*9=27', '4*4=16', '4*5=20', '4*6=24', '4*7=28', '4*8=32', '4*9=36', '5*5=25', '5*6=30', '5*7=35', '5*8=40', '5*9=45', '6*6=36', '6*7=42', '6*8=48', '6*9=54', '7*7=49', '7*8=56', '7*9=63', '8*8=64', '8*9=72', '9*9=81']
提示，先不考虑结构，只输出结果[1, 2, 3 …..72, 81]

'''
a = ['{}*{}={}'.format(m,n, m*n) for m in range(1, 10) for n in range(m, 10)]
print(a)


for i in range(1,10):  #循环9次，打印出9行
    for j in range(1,i+1):  #第几行就有几项
        s = '{}*{}={}'.format(j, i, i*j)
        print(s.center(8), end='')
    print('')  #每循环1次就打印1个空格，默认回车折行
