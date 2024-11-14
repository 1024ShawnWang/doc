
#列表生成式

#1.
squares1 =[]
for x in range( 10):
    squares1.append( x**2)

print( squares1)

#但是我们额外声明了一个变量，循环结束之后，变量仍然存在
print( x)


#节省一个变量的空间，用lamda函数
squares2 =list( map( lambda x: x**2, range(10) ))
print( squares2)

#使用列表生成式子
squares3 =[ x**2 for x in range(10) ]
print( squares3)
#三种办法，我想你已经知道选哪个了



#2. 使用多重列表生成，注意括号即可
k = [ (x, y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print( k)
#它同下面的语法等价，请注意for 和 if 的顺序
k1=[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!= y:
            k1.append( (x, y) )
print( k1)#尤其注意输出的顺序，是和上面完全一致的

#3.也就是说列表生成式，其实***隐藏****了声明空列表以及append(()办法

#4.同样地有元组生成式，把【】改成（）

