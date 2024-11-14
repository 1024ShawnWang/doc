
#15. r
#15.1 class range( start, stop, step)

#15.2 repr( object)

#15.3 reversed( object) 获得一个反序的迭代器，object必须实现其中一个办法，__len__, __getitem__

#15.4 round( ndigits=None) None的时候，距离最近的整数，一样近，取偶数

#16. s

#16.1 class set( iterable) 

#16.2 setattr(oject, name, value)  类比getattr办法

#16.3 class slice( stop)
#     class slice( start, stop, step=None)

#16.4 sorted( iterable, /, *, key=None, reverse=False)  默认从小到大
print( sorted([1,2,3]) )

#16.5 @staticmethod 变为静态method 注意methodh和funciton的区别

#16.6 class str( object='')
#     class str( object=b'', encoding='utf-8', errors='strict') errors是什么？

#16.7 sum(iterable, /, start=0)

#16.8 class super( tyep, object_or_type=None) 调用父对象的方法

#17
#17.1 class tuple( iterable)

#17.2 class type( object)  #返回对象类型
#     class type( name, bases, dict, **kwds)

#18
#18.1 var() ^=^ locals()
#     var( object )----> object.__dict___

#19
#19.4 zip( *iterables, strict=False) 两个类型，按照索引，压缩成一对，返回一个元组的iterator
for item in zip( [1,2,3], ['sugar', 'spice', 'drink'] ):
	print( item)
#迭代器会停止在最短的可迭代对象用光的时候

#20.  __import__( name, globals=None, loclas=None, fromlist=(), level=0) 看不懂思密达反正和import的实现有关系
