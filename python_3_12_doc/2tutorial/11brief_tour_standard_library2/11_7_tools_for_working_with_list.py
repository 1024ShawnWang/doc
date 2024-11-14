#提供了很多和List类似的对象，在某些方面更精细

from array import array
a=array( 'H', [4000,10,700,2222])
print( sum(a)) #1.array可以自动对出现的数字求和
print( a[1:3]) #2.array支持灵活的切片

from collections import deque #队列的实现，注意popleft()办法

import bisect
scores =[(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort( scores, (300, 'ruby')) #3.自动排序插入，返回值空
print( scores)

from heapq import heapify, heappop, heappush
data =[1,3,5,7,9,2,4,6,8,0]
heapify( data)#将data排序为一个heap order(最小值在0索引)[实现也不难啊好像]
heappush( data, -5) #插入一个元素
l=[heappop(data) for i in range(3)] #排序三次,弹出三个，列表生成式
print( l)
