#class asyncio.Semaphore( value=1) #信号量对象，非线程安全
# 信号量对象会管理一个内部计数器，该计数器会 随着 每次acquire()调用递减， 随着每次 release()调用递增
#  但是不会降到 <0 ，如果 acquire()发现其值为0，就会保持阻塞，直到某个任务调用了 release()

'''
sem =asyncio.Semaphore( 10)

async with sem:
    #操作共享的资源
'''
#这等价于
'''
sem =asyncio.Semaphore( 10)
await sem.acquire()
try:
    #操作共享的资源
finally:
    sem.release()
'''

#coroutine acquire() #2.获取一个信号量


#locker() #3.如果信号量对象无法被立即获取，则返回True

#release() #4.

#class asyncio.BoundedSemaphore( value=1)
#略过
