import weakref, gc
#1.python会自动管理内存，（垃圾回收机制）只要指向对象的最后一个引用被删除，对象就会被回收
#（内存地址没有别名了，就会被认为不再需要这部分内存，就会将这部分内存标记为垃圾

class A:
    def __init__( self, value):
        self.value= value

    def __repr__( self):
        return str( self.value)


a =A( 10)    #创建了一个引用，所以不会被标记为垃圾

d = weakref.WeakValueDictionary()
d['primary']=a #2.特殊的办法，导致这个=不会创造引用（ref）

print( d['primary'])

del a   #删除此引用，那么就会被标记为垃圾
gc.collect() #立刻回收垃圾（相当于清除垃圾站）就是做一个标记罢了，非常快速

print( d['primary']) #因为我们删除了 A(10)的最后一个引用，所以这里会报错。注意d['primary']=a这个特殊的等号，不会创建ref，因此确实只有一个引用(ref)


#3.这个办法主要是为了追踪对象是否存活，因为一旦使用=，就会创造引用，而一个对象只要存在一个或者一个以上的引用，就不会被垃圾收集器标记。导致无法正常地追踪其行为，因此需要一个特殊的不会给对象添加引用的特殊办法，用来表明对象的行为
