import numpy as np
import pandas as pd

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                        'foo', 'bar', 'foo', 'foo'],
                    'B' : ['one', 'one', 'two', 'three',
                        'two', 'two', 'one', 'three'],
                    'C' : np.random.randint(8,size=8),
                    'D' : np.random.randint(8,size=8)})

print(df)