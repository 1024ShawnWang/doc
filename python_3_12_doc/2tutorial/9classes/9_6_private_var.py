
class Mapping:
    def __init__( self, iterable):
        self.items_list=[]
        self.__update( iterable)

    def update( self, literable):
        for item in literable:
            self.items_list.append( item)
    __update =update   #1.私有变只能从内部读写，所以这个类的子类在实例化的时候，即使重写了update方法，也只能使用Mapping类中国的update办法创建实例



class MappingSubclass( Mapping):

    def update( self, keys, values):
        for item in zip(keys, values):
            self.items_list.append( item)

l=[1,2,3]
#d = MappingSubclass( 'wang', 'xu')#按照MappingSubclass中的update办法初始化实例会报错
d=MappingSubclass( l)
print( d.items_list)


#2. 私有变量实际上是如下命名的，比如上面的 __update == _Mapping__update
