from functools import *

#1. @functools.cache( user_function)

@cache
def factorial( n):
    return n *factorial(n-1) if n else 1 #f(0)=1 
print( factorial(10)) # 计算过的值，会被缓存
print( factorial(5)) #调用上面已经计算过的值


#2. @functools.cached_property( func) 类比 @property
import statistics
class DataSet:
    def __init__( self, sequence_of_numbers):
        self.data =tuple( sequence_of_numbers)
    @cached_property
    def stdev( self):
        return statistics.stdev( self.data)  #输出一系列数字的标准差


#3. functools.cmp_to_key( func) 将旧版的函数转移到python3新版本

#4. functools.lru_cache()

#5. @total_ordering() 必须实现下列方法其中之一 __lt__(), __le__(), __gt___(), __ge__(), 必须支持 _eq__办法
@total_ordering
class student:
    def __init__(self, f, l):
        self.firstname=f
        self.lastname=l
    def _is_valid_operand(self, other):
        return hasattr(other, 'lastname') and hasattr( other, 'firstname') # hasattr(obj, attr) 内置函数用来检查某个对象是否有某个属性的
    def __eq__( self, other):
        if not self._is_valid_operand( other):
            return NotImplemented
        return (self.lastname.lower(), self.firstname.lower()) ==( other.lastname.lower(), other.firstname.lower())#实现__eq__()办法
    def __lt__( self, other): #less than
        if not self._is_valid_operand( other):
            return NotImplemented
        return (self.lastname.lower(), self.firstname.lower()) <( other.lastname.lower(), other.firstname.lower())#实现__eq__()办法

o1 =student('xu','wang')
o2=student('wei','wang')
print( o2 >o1)  #注意我们并没有实现 >办法，这是由装饰器帮我们实现的

#6.partial( func, /, *args, **keywords):  # /的意思是，限制此前的参数必须是位置参数
'''实现的过程，同下述代码类似
def partila( func, /, *args, **kewwords):  #*是可变参数，**是关键字参数，list和dict
    def newfunc( *fargs, **fkewords):
        newkeywords ={**keywords, **fkeywords}
        return func(*args, *fargs, *newkeywords) #将参数自动填充进至指定的func, 并且生成一个新的函数
    #下面的是把原来函数的信息，绑定到要返回的函数上面
    newfunc.func =func
    newfunc.args=args
    newfunc.keywords =keywords
    return newfunc
'''
basetwo =partial( int, base=2) #返回一个新的函数
print( basetwo('10010') )
print( basetwo.func)  #

#python参数语法， /之前，只能是位置参数， *之后只能是 key-val形式的参数(包括，命名关键字参数（给定了key）和关键字参数两种），中间的就可以放置默认参和可变参数了。
#可变参数要用 *声明， 最后的关键字参数要用 **声明
#这一点官网没有廖雪峰讲的好
#关键字参数主要的作用是可以增加函数定义中的形式参数的数量

#7.partialmethod(func, /, *args, **keywords) #对照上面的理解，说出各个参数的名称

#8. reduce  reduce( f, [1,2,3]) =f(f(1,2),3)  对比map

#9. singledpatched  #将一个函数变为单分派generic function，

#10. singledpatchedmethod #将一个方法变为单分派 注意方法和函数的区别

#11. update_wrapper()

#12. wraps()
def my_decorator( f):
    @wraps(f)
    def wrapper( *args, **kwds):
        print( 'Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    print('called example function')

example()
