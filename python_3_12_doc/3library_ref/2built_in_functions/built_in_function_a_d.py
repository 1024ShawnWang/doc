
'''1 A: 6
abs()
aiter()
all()
anext()
any()
ascii()
'''

abs( -1) #1.1 输出值：int, float, 复数， 或者是任意一个实现了 __abs__()方法的类。 返回值： 大小（模)

# 1.2 aiter( async_iterable):  return asynchronous_iterator

# 1.3 all( iterable)---> True 如果iterable所有元素都是True，否则返回False
# 比如:
l=[1,2,3]
print( all(l)) #输出True

#1.4 awaitable anext( async_iterator, default)

#1.5 any any( iterable)--->True 如果iterable所有元素都是False，否则True
l=[0, 0, 0, 0.0]
print( any(l) )

#1.6 ascii() 和repr()方法很像，（repr(）办法尽量返回一个字符串，这个字符串包括一切能打印的信息')但是ascill()不同的是，遇到非ascill字符，会使用\x, \u \U来代替


'''2 B : 5
bin()
bool()
breakpoint()
bytearray()
bytes()
'''
# 2.1 bin() 转化一个整数变为二进制字符串形式（二进制的字符串表示形式），如果不是int对象，就一定要实现__index__()办法
#二进制的字符串表示形式会以0b开头，在python中。
print( bin(3) ) #'0b11' 

# 2.3 class bool( object=False, /)

# 2.3 breakpoint(*args, **kws)   ==pdb.set_trace()，并且不用显示地 import pdb

# 2.4 bytearray 

# 2.5 bytes 返回一个不可变对象，2.4的对象是可变对象


'''
3 C: 5
'''
print( callable( abs) ) # 3.1 callable()检查一个对象是否可调用

print( chr(97) ) # 3.2 97是'a'的unicode编码，和ord() 是互逆函数

#3.3 @classmethod 这是一个装饰器，会使得类的调用默认传入的第一个参数变为自己，类比于类的方法在l实例中的调用一样

#3.4 compile(source, filname, mode, ..) 从源代码编译为AST对象？？？？

#3.5 class complex(number=0,/)
#    class complex( string,/)
#    class complex( real=0, imag=0)
print( complex('-1.23+4.5j') ) #string
print( complex(-1.23, 4.5) ) #real,image

'''
4 D: 4
'''

#4.1 delattr ( object, attribute) 删除对象的指定属性

#4.2 class dict( **kwarg)
#    class dict( mapping, **kwarg)  #关键字参数（传入键-值对，与 命名关键字的区别？）
#    class dict( iterable, **kwarg) #

#4.3 dir() #返回目前local scope里面的名字，注意，这并非是系统的dir命令
print( dir() )
#    dir( obj )#obj必须实现__dir()__办法
import os
print( dir(os) ) #显示os模块的属性（ 变量和方法）

print( divmod(1, 2) ) #4.4 返回值（ a//b，a%b）  (0, 1) （向下取商，余数）
print( divmod(1.1, 2.0) #  ( math.float(1.1/2.0), 1.1%2.0)
