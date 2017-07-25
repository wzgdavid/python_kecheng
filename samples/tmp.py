import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'csv\Pokemon.csv')

df.columns = df.columns.str.upper()

df = df.set_index('NAME')

df = df.drop('#', axis=1)
#print(df.head())

pikachu = df.loc['Pikachu']
#print(pikachu)

types1 = df['TYPE 1'].unique()
types2 = df['TYPE 2'].unique()
#print(types1, types2)

#select = ((df['TYPE 1']=='Rock') & (df['TYPE 2']=='Dragon')) | ((df['TYPE 1']=='Dragon') & (df['TYPE 2']=='Rock'))
#print(df[select])

#print(df.HP.max(), df.HP.idxmax())


typefire = df[(df['TYPE 1'] == 'Fire') | (df['TYPE 2'] == 'Fire')]
#print(typefire.ATTACK.idxmax())
#
#print(typefire.sort_values('ATTACK', ascending=False).head(3))

type1 = df['TYPE 1'].value_counts()
type2 = df['TYPE 2'].value_counts()

typecount = (type1+type2).sort_values(ascending=False)


bugsum = ((df['TYPE 1']=='Bug') | (df['TYPE 2']=='Bug')).sum()



strong = df.sort_values(by='TOTAL', ascending=False)
strong = strong.drop_duplicates(subset=['TYPE 1'],keep='first')
#print(strong)

# type 1 和type2 合并
df1 = df.drop('TYPE 2', axis=1)
df1['TYPE'] = df['TYPE 1']
df2 = df.drop('TYPE 1', axis=1).dropna()
df2['TYPE'] = df['TYPE 2']
dft = pd.concat([df1, df2]).drop(['TYPE 1', 'TYPE 2'], axis=1)
strong = dft.sort_values(by='TOTAL', ascending=False)
strong = strong.drop_duplicates(subset=['TYPE'],keep='first')
print(strong)
'HP'
