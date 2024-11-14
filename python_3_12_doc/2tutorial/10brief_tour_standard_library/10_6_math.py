
import math
math.cos( math.pi/4) # cos(pi/4)=0.7

import random
print( random.choice( ['apple', 'pear', 'banana']) ) #2.随机在字符串列表中进行选择

print( random.sample(  range(100), 10) )   #3.从0-99，随机选择指定个不重复的项

print( random.random() )   #4.随机产生一个0-1之间的浮点数

print( random.randrange( 6) )     #5. 在 [0, 6)之间，随机输出一个整数


import statistics
data=[2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print( statistics.mean( data) )    #6. 输出平均值1.60...

print( statistics.median( data) )   #7.输出中位数 0.25, 0.5, 1.25, 1.25, 1.75, 2.75, 3.5结果是1.25

print( statistics.variance( data))  #8.输出方差1.3...




