import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# generation比例饼图
# 1 2 3 4 5 6
# 1 2 3 other

df = pd.read_csv(r'E:\python_files\csv\Pokemon.csv')
# 列名都改为小写
df.columns = df.columns.str.lower()

#counts = df.generation.value_counts()
#counts = counts.sort_index()
#plt.pie(
#        counts.values,
#        explode=(0.1,0,0,0,0,0),
#        autopct='%1.1f%%',
#        labels=counts.index
#    )
#plt.axis('equal')
#plt.show()


# 1 2 3 other
counts = df.generation.value_counts()
counts = counts.sort_index()

counts['other'] = counts[3:].sum()
#print(counts)
counts = counts[[1,2,3,'other']]
#print(counts)
plt.pie(
        counts.values,        
        autopct='%1.1f%%',
        labels=counts.index
    )
plt.axis('equal')
#plt.show()



# 读取51job.csv
# 1 哪个城市平均月薪
# 2 上海各学历的平均月薪
# 3 黄金价格每天变化的范围分布
#names = ['job', 'link','company','place','salary','exp','xueli']
df = pd.read_csv(r'E:\python_files\csv\51jobs.csv',
            encoding='gbk',
            #names=names
            )

print(df.head())