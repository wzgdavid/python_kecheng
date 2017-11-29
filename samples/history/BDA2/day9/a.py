import random
import pickle



lst = [1,2,3,4,666]
# 数据持久化
with open('lst.pickle', 'wb') as f:
    pickle.dump(lst, f)

# 读取持久化的pickle对象
with open('lst.pickle', 'rb') as f:
    lst2 = pickle.load(f)
print(lst2)


print(random.choice(lst))