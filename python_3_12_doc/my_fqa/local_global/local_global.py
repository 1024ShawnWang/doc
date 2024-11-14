
#1. 在函数内部读取的变量，默认读取的是全局变量
#1. 在函数内部写入的变量（赋值），被认为是局部变量

i=1 #顶头写的，全局变量
def my_printer():
    print(i)#只有读取，没有赋值，会自动读取全局变量 i.
my_printer() #将输出 1

'''
def local_printer():
    i =i +1 #对i进行了赋值操作。此时i被认为是局部变量，但是局部变量i是没有初始值的，会报错
    print(i) 
local_printer() #报错变量i未绑定
'''



#2.nonlocal 关键字，声明此变量是上一层命名空间的变量，常常用于嵌套函数中，内层函数对外层函数字进行写操作
#上面的理解是错误，并不能声明是上一层命名空间的变量
'''
def local_printer():
    nonlocal i
    i =i +1 #对i进行了赋值操作。此时i被认为是局部变量，但是局部变量i是没有初始值的，会报错
    print(i) 
local_printer() #报错，nonlocal i没有发现任何绑定
'''

#3. python的作用域分为四类；
#3.1 全局作用域，开头定格写的，包括变量和函数和类 ，通过模块名  .   运算符直接可以取得
#3.2 局部作用域：函数或者类 内部的变量和内层函数，都在这个作用域
#3.3 封闭作用域：嵌套函数的内层函数**里面**， 定义的变量或者函数或者其他
#3.4 内建作用域：所有内置函数和异常所在的作用域



#4. 命名空间是一个映射（从名称到值）
#4.1 不同命名空间的名称不会产生任何关系
#4.2 模块属性 和 模块的全局变量 在同一个命名空间的定义域内
#4.3 这个映射在不同时间被创建，和销毁。
#4.3.1 内置函数的命名空间（从函数名称-->函数地址）存在整个python程序运行
#4.3.2 模块的命名空间，在读取模块定义时候创建，知道python程序停止
#4.3.3 函数的命名空间（函数自己拥有的属性（变量和函数） --地址）在被调用时候创建，在返回或者异常时候被删除,递归调用每次都有自己的命名空间，，


#5.作用域：python的一段源代码区域（命名空间的定义域）
#5.1 作用域是静态的，（废话，写好了开始运行的时候被一次性全部读取进去了).
#5.2 有三四个命名空间可以直接访问的作用域
#5.2.1 最内层作用域，包含局部名称，并首先在其中搜索


#我有一个严肃的问题，locals这个内置函数的源代码在哪里，我知道它应该是用c写的，那也应该有一个源代码啊
#
#但是我找到啦len函数，github项目上，请看 cpython/Python/bltinmodule.c文件有一个 _len()函数 1771行
#在1237行，有global函数的实现
#用c实现的内置函数好像都在里面了
#网址://github.com/python/cpython/blob/main/Python/bltinmodule.c