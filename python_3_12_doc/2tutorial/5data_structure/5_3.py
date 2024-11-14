
#元组，

t =12345, 54321, 'tinjin'#1. 声明并初始化
print( t[0])


u=t, (1,2,3,4,5) #2.合并
print( u)

#t[0]=8888 #3.报错，无法赋值

v=( [1,2,3], [4,5,6] )#4.但是可以包括可变对象
print( v)

single_tuple=('hello',)#5.单个元组的声明必须使用逗号

x, y, z =t#6. unpacking解压缩，（读值
print( x, y ,z)
