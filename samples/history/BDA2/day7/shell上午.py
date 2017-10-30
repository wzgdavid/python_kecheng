Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import pandas as pd
>>> import matplotlib.pyplot as plt

>>> import seaborn as sns
>>> df = pd.read_csv(r'E:\python_files\csv\users.csv')
>>> df
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
>>> df.columns
Index(['user_id', 'age', 'gender', 'occupation', 'zip_code'], dtype='object')
>>> df = pd.read_csv(r'E:\python_files\csv\users.csv', names=['id', 'age', 'g','occup', 'zip'])
>>> df.columns
Index(['id', 'age', 'g', 'occup', 'zip'], dtype='object')
>>> df = pd.read_csv(r'E:\python_files\csv\users.csv', names=['id', 'age', 'g','occup', 'zip'], encoding='utf-8')
>>> df
          id  age       g          occup       zip
0    user_id  age  gender     occupation  zip_code
1          1   24       M     technician     85711
2          2   53       F          other     94043
3          3   23       M         writer     32067
4          4   24       M     technician     43537
5          5   33       F          other     15213
6          6   42       M      executive     98101
7          7   57       M  administrator     91344
8          8   36       M  administrator     05201
9          9   29       M        student     01002
10        10   53       M         lawyer     90703
11        11   39       F          other     30329
12        12   28       F          other     06405
13        13   47       M       educator     29206
14        14   45       M      scientist     55106
15        15   49       F       educator     97301
16        16   21       M  entertainment     10309
17        17   30       M     programmer     06355
18        18   35       F          other     37212
19        19   40       M      librarian     02138
20        20   42       F      homemaker     95660
21        21   26       M         writer     30068
22        22   25       M         writer     40206
23        23   30       F         artist     48197
24        24   21       F         artist     94533
25        25   39       M       engineer     55107
26        26   49       M       engineer     21044
27        27   40       F      librarian     30030
28        28   32       M         writer     55369
29        29   41       M     programmer     94043
..       ...  ...     ...            ...       ...
914      914   44       F          other     08105
915      915   50       M  entertainment     60614
916      916   27       M       engineer     N2L5N
917      917   22       F        student     20006
918      918   40       M      scientist     70116
919      919   25       M          other     14216
920      920   30       F         artist     90008
921      921   20       F        student     98801
922      922   29       F  administrator     21114
923      923   21       M        student     E2E3R
924      924   29       M          other     11753
925      925   18       F       salesman     49036
926      926   49       M  entertainment     01701
927      927   23       M     programmer     55428
928      928   21       M        student     55408
929      929   44       M      scientist     53711
930      930   28       F      scientist     07310
931      931   60       M       educator     33556
932      932   58       M       educator     06437
933      933   28       M        student     48105
934      934   61       M       engineer     22902
935      935   42       M         doctor     66221
936      936   24       M          other     32789
937      937   48       M       educator     98072
938      938   38       F     technician     55038
939      939   26       F        student     33319
940      940   32       M  administrator     02215
941      941   20       M        student     97229
942      942   48       F      librarian     78209
943      943   22       M        student     77841

[944 rows x 5 columns]
>>> df = pd.read_csv(r'E:\python_files\csv\users.csv')
>>> df
     user_id  age gender     occupation zip_code
0          1   24      M     technician    85711
1          2   53      F             方法    94043
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
>>> df = pd.read_csv(r'E:\python_files\csv\users.csv', encoding='gbk')
>>> df = pd.read_csv(r'E:\python_files\csv\users.csv', encoding='ascii')
Traceback (most recent call last):
  File "pandas\_libs\parsers.pyx", line 1162, in pandas._libs.parsers.TextReader._convert_tokens (pandas\_libs\parsers.c:14858)
  File "pandas\_libs\parsers.pyx", line 1273, in pandas._libs.parsers.TextReader._convert_with_dtype (pandas\_libs\parsers.c:17119)
  File "pandas\_libs\parsers.pyx", line 1292, in pandas._libs.parsers.TextReader._string_convert (pandas\_libs\parsers.c:17387)
  File "pandas\_libs\parsers.pyx", line 1581, in pandas._libs.parsers._string_box_decode (pandas\_libs\parsers.c:23510)
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe6 in position 0: ordinal not in range(128)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    df = pd.read_csv(r'E:\python_files\csv\users.csv', encoding='ascii')
  File "D:\Python36\lib\site-packages\pandas\io\parsers.py", line 655, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "D:\Python36\lib\site-packages\pandas\io\parsers.py", line 411, in _read
    data = parser.read(nrows)
  File "D:\Python36\lib\site-packages\pandas\io\parsers.py", line 1005, in read
    ret = self._engine.read(nrows)
  File "D:\Python36\lib\site-packages\pandas\io\parsers.py", line 1748, in read
    data = self._reader.read(nrows)
  File "pandas\_libs\parsers.pyx", line 890, in pandas._libs.parsers.TextReader.read (pandas\_libs\parsers.c:10862)
  File "pandas\_libs\parsers.pyx", line 912, in pandas._libs.parsers.TextReader._read_low_memory (pandas\_libs\parsers.c:11138)
  File "pandas\_libs\parsers.pyx", line 989, in pandas._libs.parsers.TextReader._read_rows (pandas\_libs\parsers.c:12175)
  File "pandas\_libs\parsers.pyx", line 1117, in pandas._libs.parsers.TextReader._convert_column_data (pandas\_libs\parsers.c:14136)
  File "pandas\_libs\parsers.pyx", line 1169, in pandas._libs.parsers.TextReader._convert_tokens (pandas\_libs\parsers.c:14972)
  File "pandas\_libs\parsers.pyx", line 1273, in pandas._libs.parsers.TextReader._convert_with_dtype (pandas\_libs\parsers.c:17119)
  File "pandas\_libs\parsers.pyx", line 1292, in pandas._libs.parsers.TextReader._string_convert (pandas\_libs\parsers.c:17387)
  File "pandas\_libs\parsers.pyx", line 1581, in pandas._libs.parsers._string_box_decode (pandas\_libs\parsers.c:23510)
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe6 in position 0: ordinal not in range(128)
>>> df = pd.read_csv(r'E:\python_files\csv\users.csv', encoding='gbk')
>>> df.head()
   user_id  age gender  occupation zip_code
0        1   24      M  technician    85711
1        2   53      F         鏂规硶    94043
2        3   23      M      writer    32067
3        4   24      M  technician    43537
4        5   33      F       other    15213
>>> df = pd.read_csv(r'E:\python_files\csv\users.csv')
>>> df.shape
(943, 5)
>>> age = df.age
>>> type(age)
<class 'pandas.core.series.Series'>
>>> id2 = df.ix[1]
>>> id2
user_id           2
age              53
gender            F
occupation       方法
zip_code      94043
Name: 1, dtype: object
>>> type(id2)
<class 'pandas.core.series.Series'>
>>> id2.shape
(5,)
>>> id2 = df[df.user_id==2]
>>> id2
   user_id  age gender occupation zip_code
1        2   53      F         方法    94043
>>> type(id2)
<class 'pandas.core.frame.DataFrame'>
>>> id2.values
array([[2, 53, 'F', '方法', '94043']], dtype=object)
>>> df.head()
   user_id  age gender  occupation zip_code
0        1   24      M  technician    85711
1        2   53      F          方法    94043
2        3   23      M      writer    32067
3        4   24      M  technician    43537
4        5   33      F       other    15213
>>> df.mean()
user_id    472.000000
age         34.051962
dtype: float64
>>> df[df.gender=='M'].age.mean()
34.149253731343286
>>> df.zip_code.apply(lambda x:int(x))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    df.zip_code.apply(lambda x:int(x))
  File "D:\Python36\lib\site-packages\pandas\core\series.py", line 2355, in apply
    mapped = lib.map_infer(values, f, convert=convert_dtype)
  File "pandas\_libs\src\inference.pyx", line 1574, in pandas._libs.lib.map_infer (pandas\_libs\lib.c:66645)
  File "<pyshell#32>", line 1, in <lambda>
    df.zip_code.apply(lambda x:int(x))
ValueError: invalid literal for int() with base 10: 'T8H1N'
>>> code = df.zip_code
>>> code.values
array(['85711', '94043', '32067', '43537', '15213', '98101', '91344',
       '05201', '01002', '90703', '30329', '06405', '29206', '55106',
       '97301', '10309', '06355', '37212', '02138', '95660', '30068',
       '40206', '48197', '94533', '55107', '21044', '30030', '55369',
       '94043', '55436', '10003', '78741', '27510', '42141', '42459',
       '93117', '55105', '54467', '01040', '27514', '80525', '17870',
       '20854', '46260', '50233', '46538', '07102', '12550', '76111',
       '52245', '16509', '55105', '55414', '66315', '01331', '46260',
       '84010', '52246', '08403', '06472', '30040', '97214', '75240',
       '43202', '48118', '80521', '60402', '22904', '55337', '60067',
       '98034', '73034', '41850', 'T8H1N', '08816', '02215', '29379',
       '61801', '03755', '52241', '21218', '22902', '44133', '55369',
       '20003', '46005', '89503', '11701', '68106', '78155', '01913',
       '80525', '23112', '71457', '10707', '75206', '98006', '90291',
       '63129', '90254', '05146', '30220', '55108', '55108', '94043',
       '55125', '60466', '63130', '55423', '77840', '90630', '60613',
       '95032', '75013', '17110', '97232', '16125', '90210', '67401',
       '06260', '99603', '22206', '20008', '60615', '22202', '20015',
       '73439', '20009', '07039', '60115', '15237', '94612', '78602',
       '80236', '38401', '97365', '84408', '53211', '08904', '32250',
       '36117', '48118', '08832', '20910', 'V3N4P', '83814', '02143',
       '97006', '17325', '02139', '48103', '68767', '60641', '53703',
       '11217', '08360', '70808', '27606', '55346', '66215', '55104',
       '15610', '97212', '80123', '53715', '55113', 'L9G2B', '80127',
       '53705', '30067', '78750', '22207', '22306', '52302', '21911',
       '07030', '19104', '49512', '20755', '60202', '21218', '33884',
       '27708', '76013', '97403', '00000', '16801', '29440', '95014',
       '95938', '95161', '90840', '49931', '02154', '93555', '55105',
       '75094', '55414', '17604', '93402', 'E2A4H', '60201', '32301',
       '10960', '06371', '53115', '92037', '01720', '85710', '03060',
       '32605', '61401', '55345', '11231', '63033', '02215', '11727',
       '06513', '43212', '78205', '20685', '27502', '47906', '43512',
       '58202', '92103', '60659', '22003', '22903', '14476', '01080',
       '99709', '98682', '94702', '22973', '53214', '63146', '44124',
       '95628', '20784', '20001', '31404', '60201', '80525', '55109',
       '28734', '20770', '37235', '84103', '95110', '85032', '07733',
       '22903', '42647', '07029', '39042', '77005', '77801', '48823',
       '89801', '85202', '78264', '55346', '90064', '84601', '78756',
       '83716', '19422', '43201', '63119', '22932', '53706', '10016',
       '55414', '92064', '95064', '55406', '30033', '85251', '22903',
       '06059', '20057', '55305', '92629', '53713', '15217', '31211',
       '23226', '94619', '93550', '44106', '94703', '60804', '92110',
       '50325', '16803', '98103', '01581', '63108', '55106', '55439',
       '77904', '14853', '71701', '94086', '73132', '55454', '95076',
       '70802', '91711', '73071', '02110', '60035', '08043', '18301',
       '77009', '13210', '06518', '22030', '24060', '55413', '50613',
       '19149', '02176', '02139', '15235', '11101', '06779', '01720',
       '33884', '91344', '40504', 'V0R2M', '30002', '33775', '42101',
       '10522', '59717', '37901', '80123', '44405', '98006', '30093',
       '94117', '94143', '76059', '90210', '45660', '61455', '97301',
       '49938', '55105', '28480', '48197', '60135', '92688', '98133',
       '10022', '61801', '98027', '44074', '85233', '87501', '01810',
       '20009', '50670', '37411', '92113', '91335', '08534', '99206',
       '66046', '55116', '78746', '37777', '10010', '18015', '02859',
       '98117', '55117', '94608', '01824', '75204', '45218', '10003',
       '43221', '37412', '36106', '83702', '85016', '84604', '59801',
       '83686', '96819', '44092', '94551', '27514', '60008', '92374',
       '78213', '84107', '95129', '06811', '55108', '10019', '93109',
       '03261', '61755', '98225', '94025', '44691', '15222', '78212',
       '38115', '85711', '92626', '48103', '21206', '43215', '02140',
       '55105', '94533', '91606', '55422', '58644', '01602', '85258',
       '55414', '29205', '98199', '92629', '50311', '11211', '49705',
       '60007', '17345', '20009', '43204', '20817', '48076', '55013',
       '85282', '33308', '53202', '92653', '60201', '55113', '10021',
       '55021', '11758', '48446', '28018', '06333', '97330', '83709',
       '31820', '30011', 'Y1A6B', '29201', '60630', '98102', '02918',
       '75218', '94583', '05001', '90804', '91201', '02341', '78628',
       '10021', '77459', '87544', '94708', '93711', '75230', '60440',
       '02125', '10019', '55409', '98257', '37771', '40256', '43212',
       '21208', '95821', '93101', '92121', '21012', '45218', 'V5A2B',
       '53711', '94618', '60090', '49428', '03052', '55414', '50112',
       '55408', '75006', '94305', '10025', '23092', '27514', '92115',
       '20657', '03869', '28450', '19382', '10011', '98038', '21250',
       '20090', '26241', '20707', '49508', '10021', '55454', '99709',
       '55320', '12603', '02146', '55443', '04102', '02159', '19711',
       '97124', '12180', '55104', '44224', '94040', '97408', '92705',
       '02324', '05464', '80302', '30078', '22902', '21010', '80303',
       '91201', '84302', '60515', '95123', '29464', '08052', '22911',
       '14534', '95468', '45680', '95453', '55414', '68147', '62901',
       '62901', '23227', '30606', '11217', '63132', '10022', '10003',
       '60005', '20879', '32707', '94591', '55422', '14627', '10003',
       '01915', '91903', '14627', '01945', '20003', '48911', '53188',
       '46032', '98281', '77845', 'M7A1A', '48103', '17961', '94131',
       '93003', '29631', '27511', '98501', '79508', '14216', '93063',
       '90034', '82435', '92093', '97520', '68767', 'M4J2K', '31909',
       '77073', '84116', '43085', 'R3T5K', '02320', '99687', '34656',
       '47905', '11787', '33716', '63044', '02154', '10003', '55106',
       '21227', '77008', '79070', '29678', '80227', '27705', '50613',
       '11201', '44212', '44134', '81648', '60402', '14850', '60187',
       '30067', '20723', '19807', '08034', '94306', '44224', '55408',
       '38866', '55454', '55414', 'T8H1N', '23237', '48043', '74101',
       '01940', '12065', '61801', '60626', '95521', '55122', '63645',
       '53211', '51250', '45810', '91351', '39762', '83814', '02903',
       '22911', '55105', '78739', '60657', '10314', '78704', '92626',
       '54248', '77380', '98121', '19102', '19341', '94115', '55412',
       '61820', '01970', '10016', '20009', '21114', '91919', '90095',
       '22906', '55337', '28814', '32712', '99835', '61462', '54302',
       '90405', '97208', '55128', '23509', '55414', '55409', '26506',
       '27713', '60476', '45439', '63304', '60089', '18053', '85210',
       '06365', '38115', '94920', '77042', '06906', '96754', '76309',
       '56321', '89104', '49512', '91105', '54494', '55454', '19146',
       '96349', 'N4T1A', '92020', '15203', '54901', '07204', '55343',
       '91206', '44265', '84105', '64118', 'V0R2H', '16506', '11238',
       '17331', '94403', '40243', '91711', '80538', '78741', '94306',
       '56567', '32114', '70403', '98405', '60630', '63108', '85719',
       '94618', '98072', '95403', '73162', '22206', '63108', '29210',
       '92660', '47024', '55113', '19047', '93612', '94720', '80919',
       '32303', '90034', '21201', '91206', '62901', '97007', '90247',
       '55104', '53706', '68503', '14211', '97302', '95050', '02113',
       '62903', '33066', '10960', '00000', '12866', '06927', '14216',
       '15232', '27105', '55414', '80027', '90036', '51157', '01810',
       '01960', 'K7L5J', '94560', '48825', '33205', '77081', '91040',
       '23322', '01754', '98620', '05779', '55420', '80913', '20064',
       '12205', '85281', '57197', '08610', '33755', '62522', '64131',
       '19716', '55337', '92154', '34105', '78212', '61820', '20009',
       '11217', '93555', '90016', '30803', '80526', '73013', '76234',
       '02136', '12345', '28806', '20755', '60152', '27514', '40205',
       '37725', '77845', '53144', '50322', '15017', '05452', '77048',
       '80228', '85282', '80209', '53066', '33765', '77042', '90019',
       '64153', '11577', '10018', '55409', '01375', '90814', '55406',
       '47401', '93055', '44212', '95662', '97405', '47130', '55417',
       '02146', '25652', '78390', '29646', '94086', '40515', '55408',
       '04988', '97215', 'V1G4L', '09645', '06492', '48322', '14085',
       '13820', '60089', '63021', '11231', '60302', '92507', '55303',
       '10025', '65203', '44648', '74078', '33763', '37076', '35802',
       '20902', '77504', '98027', '55337', '83702', '43017', '40503',
       '50266', '55337', '95316', '61820', '27249', '17036', '78704',
       '97301', '03062', '45243', '95823', '74075', '32301', '91505',
       '33484', '61755', '55116', '18505', 'L1V3W', '97203', '20850',
       '61073', '30350', '70124', '80526', '68504', '53171', '29301',
       '53210', '06512', '76201', '08105', '60614', 'N2L5N', '20006',
       '70116', '14216', '90008', '98801', '21114', 'E2E3R', '11753',
       '49036', '01701', '55428', '55408', '53711', '07310', '33556',
       '06437', '48105', '22902', '66221', '32789', '98072', '55038',
       '33319', '02215', '97229', '78209', '77841'], dtype=object)
>>> df
     user_id  age gender     occupation zip_code
0          1   24      M     technician    85711
1          2   53      F             方法    94043
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
>>> df.occupation.unique()
array(['technician', '方法', 'writer', 'other', 'executive', 'administrator',
       'student', 'lawyer', 'educator', 'scientist', 'entertainment',
       'programmer', 'librarian', 'homemaker', 'artist', 'engineer',
       'marketing', 'none', 'healthcare', 'retired', 'salesman', 'doctor'], dtype=object)
>>> df.occupation.value_counts()
student          196
other            104
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
lawyer            12
salesman          12
none               9
homemaker          7
doctor             7
方法                 1
Name: occupation, dtype: int64
>>> gcnt = df.gender.value_counts()
>>> g
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    g
NameError: name 'g' is not defined
>>> gcnt
M    670
F    273
Name: gender, dtype: int64
>>> gcnt['M']/gcnt['F']
2.4542124542124544
>>> df
     user_id  age gender     occupation zip_code
0          1   24      M     technician    85711
1          2   53      F             方法    94043
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
>>> help(df.groupby)
Help on method groupby in module pandas.core.generic:

groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, **kwargs) method of pandas.core.frame.DataFrame instance
    Group series using mapper (dict or key function, apply given function
    to group, return result as series) or by a series of columns.
    
    Parameters
    ----------
    by : mapping, function, str, or iterable
        Used to determine the groups for the groupby.
        If ``by`` is a function, it's called on each value of the object's
        index. If a dict or Series is passed, the Series or dict VALUES
        will be used to determine the groups (the Series' values are first
        aligned; see ``.align()`` method). If an ndarray is passed, the
        values are used as-is determine the groups. A str or list of strs
        may be passed to group by the columns in ``self``
    axis : int, default 0
    level : int, level name, or sequence of such, default None
        If the axis is a MultiIndex (hierarchical), group by a particular
        level or levels
    as_index : boolean, default True
        For aggregated output, return object with group labels as the
        index. Only relevant for DataFrame input. as_index=False is
        effectively "SQL-style" grouped output
    sort : boolean, default True
        Sort group keys. Get better performance by turning this off.
        Note this does not influence the order of observations within each
        group.  groupby preserves the order of rows within each group.
    group_keys : boolean, default True
        When calling apply, add group keys to index to identify pieces
    squeeze : boolean, default False
        reduce the dimensionality of the return type if possible,
        otherwise return a consistent type
    
    Examples
    --------
    DataFrame results
    
    >>> data.groupby(func, axis=0).mean()
    >>> data.groupby(['col1', 'col2'])['col3'].mean()
    
    DataFrame with hierarchical index
    
    >>> data.groupby(['col1', 'col2']).mean()
    
    Returns
    -------
    GroupBy object

>>> df.groupby('gender')
<pandas.core.groupby.DataFrameGroupBy object at 0x04E44170>
>>> df.groupby('gender').mean()
           user_id        age
gender                       
F       481.406593  33.813187
M       468.167164  34.149254
>>> df.groupby('gender').age.mean()
gender
F    33.813187
M    34.149254
Name: age, dtype: float64
>>> df
     user_id  age gender     occupation zip_code
0          1   24      M     technician    85711
1          2   53      F             方法    94043
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
>>> df.groupby(['gender', 'occupation']).age.mean()
gender  occupation   
F       administrator    40.638889
        artist           30.307692
        educator         39.115385
        engineer         29.500000
        entertainment    31.000000
        executive        44.000000
        healthcare       39.818182
        homemaker        34.166667
        lawyer           39.500000
        librarian        40.000000
        marketing        37.200000
        none             36.500000
        other            34.971429
        programmer       32.166667
        retired          70.000000
        salesman         27.000000
        scientist        28.333333
        student          20.750000
        technician       38.000000
        writer           37.631579
        方法               53.000000
M       administrator    37.162791
        artist           32.333333
        doctor           43.571429
        educator         43.101449
        engineer         36.600000
        entertainment    29.000000
        executive        38.172414
        healthcare       45.400000
        homemaker        23.000000
        lawyer           36.200000
        librarian        40.000000
        marketing        37.875000
        none             18.600000
        other            34.028986
        programmer       33.216667
        retired          62.538462
        salesman         38.555556
        scientist        36.321429
        student          22.669118
        technician       32.961538
        writer           35.346154
Name: age, dtype: float64
>>> df
     user_id  age gender     occupation zip_code
0          1   24      M     technician    85711
1          2   53      F             方法    94043
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
>>> df1 = pd.DataFrame(np.random.randint(9, size=(5,3)),index=list('abcde'),columns=list('ABC'))
>>> df2 = pd.DataFrame(np.random.randint(9, size=(5,3)),index=list('yuiop'),columns=list('ABC'))
>>> df1
   A  B  C
a  1  6  1
b  7  7  5
c  7  3  6
d  1  2  1
e  4  3  7
>>> df2
   A  B  C
y  6  7  6
u  4  2  8
i  5  7  1
o  8  2  6
p  2  4  0
>>> pd.concat([df1, df2])
   A  B  C
a  1  6  1
b  7  7  5
c  7  3  6
d  1  2  1
e  4  3  7
y  6  7  6
u  4  2  8
i  5  7  1
o  8  2  6
p  2  4  0
>>> df3 = pd.DataFrame(np.random.randint(9, size=(5,3)),index=list('yuiop'),columns=list('ABD'))
>>> pd.concat([df1, df3])
   A  B    C    D
a  1  6  1.0  NaN
b  7  7  5.0  NaN
c  7  3  6.0  NaN
d  1  2  1.0  NaN
e  4  3  7.0  NaN
y  3  3  NaN  8.0
u  5  1  NaN  3.0
i  0  0  NaN  2.0
o  6  5  NaN  4.0
p  0  0  NaN  4.0
>>> pd.concat([df1, df3], fillna=0)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    pd.concat([df1, df3], fillna=0)
TypeError: concat() got an unexpected keyword argument 'fillna'
>>> 
KeyboardInterrupt
>>> pd.concat([df1, df3]).fillna(0)
   A  B    C    D
a  1  6  1.0  0.0
b  7  7  5.0  0.0
c  7  3  6.0  0.0
d  1  2  1.0  0.0
e  4  3  7.0  0.0
y  3  3  0.0  8.0
u  5  1  0.0  3.0
i  0  0  0.0  2.0
o  6  5  0.0  4.0
p  0  0  0.0  4.0
>>> df4 = pd.DataFrame(np.random.randint(9, size=(5,4)),index=list('yuiop'),columns=list('ABCD'))
>>> pd.concat([df1, df4])
   A  B  C    D
a  1  6  1  NaN
b  7  7  5  NaN
c  7  3  6  NaN
d  1  2  1  NaN
e  4  3  7  NaN
y  8  1  0  6.0
u  1  7  1  1.0
i  8  2  3  8.0
o  4  4  7  4.0
p  2  4  0  7.0
>>> df4 = pd.DataFrame(np.random.randint(9, size=(5,4)),index=list('yuiop'),columns=list('GHJK'))
>>> pd.concat([df1, df4])
     A    B    C    G    H    J    K
a  1.0  6.0  1.0  NaN  NaN  NaN  NaN
b  7.0  7.0  5.0  NaN  NaN  NaN  NaN
c  7.0  3.0  6.0  NaN  NaN  NaN  NaN
d  1.0  2.0  1.0  NaN  NaN  NaN  NaN
e  4.0  3.0  7.0  NaN  NaN  NaN  NaN
y  NaN  NaN  NaN  5.0  2.0  5.0  6.0
u  NaN  NaN  NaN  5.0  5.0  7.0  1.0
i  NaN  NaN  NaN  5.0  7.0  5.0  3.0
o  NaN  NaN  NaN  6.0  2.0  0.0  1.0
p  NaN  NaN  NaN  6.0  4.0  1.0  3.0
>>> df1
   A  B  C
a  1  6  1
b  7  7  5
c  7  3  6
d  1  2  1
e  4  3  7
>>> df2
   A  B  C
y  6  7  6
u  4  2  8
i  5  7  1
o  8  2  6
p  2  4  0
>>> df2 = pd.DataFrame(np.random.randint(9, size=(5,3)),index=list('cbdae'),columns=list('ABC'))
>>> df1
   A  B  C
a  1  6  1
b  7  7  5
c  7  3  6
d  1  2  1
e  4  3  7
>>> df2
   A  B  C
c  6  8  5
b  0  3  5
d  3  8  3
a  6  2  0
e  7  5  5
>>> pd.concat([df1, df2])
   A  B  C
a  1  6  1
b  7  7  5
c  7  3  6
d  1  2  1
e  4  3  7
c  6  8  5
b  0  3  5
d  3  8  3
a  6  2  0
e  7  5  5
>>> pd.concat([df1, df2], axis=1)
   A  B  C  A  B  C
a  1  6  1  6  2  0
b  7  7  5  0  3  5
c  7  3  6  6  8  5
d  1  2  1  3  8  3
e  4  3  7  7  5  5
>>> df.columns
Index(['user_id', 'age', 'gender', 'occupation', 'zip_code'], dtype='object')
>>> concated = pd.concat([df1, df2], axis=1)
>>> concated
   A  B  C  A  B  C
a  1  6  1  6  2  0
b  7  7  5  0  3  5
c  7  3  6  6  8  5
d  1  2  1  3  8  3
e  4  3  7  7  5  5
>>> concated.drop('C', axis=1)
   A  B  A  B
a  1  6  6  2
b  7  7  0  3
c  7  3  6  8
d  1  2  3  8
e  4  3  7  5
>>> users10 = df.head(10)
>>> users10
   user_id  age gender     occupation zip_code
0        1   24      M     technician    85711
1        2   53      F             方法    94043
2        3   23      M         writer    32067
3        4   24      M     technician    43537
4        5   33      F          other    15213
5        6   42      M      executive    98101
6        7   57      M  administrator    91344
7        8   36      M  administrator    05201
8        9   29      M        student    01002
9       10   53      M         lawyer    90703
>>> df2 = pd.DataFrame(np.random.randint(9, size=(5,3)),index=list('cbdaf'),columns=list('ABC'))
>>> concated = pd.concat([df1, df2], axis=1)
>>> concated.shape
(6, 6)
>>> concated
     A    B    C    A    B    C
a  1.0  6.0  1.0  4.0  8.0  6.0
b  7.0  7.0  5.0  6.0  3.0  7.0
c  7.0  3.0  6.0  2.0  5.0  1.0
d  1.0  2.0  1.0  4.0  3.0  6.0
e  4.0  3.0  7.0  NaN  NaN  NaN
f  NaN  NaN  NaN  1.0  1.0  6.0
>>> df1.reindex()
   A  B  C
a  1  6  1
b  7  7  5
c  7  3  6
d  1  2  1
e  4  3  7
>>> df1.reset_index()
  index  A  B  C
0     a  1  6  1
1     b  7  7  5
2     c  7  3  6
3     d  1  2  1
4     e  4  3  7
>>> df2.reset_index()
  index  A  B  C
0     c  2  5  1
1     b  6  3  7
2     d  4  3  6
3     a  4  8  6
4     f  1  1  6
>>> df1r = df1.reset_index()
>>> df2r = df2.reset_index()
>>> pd.concat([df1r, df2r])
  index  A  B  C
0     a  1  6  1
1     b  7  7  5
2     c  7  3  6
3     d  1  2  1
4     e  4  3  7
0     c  2  5  1
1     b  6  3  7
2     d  4  3  6
3     a  4  8  6
4     f  1  1  6
>>> pd.concat([df1r, df2r], axis=1)
  index  A  B  C index  A  B  C
0     a  1  6  1     c  2  5  1
1     b  7  7  5     b  6  3  7
2     c  7  3  6     d  4  3  6
3     d  1  2  1     a  4  8  6
4     e  4  3  7     f  1  1  6
>>> pd.concat([df1r, df2r], axis=1).drop('index',axis=1)
   A  B  C  A  B  C
0  1  6  1  2  5  1
1  7  7  5  6  3  7
2  7  3  6  4  3  6
3  1  2  1  4  8  6
4  4  3  7  1  1  6
>>> data = {'class':[1,1,2,2,2], 'xuehao':[22,34,56,4,32],'score':[66,77,55,67,87]}
>>> score = df.DataFrame(data)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    score = df.DataFrame(data)
  File "D:\Python36\lib\site-packages\pandas\core\generic.py", line 3081, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'DataFrame'
>>> score = pd.DataFrame(data)
>>> score
   class  score  xuehao
0      1     66      22
1      1     77      34
2      2     55      56
3      2     67       4
4      2     87      32
>>> users = pd.read_csv(r'E:\python_files\csv\users.csv')
>>> agemean = users.groupby(['gender', 'occupation']).age.mean()
>>> score2 = score.pivot(index='class', columns='xuehao', values=score)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    score2 = score.pivot(index='class', columns='xuehao', values=score)
  File "D:\Python36\lib\site-packages\pandas\core\frame.py", line 3853, in pivot
    return pivot(self, index=index, columns=columns, values=values)
  File "D:\Python36\lib\site-packages\pandas\core\reshape\reshape.py", line 376, in pivot
    indexed = Series(self[values].values,
  File "D:\Python36\lib\site-packages\pandas\core\frame.py", line 1960, in __getitem__
    return self._getitem_frame(key)
  File "D:\Python36\lib\site-packages\pandas\core\frame.py", line 2035, in _getitem_frame
    raise ValueError('Must pass DataFrame with boolean values only')
ValueError: Must pass DataFrame with boolean values only
>>> score2 = score.pivot(index='class', columns='xuehao', values='score')
>>> score
   class  score  xuehao
0      1     66      22
1      1     77      34
2      2     55      56
3      2     67       4
4      2     87      32
>>> score2
xuehao    4     22    32    34    56
class                               
1        NaN  66.0   NaN  77.0   NaN
2       67.0   NaN  87.0   NaN  55.0
>>> score2.T
class      1     2
xuehao            
4        NaN  67.0
22      66.0   NaN
32       NaN  87.0
34      77.0   NaN
56       NaN  55.0
>>> score
   class  score  xuehao
0      1     66      22
1      1     77      34
2      2     55      56
3      2     67       4
4      2     87      32
>>> score2.T.index
Int64Index([4, 22, 32, 34, 56], dtype='int64', name='xuehao')
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
>>> agemean
gender  occupation   
F       administrator    40.638889
        artist           30.307692
        educator         39.115385
        engineer         29.500000
        entertainment    31.000000
        executive        44.000000
        healthcare       39.818182
        homemaker        34.166667
        lawyer           39.500000
        librarian        40.000000
        marketing        37.200000
        none             36.500000
        other            35.472222
        programmer       32.166667
        retired          70.000000
        salesman         27.000000
        scientist        28.333333
        student          20.750000
        technician       38.000000
        writer           37.631579
M       administrator    37.162791
        artist           32.333333
        doctor           43.571429
        educator         43.101449
        engineer         36.600000
        entertainment    29.000000
        executive        38.172414
        healthcare       45.400000
        homemaker        23.000000
        lawyer           36.200000
        librarian        40.000000
        marketing        37.875000
        none             18.600000
        other            34.028986
        programmer       33.216667
        retired          62.538462
        salesman         38.555556
        scientist        36.321429
        student          22.669118
        technician       32.961538
        writer           35.346154
Name: age, dtype: float64
>>> agemean.columns
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    agemean.columns
  File "D:\Python36\lib\site-packages\pandas\core\generic.py", line 3077, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'columns'
>>> agemean.index
MultiIndex(levels=[['F', 'M'], ['administrator', 'artist', 'doctor', 'educator', 'engineer', 'entertainment', 'executive', 'healthcare', 'homemaker', 'lawyer', 'librarian', 'marketing', 'none', 'other', 'programmer', 'retired', 'salesman', 'scientist', 'student', 'technician', 'writer']],
           labels=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],
           names=['gender', 'occupation'])
>>> gender = agemean.index.labels[0]
>>> gender
FrozenNDArray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dtype='int8')
>>> occupation = agemean.index.labels[1]
>>> occupation
FrozenNDArray([0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], dtype='int8')
>>> data = {'gender':gender, 'occupation':occupation, 'meanage':meanage}
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    data = {'gender':gender, 'occupation':occupation, 'meanage':meanage}
NameError: name 'meanage' is not defined
>>> data = {'gender':gender, 'occupation':occupation, 'agemean':agemean}
>>> agemean2 = pd.DataFream(data)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    agemean2 = pd.DataFream(data)
AttributeError: module 'pandas' has no attribute 'DataFream'
>>> agemean2 = pd.DataFrame(data)
>>> agemean2
                        agemean  gender  occupation
gender occupation                                  
F      administrator  40.638889       0           0
       artist         30.307692       0           1
       educator       39.115385       0           3
       engineer       29.500000       0           4
       entertainment  31.000000       0           5
       executive      44.000000       0           6
       healthcare     39.818182       0           7
       homemaker      34.166667       0           8
       lawyer         39.500000       0           9
       librarian      40.000000       0          10
       marketing      37.200000       0          11
       none           36.500000       0          12
       other          35.472222       0          13
       programmer     32.166667       0          14
       retired        70.000000       0          15
       salesman       27.000000       0          16
       scientist      28.333333       0          17
       student        20.750000       0          18
       technician     38.000000       0          19
       writer         37.631579       0          20
M      administrator  37.162791       1           0
       artist         32.333333       1           1
       doctor         43.571429       1           2
       educator       43.101449       1           3
       engineer       36.600000       1           4
       entertainment  29.000000       1           5
       executive      38.172414       1           6
       healthcare     45.400000       1           7
       homemaker      23.000000       1           8
       lawyer         36.200000       1           9
       librarian      40.000000       1          10
       marketing      37.875000       1          11
       none           18.600000       1          12
       other          34.028986       1          13
       programmer     33.216667       1          14
       retired        62.538462       1          15
       salesman       38.555556       1          16
       scientist      36.321429       1          17
       student        22.669118       1          18
       technician     32.961538       1          19
       writer         35.346154       1          20
>>> agemean2.reset_index()
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    agemean2.reset_index()
  File "D:\Python36\lib\site-packages\pandas\core\frame.py", line 2958, in reset_index
    new_obj.insert(0, name, level_values)
  File "D:\Python36\lib\site-packages\pandas\core\frame.py", line 2423, in insert
    allow_duplicates=allow_duplicates)
  File "D:\Python36\lib\site-packages\pandas\core\internals.py", line 3810, in insert
    raise ValueError('cannot insert {}, already exists'.format(item))
ValueError: cannot insert occupation, already exists
>>> agemean2.index
MultiIndex(levels=[['F', 'M'], ['administrator', 'artist', 'doctor', 'educator', 'engineer', 'entertainment', 'executive', 'healthcare', 'homemaker', 'lawyer', 'librarian', 'marketing', 'none', 'other', 'programmer', 'retired', 'salesman', 'scientist', 'student', 'technician', 'writer']],
           labels=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],
           names=['gender', 'occupation'])
>>> agemean2.reindex()
                        agemean  gender  occupation
gender occupation                                  
F      administrator  40.638889       0           0
       artist         30.307692       0           1
       educator       39.115385       0           3
       engineer       29.500000       0           4
       entertainment  31.000000       0           5
       executive      44.000000       0           6
       healthcare     39.818182       0           7
       homemaker      34.166667       0           8
       lawyer         39.500000       0           9
       librarian      40.000000       0          10
       marketing      37.200000       0          11
       none           36.500000       0          12
       other          35.472222       0          13
       programmer     32.166667       0          14
       retired        70.000000       0          15
       salesman       27.000000       0          16
       scientist      28.333333       0          17
       student        20.750000       0          18
       technician     38.000000       0          19
       writer         37.631579       0          20
M      administrator  37.162791       1           0
       artist         32.333333       1           1
       doctor         43.571429       1           2
       educator       43.101449       1           3
       engineer       36.600000       1           4
       entertainment  29.000000       1           5
       executive      38.172414       1           6
       healthcare     45.400000       1           7
       homemaker      23.000000       1           8
       lawyer         36.200000       1           9
       librarian      40.000000       1          10
       marketing      37.875000       1          11
       none           18.600000       1          12
       other          34.028986       1          13
       programmer     33.216667       1          14
       retired        62.538462       1          15
       salesman       38.555556       1          16
       scientist      36.321429       1          17
       student        22.669118       1          18
       technician     32.961538       1          19
       writer         35.346154       1          20
>>> 
