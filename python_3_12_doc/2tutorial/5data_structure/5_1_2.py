#使用deque类来实现一个队列

from  collections  import deque

queue =deque( ['Eric', 'John', 'Michael'])

queue.append('Terry')
queue.append('Gramma')

print( queue.popleft() )
