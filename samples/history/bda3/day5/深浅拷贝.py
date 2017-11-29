from copy import copy, deepcopy

class Person():
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

p1 = Person('cat', [98,70,67])
p1_copy = copy(p1)
p1_deepcopy = deepcopy(p1)
print(p1)
print(p1_copy) # p1 is p1_copy  false

print(id(p1.scores), '原来的scores id')
print(id(p1_copy.scores), '浅拷贝 id')
print(id(p1_deepcopy.scores), '深拷贝')

p1.scores.append(99)
print(p1.scores, '原来的scores')
print(p1_copy.scores, '浅拷贝')
print(p1_deepcopy.scores, '深拷贝')