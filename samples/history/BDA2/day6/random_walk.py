import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a = np.random.randint(2, size=10000) # [0,1,.....]
a2 = np.where(a==0,-1,a)   # [1,-1 ......]
#print(a2)
walks = a2.cumsum()
plt.plot(walks)
#plt.show()

users = pd.read_csv(r'users.csv')
