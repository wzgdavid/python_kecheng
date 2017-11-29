from copy import copy, deepcopy

lst = [[1, 2], 3, 4]
lst_copy = copy(lst)
lst_deepcopy = deepcopy(lst)
lst[0].append(3)

#print(lst_copy)
#print(lst_deepcopy)

class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score
    #def __repr__(self):
    #    return '{}: {}'.format(self.name, self.score)
    def __str__(self):
        return '{}-{}'.format(self.name, self.score)


s = Student('tom', 99)
s1 = Student('jack', 67)
s2 = Student('jerry', 88)
lst = [s, s1, s2]

print(sorted(lst, key=lambda student:student.score))
print(str(s))

#map()
lst2 = [1,-22,-3,4]
def poo(n):
    return n*n

#help(map)
print(list(map(poo, lst2)))
print(list(map(abs, lst2)))
print([abs(n) for n in lst2])
#[n*n for n in lst2]
def get_score(student):
    return student.score

for score in map(get_score, lst):
    print(score)