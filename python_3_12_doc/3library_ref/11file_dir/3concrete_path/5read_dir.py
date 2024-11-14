from pathlib import *

#1. Path.iterdir()  #当路径对象是一个目录的时候，返回目录内容
p =Path('/')
for i in p.iterdir():
    print(i)

#2. Path.glob( pattern, *, case_sensitive=None)解析相对于此路径的通配符pattern, 返回所有匹配的文件，比如返回当前目录，所有.py结尾的文的迭代器
p=Path('.') #当前目录
print( p.glob('*,py'))

#3. Path.rglob

$. Path.walk(top_down=True, ....) 遍历指定文件的一种方式，第一个就是文件的入口了
