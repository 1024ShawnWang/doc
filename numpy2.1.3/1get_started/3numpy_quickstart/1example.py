import numpy as np

a=np.arange(15)     #1.arange类比range(15)，不同的是生成[0,14]的ndarray对象
#print( a)
#print( type(a))#<class 'numpy.ndarray'>

a= a.reshape(3,5)   #2. reshape,array对象的方法，重写排列形状
#print( a)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
'''

#print( a.shape) #(3,4)#3. shape属性，行列

#print( a.ndim) #2 #4. ndim几维的，查[数量?

#print( a.dtype.name) #int64 #5.单个元素的数据类型

#print( a.itemsize) #8   #6. 5中的元素的数据类型所占用的大小（字节） ==ndarray.dtype.itemsize

#print( a.size) #15  #7. 元素总个数，==shape元素的乘积
b=np.arange( 24)
#print( b)

b=b.reshape(2,3,4)
#print(b)
'''
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
'''
#print( b.ndim) #3 #8.联系2. 为什么尾数维数是 3呢?好像真是[[[数量
#print( b.size) #24 #联系7. ==2x3x4=24真的哎


b =np.array( [6, 7, 8]) #9.传入一个列表去初始化ndarray
print(b)
print( type(b))
