
tel={'jack':4098, 'sape':4139} #1. 如何声明并且初始化一个字典

tel['guido']=4127 #2. 可变数据类型

print( tel)

print( tel['jack'])  

del tel['sape'] #3. 删除一对键值
print( tel)

tel['irv']=4127#4. 增加一对键值

print('******')
print( tel)
print('******')

print( list(tel))#5. 列表化字典，只会列表化键(key)

print( sorted( tel) )#6. 按照key排序，注意和其他sort函数的不同，这个返回值非空

print( {x:x**2 for x in (2,4,6)}) #7. 字典生成式

print( dict(sape=4139, guido=4127, jack=4098) #8.简单字符串作为键，可以使用dict保留字，用=，初始化字典

