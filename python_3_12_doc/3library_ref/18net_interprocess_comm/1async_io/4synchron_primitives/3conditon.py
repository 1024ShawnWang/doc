
#class asyncion.Condition( lock=None)
'''
cond =asyncio.Condition()

async with cond:
    await cond.wait()
'''
#这等价于
'''
cond =asyncio.Conditon()

await cond.acquire()
try:
    await cond.wait()
finally:
    cond.release()
'''

#corotine acquire() #2.获取下层的锁

#notify( n=1) #3.

#locked() #4.

#notify_all() #5.唤醒所有正在等待此条件的任务

#release() #6.释放下层的锁

#coroutine wait() #7.等待直到收到通知为止

#coroutine wait_for( predicate) #8.等待直到目标值变为true
