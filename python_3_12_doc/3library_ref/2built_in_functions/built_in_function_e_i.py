
'''
5 e : 3
'''

# 5.1 enumerate( iterable ,start=0)

# 5.2 eval( expression, globals=None, locals=None)  #看不懂思密达

# 5.3 exec(object, globals=None, locals=None, /, *, closure=None)  #看不懂思密达，但是global, locals 跟命名空间有关，维护了一个字典，全称--内容
# locals()和 globals()也有这么两个内置函数

# 6 f
#6.1 filter( function, iterable)
# 如果指定了function, ==( item for item in iterable if function( item)) 返回一个生成器
#    没指定 function  ==( item for item in iterable if item)  
l =filter( None, [1,0,2] ) 
print ( l)

#6.2 class float( number=0.0, /)
#     class float( string, /)
float()
print(  float('1.2') )

#6.3 format( value, format_spec='')
#空字符 '' 的情况下， ==str( value)

#6.4 class frozenset( iterable=set() ) --> frozenset 

'''
7 g :
'''

#7.1 getattr(object, name) == object.name
#    getattr(object, name, default) 找不到值就返回default的值

#7.2 globals() 返回一个目前模块命名空间维护的字典o


'''
8 h :
'''

#8.1 hasattr(object, name) 对象有这个属性就返回True

#8.2 hash( object) 返回hash值	

#8.3 help()
#寻找事是有顺序的 modelue function class method keyword  documentation topic

#8.4 hex( int ) #转为十六进制，\0x开头


'''
9 I
'''
#9.1 id() 对象的唯一id，就是内存地址在python中的表示，

#9.2 input()
#    input( prompt)

#9.3 class int( number=0)
#    class int( string, /, base=10 )

#9.4 isinstance( object, classinfo )#classinfo可以是元组，只要是其中之一的实例，就返回True

#9.5 issubclass( class, classinfo )#和isinstance机制大概，也可以传入元组

#9.6 iter( object )
#    iter( object, sentinel)返回一个迭代器对象

