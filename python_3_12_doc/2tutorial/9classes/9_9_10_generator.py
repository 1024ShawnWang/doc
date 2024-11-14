
#1.含有yield语句的就是生成器，通过生成器可以创造迭代器

def reverse( data):
    for index  in range( len(data)-1, -1, -1): #2.range(start,stop, step)  注意是 [start, stop) 
        yield data[ index]
#封装了 __next___()和__iter__办法

for char in reverse('golf'):
    print( char)


#9.10
#1.生成器生成式 和 列表生成式 非常相似
#不同点 ： 使用（）

r=sum( i*i for i in range(3))
print( r)


#注意到sum只接受 iterable对象，因为 generator一定是 iterable对象
