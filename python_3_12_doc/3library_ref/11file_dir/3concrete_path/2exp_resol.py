from pathlib import *

#1. classmethod Path.home() #返回家目录
print( Path.home()) 

#2. classmethod Path.expanduser()  #允许使用shell中的~符号
p= PosixPath('~/wangxu') #此对象并不存在
print( p.expanduser())

#3. classmethod Path.cwd() #返回运行此程序的目录  current working directory

#4. Path.absolute() #改为绝对路径
p =Path('test')
print( p.absolute())

#5. Path.resolve() 绝对化路径，并且解析任何符号链接（但是~无法解析，难道只有. 和 .. ?) 符号链接又称软链接，快捷方式就一种软链接？
p =Path('.')
print( p.resolve())

#6. Path.readlink() #返回符号链接指向的路径(软链接)
