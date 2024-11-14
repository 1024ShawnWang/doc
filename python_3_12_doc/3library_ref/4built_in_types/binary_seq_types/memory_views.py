
#1. memory view是支持缓冲区协议的对象，内置的对象支持此协议的有 bytes,  bytesarray

v =memoryview( b'abcdefg') #2. 创建一个memory view对象

print( v[1:4])  #3.支持切片操作

print( bytes( v[1:4] ) )  #4.转为字节


#4.一些方法。。。。


