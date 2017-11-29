Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np

i
>>> import pandas as pd

>>> df = pd.DataFrame(np.random.randint(9, size=(9,4)),columns=list('ABCD'))
>>> df
   A  B  C  D
0  0  1  2  1
1  3  3  4  2
2  2  3  6  6
3  1  1  6  3
4  0  2  4  0
5  0  4  8  5
6  8  7  7  7
7  0  2  5  2
8  0  5  4  7
>>> df.A.corr(df.B)
0.6825623184484334
>>> dfcum = df.cumsum()
>>> dfcum
    A   B   C   D
0   0   1   2   1
1   3   4   6   3
2   5   7  12   9
3   6   8  18  12
4   6  10  22  12
5   6  14  30  17
6  14  21  37  24
7  14  23  42  26
8  14  28  46  33
>>> dfcum.A.corr(dfcum.B)
0.96292642570167264
>>> dfcum.A.cov(dfcum.B)
46.31944444444445
>>> df
   A  B  C  D
0  0  1  2  1
1  3  3  4  2
2  2  3  6  6
3  1  1  6  3
4  0  2  4  0
5  0  4  8  5
6  8  7  7  7
7  0  2  5  2
8  0  5  4  7
>>> df['Dshift'] = df.D.shift(1)
>>> df
   A  B  C  D  Dshift
0  0  1  2  1     NaN
1  3  3  4  2     1.0
2  2  3  6  6     2.0
3  1  1  6  3     6.0
4  0  2  4  0     3.0
5  0  4  8  5     0.0
6  8  7  7  7     5.0
7  0  2  5  2     7.0
8  0  5  4  7     2.0
>>> df['Dshift-2'] = df.D.shift(-2)
>>> df
   A  B  C  D  Dshift  Dshift-2
0  0  1  2  1     NaN       6.0
1  3  3  4  2     1.0       3.0
2  2  3  6  6     2.0       0.0
3  1  1  6  3     6.0       5.0
4  0  2  4  0     3.0       7.0
5  0  4  8  5     0.0       2.0
6  8  7  7  7     5.0       7.0
7  0  2  5  2     7.0       NaN
8  0  5  4  7     2.0       NaN
>>> users = df.read_csv(r'E:\python_files\csv\users.csv')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    users = df.read_csv(r'E:\python_files\csv\users.csv')
  File "D:\Python36\lib\site-packages\pandas\core\generic.py", line 3081, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'read_csv'
>>> users = pd.read_csv(r'E:\python_files\csv\users.csv')
>>> users
     user_id  age gender     occupation zip_code
0          1   24      M     technician    85711
1          2   53      F          other    94043
2          3   23      M         writer    32067
3          4   24      M     technician    43537
4          5   33      F          other    15213
5          6   42      M      executive    98101
6          7   57      M  administrator    91344
7          8   36      M  administrator    05201
8          9   29      M        student    01002
9         10   53      M         lawyer    90703
10        11   39      F          other    30329
11        12   28      F          other    06405
12        13   47      M       educator    29206
13        14   45      M      scientist    55106
14        15   49      F       educator    97301
15        16   21      M  entertainment    10309
16        17   30      M     programmer    06355
17        18   35      F          other    37212
18        19   40      M      librarian    02138
19        20   42      F      homemaker    95660
20        21   26      M         writer    30068
21        22   25      M         writer    40206
22        23   30      F         artist    48197
23        24   21      F         artist    94533
24        25   39      M       engineer    55107
25        26   49      M       engineer    21044
26        27   40      F      librarian    30030
27        28   32      M         writer    55369
28        29   41      M     programmer    94043
29        30    7      M        student    55436
..       ...  ...    ...            ...      ...
913      914   44      F          other    08105
914      915   50      M  entertainment    60614
915      916   27      M       engineer    N2L5N
916      917   22      F        student    20006
917      918   40      M      scientist    70116
918      919   25      M          other    14216
919      920   30      F         artist    90008
920      921   20      F        student    98801
921      922   29      F  administrator    21114
922      923   21      M        student    E2E3R
923      924   29      M          other    11753
924      925   18      F       salesman    49036
925      926   49      M  entertainment    01701
926      927   23      M     programmer    55428
927      928   21      M        student    55408
928      929   44      M      scientist    53711
929      930   28      F      scientist    07310
930      931   60      M       educator    33556
931      932   58      M       educator    06437
932      933   28      M        student    48105
933      934   61      M       engineer    22902
934      935   42      M         doctor    66221
935      936   24      M          other    32789
936      937   48      M       educator    98072
937      938   38      F     technician    55038
938      939   26      F        student    33319
939      940   32      M  administrator    02215
940      941   20      M        student    97229
941      942   48      F      librarian    78209
942      943   22      M        student    77841

[943 rows x 5 columns]
>>> type(users)
<class 'pandas.core.frame.DataFrame'>
>>> dfhead = df.head(20)
>>> dfhead
   A  B  C  D  Dshift  Dshift-2
0  0  1  2  1     NaN       6.0
1  3  3  4  2     1.0       3.0
2  2  3  6  6     2.0       0.0
3  1  1  6  3     6.0       5.0
4  0  2  4  0     3.0       7.0
5  0  4  8  5     0.0       2.0
6  8  7  7  7     5.0       7.0
7  0  2  5  2     7.0       NaN
8  0  5  4  7     2.0       NaN
>>> usershead = users.head(20)
>>> usershead
    user_id  age gender     occupation zip_code
0         1   24      M     technician    85711
1         2   53      F          other    94043
2         3   23      M         writer    32067
3         4   24      M     technician    43537
4         5   33      F          other    15213
5         6   42      M      executive    98101
6         7   57      M  administrator    91344
7         8   36      M  administrator    05201
8         9   29      M        student    01002
9        10   53      M         lawyer    90703
10       11   39      F          other    30329
11       12   28      F          other    06405
12       13   47      M       educator    29206
13       14   45      M      scientist    55106
14       15   49      F       educator    97301
15       16   21      M  entertainment    10309
16       17   30      M     programmer    06355
17       18   35      F          other    37212
18       19   40      M      librarian    02138
19       20   42      F      homemaker    95660
>>> users.shape[0]
943
>>> users.index.size
943
>>> users.columns
Index(['user_id', 'age', 'gender', 'occupation', 'zip_code'], dtype='object')
>>> users.columns.size
5
>>> users.shape[1]
5
>>> users.shape
(943, 5)
>>> users.ndim
2
>>> users.dtye
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    users.dtye
  File "D:\Python36\lib\site-packages\pandas\core\generic.py", line 3081, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'dtye'
>>> users.dtype
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    users.dtype
  File "D:\Python36\lib\site-packages\pandas\core\generic.py", line 3081, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'dtype'
>>> users.index
RangeIndex(start=0, stop=943, step=1)
>>> users.columns
Index(['user_id', 'age', 'gender', 'occupation', 'zip_code'], dtype='object')
>>> users.occupation
0         technician
1              other
2             writer
3         technician
4              other

>>> users.occupation.unique()
array(['technician', 'other', 'writer', 'executive', 'administrator',
       'student', 'lawyer', 'educator', 'scientist', 'entertainment',
       'programmer', 'librarian', 'homemaker', 'artist', 'engineer',
       'marketing', 'none', 'healthcare', 'retired', 'salesman', 'doctor'], dtype=object)
>>> set(users.occupation)
{'healthcare', 'artist', 'retired', 'student', 'programmer', 'scientist', 'educator', 'homemaker', 'entertainment', 'librarian', 'doctor', 'marketing', 'salesman', 'technician', 'lawyer', 'engineer', 'writer', 'other', 'administrator', 'none', 'executive'}
>>> users.value_counts()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    users.value_counts()
  File "D:\Python36\lib\site-packages\pandas\core\generic.py", line 3081, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'value_counts'
>>> users.occupation.value_counts(3)
student          0.207847
other            0.111347
educator         0.100742
administrator    0.083775
engineer         0.071050
programmer       0.069989
librarian        0.054083
writer           0.047720
executive        0.033934
scientist        0.032874
artist           0.029692
technician       0.028632
marketing        0.027572
entertainment    0.019088
healthcare       0.016967
retired          0.014846
salesman         0.012725
lawyer           0.012725
none             0.009544
homemaker        0.007423
doctor           0.007423
Name: occupation, dtype: float64
>>> users.occupation.value_counts()[:1]
student    196
Name: occupation, dtype: int64
>>> users.occupation.value_counts()
student          196
other            105
educator          95
administrator     79
engineer          67
programmer        66
librarian         51
writer            45
executive         32
scientist         31
artist            28
technician        27
marketing         26
entertainment     18
healthcare        16
retired           14
salesman          12
lawyer            12
none               9
homemaker          7
doctor             7
Name: occupation, dtype: int64
>>> help(users.occupation.value_counts)
Help on method value_counts in module pandas.core.base:

value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True) method of pandas.core.series.Series instance
    Returns object containing counts of unique values.
    
    The resulting object will be in descending order so that the
    first element is the most frequently-occurring element.
    Excludes NA values by default.
    
    Parameters
    ----------
    normalize : boolean, default False
        If True then the object returned will contain the relative
        frequencies of the unique values.
    sort : boolean, default True
        Sort by values
    ascending : boolean, default False
        Sort in ascending order
    bins : integer, optional
        Rather than count values, group them into half-open bins,
        a convenience for pd.cut, only works with numeric data
    dropna : boolean, default True
        Don't include counts of NaN.
    
    Returns
    -------
    counts : Series

>>> users.age.means()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    users.age.means()
  File "D:\Python36\lib\site-packages\pandas\core\generic.py", line 3081, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'means'
>>> users.age.mean()
34.051961823966067
>>> users.head(2)
   user_id  age gender  occupation zip_code
0        1   24      M  technician    85711
1        2   53      F       other    94043
>>> man = users[users.gender=='M']
>>> man
     user_id  age gender     occupation zip_code
0          1   24      M     technician    85711
2          3   23      M         writer    32067
3          4   24      M     technician    43537
5          6   42      M      executive    98101
6          7   57      M  administrator    91344
7          8   36      M  administrator    05201
8          9   29      M        student    01002
9         10   53      M         lawyer    90703
12        13   47      M       educator    29206
13        14   45      M      scientist    55106
15        16   21      M  entertainment    10309
16        17   30      M     programmer    06355
18        19   40      M      librarian    02138
20        21   26      M         writer    30068
21        22   25      M         writer    40206
24        25   39      M       engineer    55107
25        26   49      M       engineer    21044
27        28   32      M         writer    55369
28        29   41      M     programmer    94043
29        30    7      M        student    55436
30        31   24      M         artist    10003
32        33   23      M        student    27510
36        37   23      M        student    55105
38        39   41      M  entertainment    01040
39        40   38      M      scientist    27514
40        41   33      M       engineer    80525
41        42   30      M  administrator    17870
43        44   26      M     technician    46260
44        45   29      M     programmer    50233
46        47   53      M      marketing    07102
..       ...  ...    ...            ...      ...
897      898   23      M      homemaker    61755
898      899   32      M          other    55116
899      900   60      M        retired    18505
900      901   38      M      executive    L1V3W
902      903   28      M       educator    20850
904      905   27      M          other    30350
905      906   45      M      librarian    70124
909      910   28      M     healthcare    29301
911      912   51      M          other    06512
912      913   27      M        student    76201
914      915   50      M  entertainment    60614
915      916   27      M       engineer    N2L5N
917      918   40      M      scientist    70116
918      919   25      M          other    14216
922      923   21      M        student    E2E3R
923      924   29      M          other    11753
925      926   49      M  entertainment    01701
926      927   23      M     programmer    55428
927      928   21      M        student    55408
928      929   44      M      scientist    53711
930      931   60      M       educator    33556
931      932   58      M       educator    06437
932      933   28      M        student    48105
933      934   61      M       engineer    22902
934      935   42      M         doctor    66221
935      936   24      M          other    32789
936      937   48      M       educator    98072
939      940   32      M  administrator    02215
940      941   20      M        student    97229
942      943   22      M        student    77841

[670 rows x 5 columns]
>>> man.age.mean()
34.149253731343286
>>> student = users[users.occupation=='Student']
>>> student
Empty DataFrame
Columns: [user_id, age, gender, occupation, zip_code]
Index: []
>>> student = users[users.occupation=='student']
>>> student.age.mean()
22.081632653061224
>>> p = users[users.occupation=='programmer']
>>> p.age.mean()
33.121212121212125
>>> df
   A  B  C  D  Dshift  Dshift-2
0  0  1  2  1     NaN       6.0
1  3  3  4  2     1.0       3.0
2  2  3  6  6     2.0       0.0
3  1  1  6  3     6.0       5.0
4  0  2  4  0     3.0       7.0
5  0  4  8  5     0.0       2.0
6  8  7  7  7     5.0       7.0
7  0  2  5  2     7.0       NaN
8  0  5  4  7     2.0       NaN
>>> df.dropna()
   A  B  C  D  Dshift  Dshift-2
1  3  3  4  2     1.0       3.0
2  2  3  6  6     2.0       0.0
3  1  1  6  3     6.0       5.0
4  0  2  4  0     3.0       7.0
5  0  4  8  5     0.0       2.0
6  8  7  7  7     5.0       7.0
>>> df.dropna(1)
   A  B  C  D
0  0  1  2  1
1  3  3  4  2
2  2  3  6  6
3  1  1  6  3
4  0  2  4  0
5  0  4  8  5
6  8  7  7  7
7  0  2  5  2
8  0  5  4  7
>>> df
   A  B  C  D  Dshift  Dshift-2
0  0  1  2  1     NaN       6.0
1  3  3  4  2     1.0       3.0
2  2  3  6  6     2.0       0.0
3  1  1  6  3     6.0       5.0
4  0  2  4  0     3.0       7.0
5  0  4  8  5     0.0       2.0
6  8  7  7  7     5.0       7.0
7  0  2  5  2     7.0       NaN
8  0  5  4  7     2.0       NaN
>>> df.fillna(5)
   A  B  C  D  Dshift  Dshift-2
0  0  1  2  1     5.0       6.0
1  3  3  4  2     1.0       3.0
2  2  3  6  6     2.0       0.0
3  1  1  6  3     6.0       5.0
4  0  2  4  0     3.0       7.0
5  0  4  8  5     0.0       2.0
6  8  7  7  7     5.0       7.0
7  0  2  5  2     7.0       5.0
8  0  5  4  7     2.0       5.0
>>> df.fillna({'Dshift':1, 'Dshift-2':999})
   A  B  C  D  Dshift  Dshift-2
0  0  1  2  1     1.0       6.0
1  3  3  4  2     1.0       3.0
2  2  3  6  6     2.0       0.0
3  1  1  6  3     6.0       5.0
4  0  2  4  0     3.0       7.0
5  0  4  8  5     0.0       2.0
6  8  7  7  7     5.0       7.0
7  0  2  5  2     7.0     999.0
8  0  5  4  7     2.0     999.0
>>> s1 = pd.Series(range(4),index=list('bacd'))
>>> s2 = pd.Series(range(4),index=list('eacd'))
>>> s1
b    0
a    1
c    2
d    3
dtype: int32
>>> s2
e    0
a    1
c    2
d    3
dtype: int32
>>> s1+s2
a    2.0
b    NaN
c    4.0
d    6.0
e    NaN
dtype: float64
>>> df1 = pd.DataFrame(np.arange(9).reshape(3,3))
>>> df1 = pd.DataFrame(np.arange(16).reshape(4,4))
>>> df2 = pd.DataFrame(np.arange(9).reshape(3,3))
>>> df1 + df2
      0     1     2   3
0   0.0   2.0   4.0 NaN
1   7.0   9.0  11.0 NaN
2  14.0  16.0  18.0 NaN
3   NaN   NaN   NaN NaN
>>> df1.add(df2, fill_value=0)
      0     1     2     3
0   0.0   2.0   4.0   3.0
1   7.0   9.0  11.0   7.0
2  14.0  16.0  18.0  11.0
3  12.0  13.0  14.0  15.0
>>> df1
    0   1   2   3
0   0   1   2   3
1   4   5   6   7
2   8   9  10  11
3  12  13  14  15
>>> df2
   0  1  2
0  0  1  2
1  3  4  5
2  6  7  8
>>> s1
b    0
a    1
c    2
d    3
dtype: int32
>>> df1
    0   1   2   3
0   0   1   2   3
1   4   5   6   7
2   8   9  10  11
3  12  13  14  15
>>> df1 - s1

Warning (from warnings module):
  File "D:\Python36\lib\site-packages\pandas\core\indexes\base.py", line 3033
    return this.join(other, how=how, return_indexers=return_indexers)
RuntimeWarning: '<' not supported between instances of 'int' and 'str', sort order is undefined for incomparable objects
    0   1   2   3   b   a   c   d
0 NaN NaN NaN NaN NaN NaN NaN NaN
1 NaN NaN NaN NaN NaN NaN NaN NaN
2 NaN NaN NaN NaN NaN NaN NaN NaN
3 NaN NaN NaN NaN NaN NaN NaN NaN
>>> df1.index=list('bacd')
>>> df1-s1
    0   1   2   3   b   a   c   d
b NaN NaN NaN NaN NaN NaN NaN NaN
a NaN NaN NaN NaN NaN NaN NaN NaN
c NaN NaN NaN NaN NaN NaN NaN NaN
d NaN NaN NaN NaN NaN NaN NaN NaN
>>> df1.columns=list('bacd')
>>> df1-s1
    b   a   c   d
b   0   0   0   0
a   4   4   4   4
c   8   8   8   8
d  12  12  12  12
>>> df1
    b   a   c   d
b   0   1   2   3
a   4   5   6   7
c   8   9  10  11
d  12  13  14  15
>>> df1.sub(s1)
    b   a   c   d
b   0   0   0   0
a   4   4   4   4
c   8   8   8   8
d  12  12  12  12
>>> df1.sub(s1, axis=1)
    b   a   c   d
b   0   0   0   0
a   4   4   4   4
c   8   8   8   8
d  12  12  12  12
>>> s1
b    0
a    1
c    2
d    3
dtype: int32
>>> df
   A  B  C  D  Dshift  Dshift-2
0  0  1  2  1     NaN       6.0
1  3  3  4  2     1.0       3.0
2  2  3  6  6     2.0       0.0
3  1  1  6  3     6.0       5.0
4  0  2  4  0     3.0       7.0
5  0  4  8  5     0.0       2.0
6  8  7  7  7     5.0       7.0
7  0  2  5  2     7.0       NaN
8  0  5  4  7     2.0       NaN
>>> df1
    b   a   c   d
b   0   1   2   3
a   4   5   6   7
c   8   9  10  11
d  12  13  14  15
>>> s1
b    0
a    1
c    2
d    3
dtype: int32
>>> df1.sub(s1,axis=0)
   b   a   c   d
b  0   1   2   3
a  3   4   5   6
c  6   7   8   9
d  9  10  11  12
>>> df1.sub(s1,axis=1)
    b   a   c   d
b   0   0   0   0
a   4   4   4   4
c   8   8   8   8
d  12  12  12  12
>>> df1 - s1
    b   a   c   d
b   0   0   0   0
a   4   4   4   4
c   8   8   8   8
d  12  12  12  12
>>> df1
    b   a   c   d
b   0   1   2   3
a   4   5   6   7
c   8   9  10  11
d  12  13  14  15
>>> s2 = df['a']
Traceback (most recent call last):
  File "D:\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2442, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc (pandas\_libs\index.c:5280)
  File "pandas\_libs\index.pyx", line 154, in pandas._libs.index.IndexEngine.get_loc (pandas\_libs\index.c:5126)
  File "pandas\_libs\hashtable_class_helper.pxi", line 1210, in pandas._libs.hashtable.PyObjectHashTable.get_item (pandas\_libs\hashtable.c:20523)
  File "pandas\_libs\hashtable_class_helper.pxi", line 1218, in pandas._libs.hashtable.PyObjectHashTable.get_item (pandas\_libs\hashtable.c:20477)
KeyError: 'a'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    s2 = df['a']
  File "D:\Python36\lib\site-packages\pandas\core\frame.py", line 1964, in __getitem__
    return self._getitem_column(key)
  File "D:\Python36\lib\site-packages\pandas\core\frame.py", line 1971, in _getitem_column
    return self._get_item_cache(key)
  File "D:\Python36\lib\site-packages\pandas\core\generic.py", line 1645, in _get_item_cache
    values = self._data.get(item)
  File "D:\Python36\lib\site-packages\pandas\core\internals.py", line 3590, in get
    loc = self.items.get_loc(item)
  File "D:\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2444, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc (pandas\_libs\index.c:5280)
  File "pandas\_libs\index.pyx", line 154, in pandas._libs.index.IndexEngine.get_loc (pandas\_libs\index.c:5126)
  File "pandas\_libs\hashtable_class_helper.pxi", line 1210, in pandas._libs.hashtable.PyObjectHashTable.get_item (pandas\_libs\hashtable.c:20523)
  File "pandas\_libs\hashtable_class_helper.pxi", line 1218, in pandas._libs.hashtable.PyObjectHashTable.get_item (pandas\_libs\hashtable.c:20477)
KeyError: 'a'
>>> s2 = df1['a']
>>> s2
b     1
a     5
c     9
d    13
Name: a, dtype: int32
>>> df1
    b   a   c   d
b   0   1   2   3
a   4   5   6   7
c   8   9  10  11
d  12  13  14  15
>>> df1 - s2
    b  a  c   d
b  -1 -4 -7 -10
a   3  0 -3  -6
c   7  4  1  -2
d  11  8  5   2
>>> df1.sub(s2)
    b  a  c   d
b  -1 -4 -7 -10
a   3  0 -3  -6
c   7  4  1  -2
d  11  8  5   2
>>> df1.sub(s2, axis=0)
   b  a  c  d
b -1  0  1  2
a -1  0  1  2
c -1  0  1  2
d -1  0  1  2


>>> df1.sub(s2, axis='index')
   b  a  c  d
b -1  0  1  2
a -1  0  1  2
c -1  0  1  2
d -1  0  1  2
>>> df1.sub(s2, axis=0)
   b  a  c  d
b -1  0  1  2
a -1  0  1  2
c -1  0  1  2
d -1  0  1  2
>>> s2
b     1
a     5
c     9
d    13
Name: a, dtype: int32
>>> df1
    b   a   c   d
b   0   1   2   3
a   4   5   6   7
c   8   9  10  11
d  12  13  14  15


>>> df
   A  B  C  D  Dshift  Dshift-2
0  0  1  2  1     NaN       6.0
1  3  3  4  2     1.0       3.0
2  2  3  6  6     2.0       0.0
3  1  1  6  3     6.0       5.0
4  0  2  4  0     3.0       7.0
5  0  4  8  5     0.0       2.0
6  8  7  7  7     5.0       7.0
7  0  2  5  2     7.0       NaN
8  0  5  4  7     2.0       NaN
>>> df = df.drop('Dshift', axis=1)
>>> df
   A  B  C  D  Dshift-2
0  0  1  2  1       6.0
1  3  3  4  2       3.0
2  2  3  6  6       0.0
3  1  1  6  3       5.0
4  0  2  4  0       7.0
5  0  4  8  5       2.0
6  8  7  7  7       7.0
7  0  2  5  2       NaN
8  0  5  4  7       NaN
>>> df2 = df.drop('Dshift-2', axis=1)
>>> df2
   A  B  C  D
0  0  1  2  1
1  3  3  4  2
2  2  3  6  6
3  1  1  6  3
4  0  2  4  0
5  0  4  8  5
6  8  7  7  7
7  0  2  5  2
8  0  5  4  7
>>> lst = ['A','B','C','D']
>>> df2[lst]
   A  B  C  D
0  0  1  2  1
1  3  3  4  2
2  2  3  6  6
3  1  1  6  3
4  0  2  4  0
5  0  4  8  5
6  8  7  7  7
7  0  2  5  2
8  0  5  4  7
>>> df
   A  B  C  D  Dshift-2
0  0  1  2  1       6.0
1  3  3  4  2       3.0
2  2  3  6  6       0.0
3  1  1  6  3       5.0
4  0  2  4  0       7.0
5  0  4  8  5       2.0
6  8  7  7  7       7.0
7  0  2  5  2       NaN
8  0  5  4  7       NaN
>>> df.ix[:, 'A':'D']
   A  B  C  D
0  0  1  2  1
1  3  3  4  2
2  2  3  6  6
3  1  1  6  3
4  0  2  4  0
5  0  4  8  5
6  8  7  7  7
7  0  2  5  2
8  0  5  4  7
>>> df = df.ix[:, 'A':'D']
>>> df
   A  B  C  D
0  0  1  2  1
1  3  3  4  2
2  2  3  6  6
3  1  1  6  3
4  0  2  4  0
5  0  4  8  5
6  8  7  7  7
7  0  2  5  2
8  0  5  4  7
>>> df + 2
    A  B   C  D
0   2  3   4  3
1   5  5   6  4
2   4  5   8  8
3   3  3   8  5
4   2  4   6  2
5   2  6  10  7
6  10  9   9  9
7   2  4   7  4
8   2  7   6  9
>>> func = lambda x:x+2
>>> df.applymap(func)
    A  B   C  D
0   2  3   4  3
1   5  5   6  4
2   4  5   8  8
3   3  3   8  5
4   2  4   6  2
5   2  6  10  7
6  10  9   9  9
7   2  4   7  4
8   2  7   6  9
>>> df
   A  B  C  D
0  0  1  2  1
1  3  3  4  2
2  2  3  6  6
3  1  1  6  3
4  0  2  4  0
5  0  4  8  5
6  8  7  7  7
7  0  2  5  2
8  0  5  4  7
>>> df = df.applymap(func)
>>> df
    A  B   C  D
0   2  3   4  3
1   5  5   6  4
2   4  5   8  8
3   3  3   8  5
4   2  4   6  2
5   2  6  10  7
6  10  9   9  9
7   2  4   7  4
8   2  7   6  9
>>> maxmin = lambda s:s.max()-s.min()
>>> df.apply(maxmin)
A    8
B    6
C    6
D    7
dtype: int64
>>> df.apply(maxmin, axis=1)
0    2
1    2
2    4
3    5
4    4
5    8
6    1
7    5
8    7
dtype: int64
>>> df
    A  B   C  D
0   2  3   4  3
1   5  5   6  4
2   4  5   8  8
3   3  3   8  5
4   2  4   6  2
5   2  6  10  7
6  10  9   9  9
7   2  4   7  4
8   2  7   6  9
>>> s = df.A
>>> s.applymap
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    s.applymap
  File "D:\Python36\lib\site-packages\pandas\core\generic.py", line 3081, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'applymap'
>>> s.apply(maxmin)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    s.apply(maxmin)
  File "D:\Python36\lib\site-packages\pandas\core\series.py", line 2355, in apply
    mapped = lib.map_infer(values, f, convert=convert_dtype)
  File "pandas\_libs\src\inference.pyx", line 1574, in pandas._libs.lib.map_infer (pandas\_libs\lib.c:66645)
  File "<pyshell#126>", line 1, in <lambda>
    maxmin = lambda s:s.max()-s.min()
AttributeError: 'int' object has no attribute 'max'
>>> s.apply(func)
0     4
1     7
2     6
3     5
4     4
5     4
6    12
7     4
8     4
Name: A, dtype: int64
>>> df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                        'foo', 'bar', 'foo', 'foo'],
                    'B' : ['one', 'one', 'two', 'three',
                        'two', 'two', 'one', 'three'],
                    'C' : np.random.randint(8,size=8),
                    'D' : np.random.randint(8,size=8)})

>>> 
>>> df
     A      B  C  D
0  foo    one  2  3
1  bar    one  1  3
2  foo    two  2  0
3  bar  three  3  2
4  foo    two  7  0
5  bar    two  3  6
6  foo    one  6  5
7  foo  three  5  1
>>> df.groupby('A').sum()
      C   D
A          
bar   7  11
foo  22   9
>>> df.groupby('A')
<pandas.core.groupby.DataFrameGroupBy object at 0x05777D70>
>>> grouped = df.groupby('A')
>>> grouped.mean()
            C         D
A                      
bar  2.333333  3.666667
foo  4.400000  1.800000
>>> df.groupby(['A', 'B']).sum()
           C  D
A   B          
bar one    1  3
    three  3  2
    two    3  6
foo one    8  8
    three  5  1
    two    9  0
>>> 
