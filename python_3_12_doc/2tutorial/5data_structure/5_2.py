
#del语句，这并不是办法，这是一个语句，比如if

a=[1, 2, 3, 4]

del a[0]
print( a)

del a[:]
print( a)


del a #删除变量,估计是讲内存标记为可回收
print( a)#报错

