
#异常链
'''
try:
    open('database.sqlit')#没有这个文件
except OSError:
    raise RuntimeError("处理异常时，又出现了一个异常") #1.表明异常的嵌套 during handling of the above exception, another exception occurred

'''

def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError( "无法打开数据库") from exc #2.使用from关键字来表明异常的因果关系 the above exception was the direct cause of the following exception.


