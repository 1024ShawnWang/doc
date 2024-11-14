#1. class json.JSONDecoder( *, object_hook=None, parse_float=None, ...) #简单的python解码器
'''它将json对象，变为python对象

    obj( json基本对象)      ->  dict
    array                       list
    string                      str
    number(int)                 int
    number(real)                float
    true                        True
    false                       False
    null                        None
'''

#2. decode( s)  将json对象，返回为python的 str对象，这个str肯定包含json原来的数据

#3. raw_decode( s) 看不懂思密达



#1. clas  json.JSONEncode( *, skipkeys=False,...)  对比上面的1，相反

#2. default( o)  在子类中实现这种办法使其返回 o 的可序列化对象，或调用基础实现，（引发TypeError)
'''
def defaultl(self, o):
    try:
        iterable =iter(o)
    except TypeError:
        pass
    else:
        return list( iterable)
    return super().default( o) #让基类(父类)引发TyepError异常
'''

#3. encode( o) 返回pytho数据结构的json  字符串表达形式
import json
print( json.JSONEncoder().encode( {"foo": ["bar", "baz"] } )   ) #虽然内容一样，但是前者无法用python处理，而后者已经是str对象了

#4. iterencode( o)
