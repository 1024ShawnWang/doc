
#1. ctypes对象，用于在共享内存上创建可被子进程继承的共享对象

#2. multiprocessing.Value( typecode_or_type, *args, Lock=True) 返回一个从共享内存上创建的 ctypes对象。

#3. multirprocessing.Array( typecode_or_type, size_or_initailizer, *, Lock=True) 从共享内存中申请，并返回一个具有 ctypes类型的 数组对象

#4. multiprocessing.sharedctypes模块，用来分配来自 共享内存的，可被子进程继承的 ctypes 对象

#4.1. multiprocessing.sharedctypes.RawArray( typecode_or_type, size_or_initializer) 从共享内存中申请，并返回一个 ctypes 数组

#4.2. multiprocessing.sharedctypes.RawValue( typecode_or_type, *args) 从共享内存中申请，并返回一个ctypes对象

#4.3. multiprocessing.sharedctypes.Array( typecode_or_type, size_or_initializer, *, Lock=True)

#4.4. multiprocessing.aharedctypes.Value( typecoce_or_type, *args, Lock=True) 返回一个纯 ctypes数组，或者在此之上，经过同步器包装过的进程安全的对象

#4.5  multiprocessing.sharedtypes.copy( obj) 将对象copy到共享内存，返回一个新的 ctypes对象

#4.6 multiprocessing.sharedctypes.synchronized( obj[, Lock])

#例子
from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_double  #在Python中操作 c语言中的对象

class Point( Structure):
    #__fields__ = [('x', c_double), ('y', c_double)] #双下引号会报错，引发下列错误
    #RuntimeError: (Point) TypeError: too many initializers
    _fields_ = [('x', c_double), ('y', c_double)]

def modify( n, x, s, A): #修改每个参数的属性
    n.value **= 2 # a =  a**2  a的平方
    #x.value ** = 2 #注意，就地操作，需要 **= 紧密连接，这是一个整体
    x.value **= 2
    s.value = s.value.upper()
    for a in A:
        a.x **= 2
        a.y **= 2

if __name__ == '__main__':
    lock = Lock()

    n = Value( 'i', 7) 
    x = Value( c_double, 1.0/3.0, lock=False)
    s = Array( 'c', b'hello world', lock=lock)
    A = Array(  Point, [(1.875, -6.25), (-5.75, 2.0), (2.375, 9.5)], lock=lock) #Point哪里来的? 开头定义的类

    p = Process( target=modify, args=(n, x, s, A) )
    p.start()
    p.join()

    print( n.value) #multiprocessing.Value对象，拥有 value属性，所以可以取得
    print( x.value)
    print( s.value) #multiprocessing.Array对象，拥有value 和 raw属性，用来保存和提取字符串
    print( [(a.x, a.y) for a in A] )
