
#class asyncio.Lock #实现一个用于 asyncio任务的互斥锁。非线程安全
'''
lock =asyncio.Lock()
async with lock:
    #访问共享资源
'''
#和下面的等价
'''
lock =asyncio.Lock()
await lock.acquire()
try:
    #访问共享资源
finally:
    lock.release()
'''

#coroutine acquire() #1.获取锁

#release() #2.释放锁

#locked #3.检查是否被锁

