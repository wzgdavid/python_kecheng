import json
dct = {}
dct = {'name':'tom', 'score':99}
dct = dict() # dict dct = new dict()
dct = dict(name='tom', score=99) # 和第三行等价
# 参数是一个列表
dct = dict( [('name', 'tom'), ('score', 99)] )
#print(dct)

names = ['aa', 'bb', 'ccc']
scores = [98, 56, 34]
# 利用zip构造字典数据
name_score = dict(zip(names, scores))
#print(name_score)

dct['name'] # 
dct['name'] = 'jack' # 赋值

# json示例
#dct_json = json.dumps(dct)
#print(dct_json, type(dct_json))
#dct2 = json.loads(dct_json)
#print(dct2, type(dct2))

dct['age'] = 90
# update 更新dct
dct.update( {'name':'zoo', 'score': 50, 'gender':'M', 'salary':999} )
print(dct)

dct2 = dict.fromkeys(dct.keys())
#print(dct.values())
#print(dct2)
#print(dct['salary'])
#print(dct.get('salary',2000))
#print(dct.pop('name'))
#del dct['name']
#print(dct)

print('name' in dct)

