page5 pandas
pandas是python下最强大的数据分析工具
支持类似于SQL的数据增、删、改、查
支持时间序列分析功能
灵活处理缺失数据
pandas安装
    linux直接安装，windows下先安装wheel，然后去
    http://www.lfd.uci.edu/~gohlke/pythonlibs/
    下载对应版本pandas的whl文件，然后本地安装whl

page6 pandas数据结构
pandas有两个主要数据结构：Series和DataFrame
Series是一种类似于一维数组的对象，它由一组值（numpy数据类型）和一组索引（index）组成
s = pd.Series([1, 4, 7, -5])  # 创建一个最简单Series
s.values     # array([ 1,  4,  7, -5], dtype=int64
s.index         # RangeIndex(start=0, stop=4, step=1)
s = pd.Series([1, 4, 7,-5], index=['b','c','a','d']) # 给定一个索引
s['a']      # 通过索引选取一个值
s['c'] = 9   # 赋值
s[['a','b']]   # 选取一组值

page7 series
Numpy数组运算（如根据布尔型数组进行过滤、标量运算、np函数等）都会保留索引和值之间的链接
s = pd.Series([1, 4, 7,-5], index=['b','c','a','d'])
s[s>1]   # 过滤数据
s * 2     # 标量乘法
np.sqrt(s)    # 平方根
可以像字典一样检查索引
'a' in s
可以通过字典创建Series
phone = {'tom':123, 'bob':444, 'dog': 789}
s = Series(phone)

page8 series
索引就地修改
s.index = ['jerry', 'cat', 'jeff']
Series对象本身及其索引都有name属性
s.name = 'phone'
s.index.name = 'name'
NaN，pandas中用于表示缺失值
phone = {'tom':123, 'bob':444, 'dog': None}
s = Series(phone)
s.isnull() 或 pd.isnull(s)    # 检测NaN值
s.notnull() 或 pd.notnull(s)  # 检测NaN值

page9 DataFrame
DataFrame是一个表格型的数据结构
通过numpy数组创建dataframe
df = pd.DataFrame(np.random.randn(6,4))
可以指定index和columns
dates = pd.date_range('20130101', periods=6)
pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
通过字典创建dataframe
data = {'name':['tom', 'bob', 'dog'],
         'phone':[123, 444, 789],}
pd.DataFrame(data)              # 一个字典创建
pd.DataFrame([dict1, dict2])    # 用n个字典创建

       A  B  C  D
01-01  1  5  9  5
01-02  4  6  0  2
01-03  3  8  8  4
01-04  5  2  6  8
01-05  6  3  7  6
01-06  7  4  3  9 


page10 DataFrame
获取行和列，返回Series对象
data = {'name':['tom', 'bob', 'dog'],
         'phone':[123, 444, 789],
         'year': 2017,
         'xuehao': pd.Series([2,3,4])}
df = pd.DataFrame(data)
df.name   或 df['name']    # 获取一列
df.ix[1]             # 获取一行
df.xuehao = np.arange(1,4)  # 列赋值，长度要匹配
df.ix[0] = ['cat', 888, 4,2018]  # 给行赋值
定义和赋值时行或列的对象可以是常量，列表，numpy数组，Series

page11 DataFrame
data = {'name':['tom', 'bob', 'dog'],
         'phone':[123, 444, 789],
         'year': 2017,
         'xuehao': pd.Series([2,3,4])}
df = pd.DataFrame(data)
df['class'] ='class1'  #新建一列, 可以是一个常亮或任意的序列类型
del df['class']    # 删除一列
df.ix[3] = ['cat',333,56,2000]  # 添加一行
df2 = df.T   # 返回另一个行列转换过的dataframe

page12 查看数据
查看数据
df = pd.DataFrame(np.random.randint(10,size=(6,4)), index=list('bdcfea'), columns=list('BDAC'))
df.head(4)   df.tail(3)   # 显示头和尾的几条
df.index ,  df.columns  # 行名， 列名
df.values                   # 返回的是ndarray
df.describe()
df.sort_index()
df.sort_index(axis=1, ascending=False)
df.sort_values(by='B')   df.sort_values(by=['A','B'])
df.T       # 矩阵转置

page13 选择数据
选择数据
df = pd.DataFrame(np.random.randint(10,size=(6,4)), index=list('abcdef'), columns=list('ABCD'))
df['A']  或 df.A     # 选列
df[['A', 'B']]   # 选多列
df[0:3]df['a':'d']   # 选多行
通过标签选择，用loc，ix
df.loc['b']
df.loc[:,['A','B']]
df.loc['b',['A','B']]
df.loc['b':'d',['A','B']]
df.loc['b','A']



page14 选择数据
通过位置选择iloc，ix
df.iloc[3]
df.iloc[3:5,0:2]
df.iloc[[1,2,4],[0,2]]
df.iloc[1:3,:]
df.iloc[:,1:3]
df.iloc[1,1]
布尔型索引
df[df.A > 5]
df[df > 5]
df[df['D'].isin([2,3,4])]
df.ix[df.B>5, :3]

page15 处理缺失数据
丢弃数据
df = pd.DataFrame(np.arange(20).reshape(5,4), columns=list('ABCD'))
df.loc[0:1,'D'] = np.nan
df.loc[3,'C'] = np.nan
df.dropna()   # 丢弃含有nan的行
df.dropna(axis=1)   # 丢弃含有nan的列
填充数据
df.fillna(5)          # 对nan值赋一个固定值
df.fillna({'C':1, 'D': 99})  #通过字典对列分别赋值

    A   B     C     D
0   0   1   2.0   NaN
1   4   5   6.0   NaN
2   8   9  10.0  11.0
3  12  13   NaN  15.0
4  16  17  18.0  19.0


page16 统计
df.sum()
df.sum(axis=1)         # 默认0
df.sum(skipna=False)   # skipna忽略Nan值，默认为True
count       # 非NA值数量
describe    # 列出一些常用的汇总统计
max  min    #  最大值  最小值
idxmax  idxmin   # 最大最小值的索引值
quantile    # 计算样本的分位数
mean   # 平均数  median   # 中位数（50%分位数）
var   std   # 方差  标准差


page17 统计
累计统计
cumsum()    # 累计和
cumprod()   # 累计积
df.rolling(window=n).max()
df.rolling(window=n).mean()
df.rolling(window=n).var()
df.rolling(window=n).std()
df.rolling(window=n).corr()
df.rolling(window=n).cov()
df.xx.shift(n)   # 偏移

page18 算术运算
运算结果是并集，不存在自动填充NaN
s1 = pd.Series(range(4),index=list('abce'))
s2 = pd.Series(range(4),index=list('bcdf'))
s1+s2
df1 = pd.DataFrame(np.arange(9).reshape((3,3)))
df2 = pd.DataFrame(np.arange(16).reshape((4,4)))
df1 + df2
如果想填充值，用add,sub,div,mul方法
df1.add(df2, fill_value=0) df1.add(df2, fill_value=0)

page19 算术运算
DataFrame和Series之间的运算
df = pd.DataFrame(np.arange(16).reshape((4,4)))
s = df.ix[0]   # 选取一行
df - s   # 沿着行逐一向下计算
想在列上运算，使用add,sub,div,mul方法
s2 = df[0]     # 选取一列
df.sub(s2, axis=0)

函数应用到每个元素
func = lambda x: x+2
df.applymap(func)
np.abs(df)    #Numpy的元素级数组方法
函数应用到行或列
func = lambda x:x.max() – x.min()
df.apply(func)   # 行
df.apply(func, axis=1)

函数应用到多列
df = pd.DataFrame ({'a' : np.random.randint(6,size=6),
             'b' : ['foo', 'bar'] * 3,
             'c' : np.random.randint(6,size=6)})
def foo(row):
    return row['a'] * row['c']
df['Value'] = df.apply(foo, axis=1)


page20 分组
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                        'foo', 'bar', 'foo', 'foo'],
                    'B' : ['one', 'one', 'two', 'three',
                        'two', 'two', 'one', 'three'],
                    'C' : np.random.randint(8,size=8),
                    'D' : np.random.randint(8,size=8)})
df.groupby('A').sum()
df.groupby(['A','B']).sum()


page21  读写文件
csv
df.to_csv('foo.csv')
pd.read_csv('foo.csv')
Excel  读需要pip3 install xlrd
df.to_excel('foo.xlsx', sheet_name='Sheet1')
pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
HDF5   需要pip3 install tables
df.to_hdf('foo.h5','df')
pd.read_hdf('foo.h5','df')


page21 练习
1, 有两门课的成绩，打印出两门课都及格的学生名字
math = {'cat': 55, 'bob': 75, 'pig': 85, 'tom': 50, 'dog': 66}
english = {'cat': 95, 'bob': 88, 'pig': 85, 'tom': 50}
2, 以总分由高到低打印出学生名字，缺考为零分
