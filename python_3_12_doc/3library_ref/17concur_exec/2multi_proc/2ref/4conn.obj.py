
#1. Connection对象允许收发可以序列化的对象或者字符串。它们可以看作面向消息的连接套接字

#2. 通常使用Pipe创建 Connection对象。

#3. class multiprocessing.connection.Connection

#3.1 send( obj) #将一个对象发送到连接的另一端，可以使用recv()读取

#3.2 recv()返回一个由另一端使用 send(0发送的对象

#3.3 fileno() 

#3.4 close() 关闭连接对象

#3.5 poll( [ timeout]) 返回连接对象中，是否有可以读取的数据

#3.6 send_bytes( buffer[, offset[, size]])

#3.7 recv_bytes( [ maxlength]) #对比 recv()

#3.8 recv_bytes_int( buffer[, offset])

from multiprocessing import Pipe
a, b =Pipe() 
#print( type(a)) #<class 'multiprocessing.connection.Connection'>
a.send( [1, 'hello', None])
rec =b.recv() #返回的类型居然是动态的，发送的是list，返回的就是list，很神奇它怎么知道的
#print( type( rec)) #<class 'list'>

b.send_bytes( b'thank you')# 字节对象
print( a.recv_bytes() )

import array
arr1 = array.array('i', range( 5)) #‘i' for signed int 有符号整数
arr2 = array.array('i', [0]*10) 
print( 'arr2的长度是: ', arr2.itemsize) #居然是 4， 不知道为什么只占了四个字节
print( 'len(arr2): ', len( arr2)) #10, 这次长度是10了

a.send_bytes( arr1)
count = b.recv_bytes_into( arr2) #返回直接读取的arr2和 前面发送的 arr1的字节数

assert count == len( arr1) * arr1.itemsize #断言后面的如果错误，就会抛出断言异常 AssertionError
# itemsize 单个数组项的长度，单位是字节 1字节=8 bits

