
class WareHouse():
    purpose ='storage'
    region ='west'

w1 =WareHouse()
print( w1.purpose, w1.region)

w2= WareHouse()
w2.region ='east'
print( w2.purpose, w2.region) #输出 storage east
#1. 变量按照scope前搜寻，优先匹配靠后的scope里的者值，这是因为设计者认为
#********后面的scope出现相同的变量的原因就是因为前面scope出现的变量完成不了程序的目的***************的这个理念，被所有开发者共同知道
#因此，自然会让程序选择靠后scope的变量声明。

#2. 因为1的存在，所以必须对变量存取进行封装，因为后面的开发者一旦写出类变量相同的名称就会覆盖类变量，导致出错。

#3.类的method不一定要 textually enclosed in the class definition.
def f1( self, x, y):
    return min( x, x+y)
Class C:
    f =f1 #如3描述的，函数定义在类的定义外面

    def g(self):
        return  "hello"

