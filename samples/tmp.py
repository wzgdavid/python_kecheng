import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(10,size=(6,4)), index=list('abcdef'), columns=list('ABCD'))

print(df)

df.ix[5,1] = 99

print(df)

print(df.sum())