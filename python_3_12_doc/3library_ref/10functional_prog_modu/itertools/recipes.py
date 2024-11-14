import collections
import contextlib
import functools
import math
import operator
import random

from itertools import *
from collections.abc import Iterable #collections.abc和collection并没有关系，😅

#1.
def take(n, iterable):
    '''
        返回可迭代对象的第n个对象，允许iterable像list一样，按下标取得前n个
    '''
    return list( islice(iterable, n)) #from itertools import *就好了，原来显示islice没定义

k= range(1,5)
print( isinstance(k, Iterable)) #检查是否是可迭代对象，已经被import了，可以直接使用，注意名命空间
#但是确定一个对象是否是Iterable的办法其实是调用Iter(obj)
print( take(3, k))
print( '*****')
k1 =islice(k, 3) #返回一个迭代器
for i in k1:
    print(i)  #输出了前三个值
print( '*****')

#2.
def prepend( value, iterable): #返回一个Iterator对象
    "向最前面加一个值"
    return chain( [value], iterable)
p=prepend(1,[2,3,4])

for i in p:
	print( i)
	
#3.
def tabulate( function, start=0):
    "return function(0), function(1),..."
    return map( function, count(start)) #回忆count:生成一个均匀的连续值，无穷的 ，因为它是一个Iterator

#4.
def tail(n, iterable):
    "返回迭代器指定后面几位的值"
    #tail(3, 'ABCDEFG')-->E F G
    return iter( collections.deque( iterable, maxlen=n))

#5.
def consume( iterator, n=None):
    ""
    if n is None:
        collections.deque( iterator, maxlen=0) #队列
    else:
        next( islice( iterator, n, n), None)

#6.
def nth(iterable, n, default=None):
    return next( islice( iterable, n, None), default) #回忆isliceh函数，iterator_slice 迭代器的切片操作
#next可以对于一个迭代器取出下一个值，default值是当迭代器耗尽的时候代替抛出的异常返回的值
#注意： islice( iterable, stop) 之后两个参数的时候，但是三个参数的时候是( it, start, stop)
print('6****')
print( nth( range(1,3), 0,) )
print('6****')

#7.
def all_equall( iterable):
    "所有值都一样的话， 返回True"
    g=groupby( iterable)
    return next(g, True) and not next(g, False)

#8.
def quantify( iterable, pred=bool):
    "查出predicate==True有多少次"
    return sum(map(pred, iterable)) #没看懂思密达，看懂了，比如[0,1,2,3] 就会返回3，毕竟bool(0)==False

#9.
def ncycles( ite,n):
    "返回元素n次"
    return chain.from_iterable( repeat(tuple(iterable), n))

#10.
def batched( iterable, n):
    if n<1:
        raise ValueError('n must be at least one')
    it =iter( iterable)
    while batch := tuple( islice(it, n)): # :=海象运算符，内部赋值用 if a:=10 <15....
        yield batch

#11.
def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    pass

#12.
def sumpord( vect1, vec2):
    #乘积的和
    pass

#13.
def sum_of_squares( it):
    return sumpord( *tee(it))

#14.
def transpose(it):
    pass


#15.
def matmul( m1, m2):
    #计算两个矩阵的乘积
    pass

#16.
def convolve( signal, kernel):
    pass

#17
def polynomial_from_roots( roots):
    "利用多项式的根，转为多项式的一般表达式"
    pass

#18.
def polynomial_eval( coefficients, x):
    pass

#19.
def iter_index( iterable, value, start=0):
    pass

#20.
def iter_index( ite, val, start=0):
    pass

#21.
def sieve( n):
    pass

#22.
def factor( n):
    #质因数分解，（会重复）
    pass

#23.
def flatten( list_of_lists):
    #列表融合？
    return chain.from_iterable( list_of_lists)

#24.
def repeatfunc(func, times=None, *args): #*是可变参数，可以传入一个列表
    "repeat calls to func with specified arguments."
    if times is None:
        return starmap(func, repeat(args)) #starmap 是一个生成器<=> 含有yield关键字 eg: starmap( pow, [(2,5),(3,2)]) --> 32, 9
    return starmap( func, repeat( args, times))

#25.
def triplewise( ite):
    # 'ABCDEFG'---> ABC BCD CDE DEF EFG
    pass

#26.
def sliding_window( iterable, n):
    #('ABCDEFG', 4) ----> ABCD BCDE CDEF DEFG  #什么跑马灯效果
    pass

#27.
def roundrobin( *iterables):
    pass

#28
def partition( pred, iterable):
    pass

#29.
def before_and_after( predicate, it):
    pass

#30.
def subslices( seq):
    #'ABCD' --> A AB ABC ABCD B BC BCD C CD D
    pass

#31.
def powerset( iterable):
    pass

#32.
def unique_everseen( iterable, key=None):
    pass

#33.
def unique_justseen( iterable, key=None):
    pass

#34.
def iter_except( func, exception, first=None):
    pass

#35.
def first_true( iterable, default=False, pred=None):
    #返回第一个真值，否则default
    pass

#36.
def nth_combination( iterable, r, index):
    pass

