lst = ['bart', 123, None, 'lisa', 'adam']
#for n in lst:
#    if isinstance(n, str):
#        #print('Hello '+n+' !')
#        #print('hello %s !' % n)
#        print('hello {} !'.format(n))

s = 'abcde, A a '
print(s.lower()) # 
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
for n in s.lower():
    if n == 'a': # 这里判断可以用is
        count_a += 1
    elif n == 'e': # 这里判断可以用is
        count_e += 1
    elif n == 'i': # 这里判断可以用is
        count_i += 1
    elif n == 'o': # 这里判断可以用is
        count_o += 1
    elif n == 'u': # 这里判断可以用is
        count_u += 1

#print('这里有{}个{}'.format(count_a, 'a') )
#print('这里有{}个{}'.format(count_e, 'e') )
#print('这里有{}个{}'.format(count_i, 'i') )
#print('这里有{}个{}'.format(count_o, 'o') )
#print('这里有{}个{}'.format(count_u, 'u') )


for i in range(1, 10):
    for j in range(1, i+1):
        #print(i,j)
        #print('{}*{}={}'.format(j,i,j*i).center(9), end='')
        print('{}*{}={}'.format(j,i,j*i), end='\t')
    print('')  

# 伪代码
id   name  age
students = [row0, row1, row2,1111]
insert into table values (1, 'tom', 78)
insert into table values (2, 'cat', 90)
...
...
for row in students:
    sql = "insert into table values ({}, {}, {})".format(row[0], row[1], row[2])
    mysql.execute(sql)
    commite