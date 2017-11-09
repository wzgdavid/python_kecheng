import numpy as np

times = 99999
touzi = np.random.randint(1,7, size = (2,times))
print(touzi)

print((touzi[0]==touzi[1]).sum())

a = ((touzi[0]==touzi[1]) & (touzi[1]==6)).sum()
eq = touzi[0]==touzi[1]
eq6 = touzi[1]==6
dui6 = (eq & eq6).sum()
print(dui6)
gt10 = ((touzi[0]+touzi[1])>10).sum()
print(gt10)