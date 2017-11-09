#1， 去掉names中元素两边的空格并生成一个新的列表
names = ['   Tom', '   Jack   ', 'Mary', 'Jerry     ']
#不用strip方法
new_names = list()
for name in names:
    #stridped_name = name.strip()
    stridped_name = ''
    for n in name:
        if n != ' ':
           stridped_name += n 
    new_names.append(stridped_name)
print(new_names)

lst = [3, 7, [0, [9, 5], 7], 1]
#lst2 = [3, 7, 0, 9, 5, 7, 1] # 扁平化处理
# 'abc-efg-'.replace('-','+')
import re

lst_str = str(lst) # 字符串形式‘[3, 7, [0, [9, 5], 7], 1]’
#lst_str2 = lst_str.replace(']', '').replace('[', '')
lst_str2 = re.sub(r'[\[\]]', '', lst_str)
splited_lst = lst_str2.split(',') # 返回列表
lst2 = [int(n) for n in splited_lst]
print(lst2)


