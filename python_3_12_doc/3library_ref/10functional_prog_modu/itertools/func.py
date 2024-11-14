#这些函数，都返回一个迭代器

from itertools import *

#写一个函数，打印迭代器
def print_iter( ite):
    for i in ite:
        print( i)
    print( '****')

#1 itertools.accumulate( iterable[, function, *, initial=None])


#1.1 iterable和Iterator的区别： collections.abc.Iterator, collections.abc.Iterable
#前者有一个 next()方法，后者不一定有，比如[1,2,3]就是 Iterable的实例
print_iter( accumulate([1,2,3]) )

#itertools.batched(['roses','red', 'violets', 'blue', 2])#2.itertools.batched( iterable, n) 分批返还3.12版本加入

print_iter( chain( [1,2,3],[2,3,4] )) #3#1,2,3,2,3,4

#4#classmethod chain.from_iterable( iterable)

#5#itertools.combinations( iterable, r)，返回可迭代对象中，长度为r的子序列。返回一个迭代器
l=[1, 2, 3, 4]
k=[]
k.extend( combinations(l, 2)) #返回长度为2的所有子集
print( k) #extend也可以接受一个迭代器对象

#6# itertools.combinations_with_replacement( iterable, r)

#7
print_iter( compress([1,2,3],[1,0,0]))#1  因为选择器是1,0,0所以只会选择第一个bool(1)==True

#8
#print_iter( count(1,3))#1,4,7,........ 这就是迭代器的魅力，无穷的
for i in count(1,3):
    if i <10:
        print(i)
    else:
        print('****')
        break

#9. itertools.cycle( iterable) ，循环没有尽头

#10.itertools.dropwhile( predicate, iterable) 首次假值

#11.itertools.filterfalse( pre, iterable) 只返回假值

print_iter( groupby('AAABBBCCC'))#12.itertools.groupby( iterable, key=None)

#13. itertools.islice(iter, start, stop[, step])

#14. itertools.pairwise( iterable)


