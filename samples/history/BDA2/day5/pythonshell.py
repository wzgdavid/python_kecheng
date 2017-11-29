Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> arr = np.array([1,2,3,4])
>>> arr
array([1, 2, 3, 4])
>>> print(arr)
[1 2 3 4]
>>> print([1,2,3,4])
[1, 2, 3, 4]
>>> type(arr)
<class 'numpy.ndarray'>
>>> arr = np.ndarray([1,2,3,4])
>>> arr
array([[[[  1.23859045e-293,   1.28778178e-310,   2.15412622e-321,
            0.00000000e+000],
         [  0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
            1.03056301e-113],
         [  1.05894588e-153,   0.00000000e+000,   0.00000000e+000,
            0.00000000e+000]],

        [[  0.00000000e+000,   0.00000000e+000,   4.24399158e-314,
            4.94065646e-324],
         [  0.00000000e+000,   0.00000000e+000,   6.96853406e-293,
            0.00000000e+000],
         [  5.40541212e+257,   5.56206104e+180,   8.17434450e+141,
            6.09343068e-013]]]])
>>> arr = np.array([1,2,3,4])
>>> arr
array([1, 2, 3, 4])
>>> lst = [1,2,3,4]
>>> arr.dtype
dtype('int32')
>>> np.float8
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    np.float8
AttributeError: module 'numpy' has no attribute 'float8'
>>> np.int8
<class 'numpy.int8'>
>>> np.float16
<class 'numpy.float16'>
>>> arr = np.array(lst, dtype=np.int8)
>>> arr
array([1, 2, 3, 4], dtype=int8)
>>> arr = np.array(lst, dtype=int)
>>> arr
array([1, 2, 3, 4])
>>> arr.dtype
dtype('int32')
>>> arr2d = np.array([[1, 2, 4],[5,6,7]])
>>> arr2d
array([[1, 2, 4],
       [5, 6, 7]])
>>> arr2d = np.array([(1, 2, 4),(5,6,7)])
>>> arr2d
array([[1, 2, 4],
       [5, 6, 7]])
>>> np.array([(1, 2, 4),(5, 6, 7, 8)])
array([(1, 2, 4), (5, 6, 7, 8)], dtype=object)
>>> arr2d.ndim
2
>>> arr1 = np.array([(1, 2, 4),(5, 6, 7, 8)])
>>> arr1.ndim
1
>>> arr1.size
2
>>> print(arr1)
[(1, 2, 4) (5, 6, 7, 8)]
>>> print(arr2d)
[[1 2 4]
 [5 6 7]]
>>> arr2d
array([[1, 2, 4],
       [5, 6, 7]])
>>> arr1 = np.array(range(1,11))
>>> arr1
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
>>> arr1 = np.arange(10)
>>> arr1
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> arr1 = np.array(range(1,11),range(1,11))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    arr1 = np.array(range(1,11),range(1,11))
TypeError: data type not understood
>>> arr1 = np.array([range(1,11),range(1,11)])
>>> arr1
array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10],
       [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10]])
>>> print(arr1)
[[ 1  2  3  4  5  6  7  8  9 10]
 [ 1  2  3  4  5  6  7  8  9 10]]
>>> arr1 = np.arange(10).reshape(4, 2)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    arr1 = np.arange(10).reshape(4, 2)
ValueError: cannot reshape array of size 10 into shape (4,2)
>>> arr1 = np.arange(10).reshape(5, 2)
>>> arr1
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])
>>> arr1 = np.arange(10).reshape(2, 5)
>>> arr1
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
>>> arr1 = np.arange(10).reshape(2, -1)
>>> arr1
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
>>> arr1 = np.arange(24).reshape(12, -1)
>>> arr1
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15],
       [16, 17],
       [18, 19],
       [20, 21],
       [22, 23]])
>>> arr1 = np.arange(24).reshape(13, -1)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    arr1 = np.arange(24).reshape(13, -1)
ValueError: cannot reshape array of size 24 into shape (13,newaxis)
>>> arr1 = np.arange(24).reshape(-1, 6)
>>> arr1
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23]])
>>> np.arange(10, 30, 4)
array([10, 14, 18, 22, 26])
>>> np.zeros((3,4))
array([[ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.]])
>>> arr1.shape
(4, 6)
>>> np.zeros((3,4)).shape
(3, 4)
>>> np.zeros((3,4)).dtype
dtype('float64')
>>> np.ones((2,3,4))
array([[[ 1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.]],

       [[ 1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.]]])
>>> print(np.ones((2,3,4)))
[[[ 1.  1.  1.  1.]
  [ 1.  1.  1.  1.]
  [ 1.  1.  1.  1.]]

 [[ 1.  1.  1.  1.]
  [ 1.  1.  1.  1.]
  [ 1.  1.  1.  1.]]]
>>> print(np.ones((2,3,4,3)))
[[[[ 1.  1.  1.]
   [ 1.  1.  1.]
   [ 1.  1.  1.]
   [ 1.  1.  1.]]

  [[ 1.  1.  1.]
   [ 1.  1.  1.]
   [ 1.  1.  1.]
   [ 1.  1.  1.]]

  [[ 1.  1.  1.]
   [ 1.  1.  1.]
   [ 1.  1.  1.]
   [ 1.  1.  1.]]]


 [[[ 1.  1.  1.]
   [ 1.  1.  1.]
   [ 1.  1.  1.]
   [ 1.  1.  1.]]

  [[ 1.  1.  1.]
   [ 1.  1.  1.]
   [ 1.  1.  1.]
   [ 1.  1.  1.]]

  [[ 1.  1.  1.]
   [ 1.  1.  1.]
   [ 1.  1.  1.]
   [ 1.  1.  1.]]]]
>>> a = np.arange(12).reshape(4)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a = np.arange(12).reshape(4)
ValueError: cannot reshape array of size 12 into shape (4,)
>>> a = np.arange(12).reshape(4,3)
>>> a.size
12
>>> a = np.arange(12).reshape(2,2,3)
>>> a
array([[[ 0,  1,  2],
        [ 3,  4,  5]],

       [[ 6,  7,  8],
        [ 9, 10, 11]]])
>>> a = np.arange(12).reshape(2,2,-1)
>>> a
array([[[ 0,  1,  2],
        [ 3,  4,  5]],

       [[ 6,  7,  8],
        [ 9, 10, 11]]])
>>> a = np.arange(12).reshape(2,-1,-1)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a = np.arange(12).reshape(2,-1,-1)
ValueError: can only specify one unknown dimension
>>> a = np.arange(12).reshape(2,-1,2)
>>> a
array([[[ 0,  1],
        [ 2,  3],
        [ 4,  5]],

       [[ 6,  7],
        [ 8,  9],
        [10, 11]]])
>>> import random
>>> random.random()
0.18372366042057997
>>> np.random.rand(3,2)
array([[ 0.25867431,  0.00476546],
       [ 0.55942489,  0.38333464],
       [ 0.57182453,  0.50941793]])
>>> np.random.rand(3)
array([ 0.11333444,  0.08992443,  0.16816647])
>>> b = np.random.rand()
>>> b
0.08340051569763685
>>> type(b)
<class 'float'>
>>> np.random.randint(9, size=9)
array([2, 1, 7, 0, 4, 6, 5, 5, 7])
>>> np.random.randint(9, size=(4,5))
array([[5, 7, 4, 0, 0],
       [3, 2, 4, 3, 5],
       [7, 7, 6, 2, 8],
       [4, 1, 2, 4, 2]])
>>> arr = np.arange(10)
>>> np.random.shuffle(arr)
>>> arr
array([5, 2, 9, 8, 4, 7, 3, 0, 6, 1])
>>> np.random.shuffle(arr)
>>> arr
array([4, 2, 3, 5, 9, 0, 6, 1, 8, 7])
>>> arr = np.arange(12).reshape(3,4)
>>> arr
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> np.random.shuffle(arr)
>>> arr
array([[ 8,  9, 10, 11],
       [ 4,  5,  6,  7],
       [ 0,  1,  2,  3]])
>>> np.random.shuffle(arr)
>>> arr
array([[ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [ 0,  1,  2,  3]])
>>> help(np.random.shuffle)
Help on built-in function shuffle:

shuffle(...) method of mtrand.RandomState instance
    shuffle(x)
    
    Modify a sequence in-place by shuffling its contents.
    
    This function only shuffles the array along the first axis of a
    multi-dimensional array. The order of sub-arrays is changed but
    their contents remains the same.
    
    Parameters
    ----------
    x : array_like
        The array or list to be shuffled.
    
    Returns
    -------
    None
    
    Examples
    --------
    >>> arr = np.arange(10)
    >>> np.random.shuffle(arr)
    >>> arr
    [1 7 5 2 9 4 3 6 0 8]
    
    Multi-dimensional arrays are only shuffled along the first axis:
    
    >>> arr = np.arange(9).reshape((3, 3))
    >>> np.random.shuffle(arr)
    >>> arr
    array([[3, 4, 5],
           [6, 7, 8],
           [0, 1, 2]])

>>> arr = np.arange(12)
>>> np.random.shuffle(arr)
>>> np.random.reshape(arr)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    np.random.reshape(arr)
AttributeError: module 'numpy.random' has no attribute 'reshape'
>>> arr.reshape(3,4)
array([[ 8,  0, 10,  7],
       [ 5,  3,  4,  2],
       [ 1,  9, 11,  6]])
>>> arr = np.arange(1, 10)
>>> np.random.shuffle(arr)
>>> arr
array([9, 7, 5, 2, 1, 8, 4, 6, 3])
>>> arr.reshape(3, 3)
array([[9, 7, 5],
       [2, 1, 8],
       [4, 6, 3]])
>>> arr.reshape(3, 3)
array([[9, 7, 5],
       [2, 1, 8],
       [4, 6, 3]])
>>> arr
array([9, 7, 5, 2, 1, 8, 4, 6, 3])
>>> lst = [1,2,3]
>>> arr
array([9, 7, 5, 2, 1, 8, 4, 6, 3])
>>> arr[0]
9
>>> arr[-1]
3
>>> arr[0:4]
array([9, 7, 5, 2])
>>> arr[-4:-1]
array([8, 4, 6])
>>> arr[90:]
array([], dtype=int32)
>>> arr
array([9, 7, 5, 2, 1, 8, 4, 6, 3])
>>> arr[0] = 8
>>> arr
array([8, 7, 5, 2, 1, 8, 4, 6, 3])
>>> arr[0: 5] = 88
>>> arr
array([88, 88, 88, 88, 88,  8,  4,  6,  3])
>>> aslice = arr[0: 5]
>>> aslice = 90
>>> arr
array([88, 88, 88, 88, 88,  8,  4,  6,  3])
>>> aslice
90
>>> aslice = arr[1: 5]
>>> aslice
array([88, 88, 88, 88])
>>> arr[1: 5] = 4
>>> aslice
array([4, 4, 4, 4])
>>> arr[:] = 1
>>> aslice
array([1, 1, 1, 1])
>>> aslice = arr[1: 5].copy()
>>> arr[:] = 11
>>> aslice
array([1, 1, 1, 1])
>>> arr
array([11, 11, 11, 11, 11, 11, 11, 11, 11])
>>> a = np.arange(1, 10).reshape(3,3)
>>> a[2]
array([7, 8, 9])
>>> a[:2]
array([[1, 2, 3],
       [4, 5, 6]])
>>> a[:2,:1]
array([[1],
       [4]])
>>> a[1,:2]
array([4, 5])
>>> a = np.arange(12)
>>> a
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
>>> i = np.array([1,1,3,8,5])
>>> a = np.arange(12)**2
>>> a
array([  0,   1,   4,   9,  16,  25,  36,  49,  64,  81, 100, 121], dtype=int32)
>>> a[i]
array([ 1,  1,  9, 64, 25], dtype=int32)
>>> j = np.array([[1,2],[3,4]])
>>> j
array([[1, 2],
       [3, 4]])
>>> a[j]
array([[ 1,  4],
       [ 9, 16]], dtype=int32)
>>> j = p.array([[9,7],[3,4]])
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    j = p.array([[9,7],[3,4]])
NameError: name 'p' is not defined
>>> j = np.array([[9,7],[3,4]])
>>> a[j]
array([[81, 49],
       [ 9, 16]], dtype=int32)
>>> a = np.arange(12).reshape(3,4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> i = np.array([1,2], [2,3])
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    i = np.array([1,2], [2,3])
TypeError: data type not understood
>>> i = np.array([[1,2], [2,3]])
>>> j = np.array([[2,1], [3,3]])
>>> a[i,j]
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    a[i,j]
IndexError: index 3 is out of bounds for axis 0 with size 3
>>> i = np.array([[1,2], [2,0]])
>>> j = np.array([[2,1], [3,3]])
>>> a[i, j]
array([[ 6,  9],
       [11,  3]])
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> a[i, 2]
array([[ 6, 10],
       [10,  2]])
>>> a[:, j]
array([[[ 2,  1],
        [ 3,  3]],

       [[ 6,  5],
        [ 7,  7]],

       [[10,  9],
        [11, 11]]])
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> j
array([[2, 1],
       [3, 3]])
>>> a = np.ran
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    a = np.ran
AttributeError: module 'numpy' has no attribute 'ran'
>>> a = np.random.randint(9, size=(3,3))
>>> a
array([[3, 7, 5],
       [4, 2, 1],
       [8, 7, 2]])
>>> print(a)
[[3 7 5]
 [4 2 1]
 [8 7 2]]
>>> a.sum()
39
>>> a.sum(axis=0)
array([15, 16,  8])
>>> a.sum(axis=1)
array([15,  7, 17])
>>> a.max(0)[8 7 2]]
SyntaxError: invalid syntax
>>> a.max(0)
array([8, 7, 5])
>>> a.max(1)
array([7, 4, 8])
>>> a.argmax(0)
array([2, 0, 0], dtype=int32)
>>> a.mean(0)
array([ 5.        ,  5.33333333,  2.66666667])
>>> a.std(0)
array([ 2.1602469 ,  2.3570226 ,  1.69967317])
>>> a
array([[3, 7, 5],
       [4, 2, 1],
       [8, 7, 2]])
>>> a.var(0)
array([ 4.66666667,  5.55555556,  2.88888889])
>>> a.cumsum(0)
array([[ 3,  7,  5],
       [ 7,  9,  6],
       [15, 16,  8]], dtype=int32)
>>> a.cumsum(1)
array([[ 3, 10, 15],
       [ 4,  6,  7],
       [ 8, 15, 17]], dtype=int32)
>>> a
array([[3, 7, 5],
       [4, 2, 1],
       [8, 7, 2]])
>>> a2 = np.ones((3,3))
>>> a2
array([[ 1.,  1.,  1.],
       [ 1.,  1.,  1.],
       [ 1.,  1.,  1.]])
>>> a + a2
array([[ 4.,  8.,  6.],
       [ 5.,  3.,  2.],
       [ 9.,  8.,  3.]])
>>> a
array([[3, 7, 5],
       [4, 2, 1],
       [8, 7, 2]])
>>> a * a2
array([[ 3.,  7.,  5.],
       [ 4.,  2.,  1.],
       [ 8.,  7.,  2.]])
>>> a - a2
array([[ 2.,  6.,  4.],
       [ 3.,  1.,  0.],
       [ 7.,  6.,  1.]])
>>> a
array([[3, 7, 5],
       [4, 2, 1],
       [8, 7, 2]])
>>> a+1
array([[4, 8, 6],
       [5, 3, 2],
       [9, 8, 3]])
>>> a**2
array([[ 9, 49, 25],
       [16,  4,  1],
       [64, 49,  4]], dtype=int32)
>>> a<4
array([[ True, False, False],
       [False,  True,  True],
       [False, False,  True]], dtype=bool)
>>> a!=4
array([[ True,  True,  True],
       [False,  True,  True],
       [ True,  True,  True]], dtype=bool)
>>> a
array([[3, 7, 5],
       [4, 2, 1],
       [8, 7, 2]])
>>> a *= 3
>>> a
array([[ 9, 21, 15],
       [12,  6,  3],
       [24, 21,  6]])
>>> a= a*3
>>> a
array([[27, 63, 45],
       [36, 18,  9],
       [72, 63, 18]])
>>> a
array([[27, 63, 45],
       [36, 18,  9],
       [72, 63, 18]])
>>> a+1
array([[28, 64, 46],
       [37, 19, 10],
       [73, 64, 19]])
>>> a
array([[27, 63, 45],
       [36, 18,  9],
       [72, 63, 18]])
>>> a+=1
>>> a
array([[28, 64, 46],
       [37, 19, 10],
       [73, 64, 19]])
>>> a[1]
array([37, 19, 10])
>>> a>20
array([[ True,  True,  True],
       [ True, False, False],
       [ True,  True, False]], dtype=bool)
>>> a[a>20]
array([28, 64, 46, 37, 73, 64])
>>> a[(a>20) & (a<50)]
array([28, 46, 37])
>>> a[(a>20) | (a<50)]
array([28, 64, 46, 37, 19, 10, 73, 64, 19])
>>> (a>20)
array([[ True,  True,  True],
       [ True, False, False],
       [ True,  True, False]], dtype=bool)
>>> a.sum()
360
>>> (a>20).sum()
6
>>> (a>20).sum(1)
array([3, 1, 2])
>>> (a>20).sum(0)
array([3, 2, 1])
>>> sdfsd and dfsfd and sdfsf
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    sdfsd and dfsfd and sdfsf
NameError: name 'sdfsd' is not defined
>>> all([1,1,1,0])
False
>>> any[[1,1,1,0]]
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    any[[1,1,1,0]]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> any([1,1,1,0])
True
>>> 1 or 1 or 1
1
>>> a
array([[28, 64, 46],
       [37, 19, 10],
       [73, 64, 19]])
>>> (a>20).all()
False
>>> (a>20).any()
True
>>> a2 = np.array([1,2,3,4])
>>> a2 = np.array([])
>>> (a2>10)
array([], dtype=bool)
>>> (a2>10).all()
True
>>> (a2>10).any()
False
>>> all([])
True
>>> all([1,1,1,0])
False
>>> any([])
False
>>> a2
array([], dtype=float64)
>>> arr = np.random.randint(1, 10, size=(9,3) )
>>> arr
array([[5, 3, 4],
       [5, 8, 9],
       [2, 7, 5],
       [1, 8, 7],
       [7, 5, 6],
       [2, 6, 4],
       [9, 9, 7],
       [3, 7, 4],
       [8, 6, 7]])
>>> arr>6
array([[False, False, False],
       [False,  True,  True],
       [False,  True, False],
       [False,  True,  True],
       [ True, False, False],
       [False, False, False],
       [ True,  True,  True],
       [False,  True, False],
       [ True, False,  True]], dtype=bool)
>>> (arr>6).sum(0)
array([3, 5, 4])
>>> arr>3
array([[ True, False,  True],
       [ True,  True,  True],
       [False,  True,  True],
       [False,  True,  True],
       [ True,  True,  True],
       [False,  True,  True],
       [ True,  True,  True],
       [False,  True,  True],
       [ True,  True,  True]], dtype=bool)
>>> (arr>3).sum(1)
array([2, 3, 2, 2, 3, 2, 3, 2, 3])
>>> a = (arr>3).sum(1)
>>> a[a==3].sum()
12
>>> (a==3).sum()
4
>>> a
array([2, 3, 2, 2, 3, 2, 3, 2, 3])
>>> a+1
array([3, 4, 3, 3, 4, 3, 4, 3, 4])
>>> np.abs(a)
array([2, 3, 2, 2, 3, 2, 3, 2, 3])
>>> np.sign(a)
array([1, 1, 1, 1, 1, 1, 1, 1, 1])
>>> a  = np.array([1,1,-2,-4])
>>> np.sign(a)
array([ 1,  1, -1, -1])
>>> a
array([ 1,  1, -2, -4])
>>> a
array([ 1,  1, -2, -4])
>>> a[-1] = np.nan
Traceback (most recent call last):
  File "<pyshell#243>", line 1, in <module>
    a[-1] = np.nan
ValueError: cannot convert float NaN to integer
>>> a[1] = np.nan
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    a[1] = np.nan
ValueError: cannot convert float NaN to integer
>>> a[1]
1
>>> a[1:2] = np.nan
Traceback (most recent call last):
  File "<pyshell#246>", line 1, in <module>
    a[1:2] = np.nan
ValueError: cannot convert float NaN to integer
>>> a.astype(np.object)
array([1, 1, -2, -4], dtype=object)
>>> a[1] = np.nan
Traceback (most recent call last):
  File "<pyshell#248>", line 1, in <module>
    a[1] = np.nan
ValueError: cannot convert float NaN to integer
>>> a = np.arange([1,2,3,None])
Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    a = np.arange([1,2,3,None])
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> a = np.array([1,2,3,None])
>>> a
array([1, 2, 3, None], dtype=object)
>>> a = np.array([1,2,3,np.nan])
>>> a
array([  1.,   2.,   3.,  nan])
>>> np.isnan(a)
array([False, False, False,  True], dtype=bool)
>>> a.isnan()
Traceback (most recent call last):
  File "<pyshell#255>", line 1, in <module>
    a.isnan()
AttributeError: 'numpy.ndarray' object has no attribute 'isnan'
>>> np.notnan(a)
Traceback (most recent call last):
  File "<pyshell#256>", line 1, in <module>
    np.notnan(a)
AttributeError: module 'numpy' has no attribute 'notnan'
>>> dir(np)
['ALLOW_THREADS', 'AxisError', 'BUFSIZE', 'CLIP', 'ComplexWarning', 'DataSource', 'ERR_CALL', 'ERR_DEFAULT', 'ERR_IGNORE', 'ERR_LOG', 'ERR_PRINT', 'ERR_RAISE', 'ERR_WARN', 'FLOATING_POINT_SUPPORT', 'FPE_DIVIDEBYZERO', 'FPE_INVALID', 'FPE_OVERFLOW', 'FPE_UNDERFLOW', 'False_', 'Inf', 'Infinity', 'MAXDIMS', 'MAY_SHARE_BOUNDS', 'MAY_SHARE_EXACT', 'MachAr', 'ModuleDeprecationWarning', 'NAN', 'NINF', 'NZERO', 'NaN', 'PINF', 'PZERO', 'PackageLoader', 'RAISE', 'RankWarning', 'SHIFT_DIVIDEBYZERO', 'SHIFT_INVALID', 'SHIFT_OVERFLOW', 'SHIFT_UNDERFLOW', 'ScalarType', 'Tester', 'TooHardError', 'True_', 'UFUNC_BUFSIZE_DEFAULT', 'UFUNC_PYVALS_NAME', 'VisibleDeprecationWarning', 'WRAP', '_NoValue', '__NUMPY_SETUP__', '__all__', '__builtins__', '__cached__', '__config__', '__doc__', '__file__', '__git_revision__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_distributor_init', '_globals', '_import_tools', '_mat', 'abs', 'absolute', 'absolute_import', 'add', 'add_docstring', 'add_newdoc', 'add_newdoc_ufunc', 'add_newdocs', 'alen', 'all', 'allclose', 'alltrue', 'amax', 'amin', 'angle', 'any', 'append', 'apply_along_axis', 'apply_over_axes', 'arange', 'arccos', 'arccosh', 'arcsin', 'arcsinh', 'arctan', 'arctan2', 'arctanh', 'argmax', 'argmin', 'argpartition', 'argsort', 'argwhere', 'around', 'array', 'array2string', 'array_equal', 'array_equiv', 'array_repr', 'array_split', 'array_str', 'asanyarray', 'asarray', 'asarray_chkfinite', 'ascontiguousarray', 'asfarray', 'asfortranarray', 'asmatrix', 'asscalar', 'atleast_1d', 'atleast_2d', 'atleast_3d', 'average', 'bartlett', 'base_repr', 'bench', 'binary_repr', 'bincount', 'bitwise_and', 'bitwise_not', 'bitwise_or', 'bitwise_xor', 'blackman', 'block', 'bmat', 'bool', 'bool8', 'bool_', 'broadcast', 'broadcast_arrays', 'broadcast_to', 'busday_count', 'busday_offset', 'busdaycalendar', 'byte', 'byte_bounds', 'bytes0', 'bytes_', 'c_', 'can_cast', 'cast', 'cbrt', 'cdouble', 'ceil', 'cfloat', 'char', 'character', 'chararray', 'choose', 'clip', 'clongdouble', 'clongfloat', 'column_stack', 'common_type', 'compare_chararrays', 'compat', 'complex', 'complex128', 'complex64', 'complex_', 'complexfloating', 'compress', 'concatenate', 'conj', 'conjugate', 'convolve', 'copy', 'copysign', 'copyto', 'core', 'corrcoef', 'correlate', 'cos', 'cosh', 'count_nonzero', 'cov', 'cross', 'csingle', 'ctypeslib', 'cumprod', 'cumproduct', 'cumsum', 'datetime64', 'datetime_as_string', 'datetime_data', 'deg2rad', 'degrees', 'delete', 'deprecate', 'deprecate_with_doc', 'diag', 'diag_indices', 'diag_indices_from', 'diagflat', 'diagonal', 'diff', 'digitize', 'disp', 'divide', 'division', 'divmod', 'dot', 'double', 'dsplit', 'dstack', 'dtype', 'e', 'ediff1d', 'einsum', 'einsum_path', 'emath', 'empty', 'empty_like', 'equal', 'errstate', 'euler_gamma', 'exp', 'exp2', 'expand_dims', 'expm1', 'extract', 'eye', 'fabs', 'fastCopyAndTranspose', 'fft', 'fill_diagonal', 'find_common_type', 'finfo', 'fix', 'flatiter', 'flatnonzero', 'flexible', 'flip', 'fliplr', 'flipud', 'float', 'float16', 'float32', 'float64', 'float_', 'float_power', 'floating', 'floor', 'floor_divide', 'fmax', 'fmin', 'fmod', 'format_parser', 'frexp', 'frombuffer', 'fromfile', 'fromfunction', 'fromiter', 'frompyfunc', 'fromregex', 'fromstring', 'full', 'full_like', 'fv', 'generic', 'genfromtxt', 'geomspace', 'get_array_wrap', 'get_include', 'get_printoptions', 'getbufsize', 'geterr', 'geterrcall', 'geterrobj', 'gradient', 'greater', 'greater_equal', 'half', 'hamming', 'hanning', 'heaviside', 'histogram', 'histogram2d', 'histogramdd', 'hsplit', 'hstack', 'hypot', 'i0', 'identity', 'iinfo', 'imag', 'in1d', 'index_exp', 'indices', 'inexact', 'inf', 'info', 'infty', 'inner', 'insert', 'int', 'int0', 'int16', 'int32', 'int64', 'int8', 'int_', 'int_asbuffer', 'intc', 'integer', 'interp', 'intersect1d', 'intp', 'invert', 'ipmt', 'irr', 'is_busday', 'isclose', 'iscomplex', 'iscomplexobj', 'isfinite', 'isfortran', 'isin', 'isinf', 'isnan', 'isnat', 'isneginf', 'isposinf', 'isreal', 'isrealobj', 'isscalar', 'issctype', 'issubclass_', 'issubdtype', 'issubsctype', 'iterable', 'ix_', 'kaiser', 'kron', 'ldexp', 'left_shift', 'less', 'less_equal', 'lexsort', 'lib', 'linalg', 'linspace', 'little_endian', 'load', 'loads', 'loadtxt', 'log', 'log10', 'log1p', 'log2', 'logaddexp', 'logaddexp2', 'logical_and', 'logical_not', 'logical_or', 'logical_xor', 'logspace', 'long', 'longcomplex', 'longdouble', 'longfloat', 'longlong', 'lookfor', 'ma', 'mafromtxt', 'mask_indices', 'mat', 'math', 'matmul', 'matrix', 'matrixlib', 'max', 'maximum', 'maximum_sctype', 'may_share_memory', 'mean', 'median', 'memmap', 'meshgrid', 'mgrid', 'min', 'min_scalar_type', 'minimum', 'mintypecode', 'mirr', 'mod', 'modf', 'moveaxis', 'msort', 'multiply', 'nan', 'nan_to_num', 'nanargmax', 'nanargmin', 'nancumprod', 'nancumsum', 'nanmax', 'nanmean', 'nanmedian', 'nanmin', 'nanpercentile', 'nanprod', 'nanstd', 'nansum', 'nanvar', 'nbytes', 'ndarray', 'ndenumerate', 'ndfromtxt', 'ndim', 'ndindex', 'nditer', 'negative', 'nested_iters', 'newaxis', 'nextafter', 'nonzero', 'not_equal', 'nper', 'npv', 'numarray', 'number', 'obj2sctype', 'object', 'object0', 'object_', 'ogrid', 'oldnumeric', 'ones', 'ones_like', 'outer', 'packbits', 'pad', 'partition', 'percentile', 'pi', 'piecewise', 'pkgload', 'place', 'pmt', 'poly', 'poly1d', 'polyadd', 'polyder', 'polydiv', 'polyfit', 'polyint', 'polymul', 'polynomial', 'polysub', 'polyval', 'positive', 'power', 'ppmt', 'print_function', 'prod', 'product', 'promote_types', 'ptp', 'put', 'putmask', 'pv', 'r_', 'rad2deg', 'radians', 'random', 'rank', 'rate', 'ravel', 'ravel_multi_index', 'real', 'real_if_close', 'rec', 'recarray', 'recfromcsv', 'recfromtxt', 'reciprocal', 'record', 'remainder', 'repeat', 'require', 'reshape', 'resize', 'result_type', 'right_shift', 'rint', 'roll', 'rollaxis', 'roots', 'rot90', 'round', 'round_', 'row_stack', 's_', 'safe_eval', 'save', 'savetxt', 'savez', 'savez_compressed', 'sctype2char', 'sctypeDict', 'sctypeNA', 'sctypes', 'searchsorted', 'select', 'set_numeric_ops', 'set_printoptions', 'set_string_function', 'setbufsize', 'setdiff1d', 'seterr', 'seterrcall', 'seterrobj', 'setxor1d', 'shape', 'shares_memory', 'short', 'show_config', 'sign', 'signbit', 'signedinteger', 'sin', 'sinc', 'single', 'singlecomplex', 'sinh', 'size', 'sometrue', 'sort', 'sort_complex', 'source', 'spacing', 'split', 'sqrt', 'square', 'squeeze', 'stack', 'std', 'str', 'str0', 'str_', 'string_', 'subtract', 'sum', 'swapaxes', 'sys', 'take', 'tan', 'tanh', 'tensordot', 'test', 'testing', 'tile', 'timedelta64', 'trace', 'tracemalloc_domain', 'transpose', 'trapz', 'tri', 'tril', 'tril_indices', 'tril_indices_from', 'trim_zeros', 'triu', 'triu_indices', 'triu_indices_from', 'true_divide', 'trunc', 'typeDict', 'typeNA', 'typecodes', 'typename', 'ubyte', 'ufunc', 'uint', 'uint0', 'uint16', 'uint32', 'uint64', 'uint8', 'uintc', 'uintp', 'ulonglong', 'unicode', 'unicode_', 'union1d', 'unique', 'unpackbits', 'unravel_index', 'unsignedinteger', 'unwrap', 'ushort', 'vander', 'var', 'vdot', 'vectorize', 'version', 'void', 'void0', 'vsplit', 'vstack', 'warnings', 'where', 'who', 'zeros', 'zeros_like']
>>> a
array([  1.,   2.,   3.,  nan])
>>> arr
array([[5, 3, 4],
       [5, 8, 9],
       [2, 7, 5],
       [1, 8, 7],
       [7, 5, 6],
       [2, 6, 4],
       [9, 9, 7],
       [3, 7, 4],
       [8, 6, 7]])
>>> np.where(a>5, 1, 0)

Warning (from warnings module):
  File "__main__", line 1
RuntimeWarning: invalid value encountered in greater
array([0, 0, 0, 0])
>>> np.where(arr>5, 1, 0)
array([[0, 0, 0],
       [0, 1, 1],
       [0, 1, 0],
       [0, 1, 1],
       [1, 0, 1],
       [0, 1, 0],
       [1, 1, 1],
       [0, 1, 0],
       [1, 1, 1]])
>>> arr
array([[5, 3, 4],
       [5, 8, 9],
       [2, 7, 5],
       [1, 8, 7],
       [7, 5, 6],
       [2, 6, 4],
       [9, 9, 7],
       [3, 7, 4],
       [8, 6, 7]])
>>> np.where(arr>5, arr, 0)
array([[0, 0, 0],
       [0, 8, 9],
       [0, 7, 0],
       [0, 8, 7],
       [7, 0, 6],
       [0, 6, 0],
       [9, 9, 7],
       [0, 7, 0],
       [8, 6, 7]])
>>> np.unique(arr)
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> 1 in [1,2,3]
True
>>> np.in1d(1, arr)
array([ True], dtype=bool)
>>> np.in1d(arr, arr)
array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True], dtype=bool)
>>> np.in1d(np.array([1,2]), arr)
array([ True,  True], dtype=bool)
>>> np.in1d(np.array([1,22]), arr)
array([ True, False], dtype=bool)
>>> 
