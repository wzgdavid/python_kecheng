#sum_ = 0 # [1, 100]
#a = 100
#while a>0:   # while a:  
#    if a %2 == 0:
#        sum_ += a 
#    a -= 1
#print(sum_)
#
#
#a = 100
#sum_2 = 0
#while a>0:   # while a:  
#    if a %2 == 1:
#        break
#    sum_2 += a 
#    a -= 1
#
#print(sum_2)#
#

lst = [1, 2, 3, 4, 5, None, 'shasd', None]
for num in lst: 
    if isinstance(num, int):
        print(num+1)
    #elif isinstance(num, str): # 看你怎么处理
    #    print(str(1)+num) # '1'
    else:
        print('非数字不处理')
        pass

sum_ = 0
r = range(1, 101)
for n in range(2, 101, 2):
    
    sum_ += n
   
print(sum_)