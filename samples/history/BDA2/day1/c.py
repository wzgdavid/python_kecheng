names = ['   tom', ' jack  ',' mary ']
striped_names = []
for name in names:
    striped_names.append(name.strip())
#print(striped_names)

lst = [1,2,3,2,3,2,1,23,4,5]
lst2 = []
for n in lst:
    if n not in lst2:
        lst2.append(n)
print(lst2)