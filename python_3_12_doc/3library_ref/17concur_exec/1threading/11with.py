
#1. 这个模块中所有具有 acquire和 release方法的对象，都可以用作with语句的上下文管理器.
#1.1 就是说，进去语句时，自动调用acquire方法，退出语句块的时候自动调用release方法

'''
with some_lock:
    #某操作

和下面的语句等价

some_lock.acquire()
try:
    #某操作
finally:
    some_lock.release()
'''

#2. 可以使用with的对象有 Lock, Rlock, Condition, Semaphore, BoundedSemaphore
