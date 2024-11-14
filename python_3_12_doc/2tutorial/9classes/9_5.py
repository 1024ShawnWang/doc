    
#1. 如何声明一个派生类（子类）
#class DerivedClassName( BaseClassName):
#   pass

print(  isinstance( int, object) ) #True #2. 检查是否实例，包括自己

print( issubclass(bool, int) ) #True  #3.检查是否是子类





##9.5.1多重继承
#Class DerivedClassName( Base1, Base2, Base3) #1.如何声明

#2.属性的搜索顺序，最先是derivedClassName中搜索， Base1 -> base of Base1 ->Base2 -> base of Base2
#深度优先，先左后右


