urls = [
    'https://www.zhihu.com/question/2355645',
    'http://python.org/question/2355645'
]

#print(urls[0].split('/')[2])

#for url in urls:
#    print(url.split('/')[2])

names = ['   tom', 'jack   ', 'mary  ', ' jerry']
new_names = []
for name in names:
    name1 = name.strip()
    new_names.append(name1)
#print(new_names)

# 列表去重
lst = [1,2,3,3,2,2,13,4,5,6,6]
lst2 = []
for n in lst:
    if n not in lst2:
        lst2.append(n)
#print(lst2)

lst =[[],[],[]]
lst =[[10,20],[10,20],[10,20],[30]]



lst = [7, 4,3,5,1]
lst2 = [5, 9,7,8]


from operator import itemgetter
z = list(zip(lst, lst2))
#print(sorted(z, key=itemgetter(0)))
#print(sorted(z, reverse=True, key=itemgetter(1)))
#z.sort(key=itemgetter(1))
#print(z) # [(7, 5), (3, 7), (5, 8), (4, 9)]

# func的作用是取得序列下标为0的元素
func = itemgetter(1)
#print(func([8,9]))
#print(func)


lst0 = [1,2,3,4,5,6]
lst = []
for n in lst0:
    lst.append(n*n)
#print(lst)
# 列表生成式  
lst = [n*n for n in lst0]
lst = [n*n for n in lst0 if n%2==1]
lst = [n*n if n%2==1 else str(n) for n in lst0]
lst = ['{}*{}={}'.format(i,j,i*j) for i in range(1,3) for j in range(2,4)]
print(lst)

# 把前面的练习改成列表生成式
new_names = [name.strip() for name in names]
#print(new_names)
