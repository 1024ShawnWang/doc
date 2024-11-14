
#1. 类有自己的属性attribute( 值和函数都算)

#2. __initi___()办法对类进行初始化

#3. 类的实例化和函数的调用很像

class MyClass():
    """simple example class"""
    i=12345

    def f( self):
        return "Hello World"



#9_3_4
x =MyClass()
print( x.f() ) #1. x.f() = MyClass.f( x) ,所以在使用x.f()时候，并没有按照声明的那样，传入一个参数。

#9_3_5
#1. 类的属性(attribute)包括两种( variable & method)
#2. 类的属性会被分配给所有对象
'''
class Dog():
    kind ="canine" # shared by all instances
    def __init__(self, name):
        self.name =name

d =Dog( 'Figo')
e =Dog( 'Buddy')

print( d.kind) #canine
print( e.kind) #also
print( d.name) #figo
print( e.name) #Buddy
'''

#3. 类的变量建议设置为不可变对象（因为类的属性可以被所有实例读写）
class Dog:
    tricks=[] #可变对象，会导致问题
    def __init__( self, name):
        self.name =name
    def add_trick(self, trick):
        self.tricks.append( trick)
d =Dog( 'fido')
e =Dog( 'buddy')
d.add_trick( 'roll over') # == Dog.add_trick( d, 'roll over') 使得类的变量tricks增加一个元素
e.add_trick( 'paly dead') # == Dog.add_trick( e, 'play dead') 使得类的变量tricks再增加一个元素
print( d.tricks) # d.tricks==Dog.tricks #输出 roll over, paly dead

#3.1 办法就是改为私有变量，仅有实例有
class Dog1:
    def __init__(self, name):
        self.tricks=[]  #为每一个dog新建一个lsit
        self.name=name
    def add_trick(self, trick):
        self.tricks.append( trick)  #4.即使类变量有tricks,也会先取用同一个scope的tricks，也就是实例变量




