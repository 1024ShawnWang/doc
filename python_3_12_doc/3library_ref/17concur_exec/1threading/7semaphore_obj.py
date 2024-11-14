
#1.信号量对象管理一个内部计数器，默认值是1
#1.1 每次调用acquire()方法，计数器递减
#1.2 每次调用release()方法，计数器递增
#1.3 如果acquire()之后，计数器==0，将会阻塞，直到其他线程调用release()办法

#2. class threading.Semaphore( value=1) value的初始值严格比0小的时候，会引发ValueError异常

#3. class threading.BoundedSemaphore( value=1) 
